import random
from .parts.colors import HAIR_COLORS, PALETTE_COLORS, SKIN_COLORS
from .parts.Mouth import MOUTHS_NAMES
from .parts.Eyebrow import EYEBROWS_NAMES
from .parts.Eyes import EYES_NAMES
from .parts.Top.Hats import HATS_NAMES
from .parts.Top.FacialHair import FACIALHAIRS_NAMES
from .parts.Top.Glasses import GLASSES_NAMES
from .parts.Top.Accesories import ACCESORIES_NAMES
from .parts.Top.Hairs import HAIRS_NAMES
from .parts.Clothing import CLOTHING_NAMES, get_clothing
from .parts.Clothing.Graphic import GRAPHICS_NAMES
from .parts.body import get_skin
from .parts.face import get_face
from .parts.Top import get_top
from typing import Literal
from wand.image import Image
from wand.color import Color


def _config_fields_validator(available_list, config, field, need_error=True, need_choice=True):
    if not config.get(field) and need_choice:
        config[field] = random.choice(available_list)
    if need_error and config.get(field) not in available_list and need_choice:
        raise ValueError(f'Invalid {field}')

    return config

CONFIG_FIELDS = {
    "eyebrow_name": EYEBROWS_NAMES,
    "eyes_name": EYES_NAMES,
    "mouth_name": MOUTHS_NAMES,
    "skin_color": SKIN_COLORS,
    "clothing_name": CLOTHING_NAMES,
    "clothing_color": PALETTE_COLORS,

    'graphic_name': GRAPHICS_NAMES,

    'hat_name': HATS_NAMES,
    'hat_color': PALETTE_COLORS,

    'hair_name': HAIRS_NAMES,
    'hair_color': HAIR_COLORS,

    'facial_hair_name': FACIALHAIRS_NAMES,
    'facial_hair_color': HAIR_COLORS,

    'glasses_name': GLASSES_NAMES, 

    'accesories_name': ACCESORIES_NAMES,

}
NOT_AVAILABLE_FIELDS = {
    'hat_name': {
        'names': {
            'Hijab': {
                'fields': {
                    'facial_hair_name': {
                        'available_names': []
                    }, 
                    'facial_hair_color': {
                        'available_names': []
                    },
                }
            },
        },
        'all': [
            'hair_name', 'hair_color',
            'accesories_name'
        ]
    },
    'hair_name': {
        'names': {
            "Dreads":{
                'fields': {'facial_hair_name':{'available_names': ['Blank', 'MoustacheFancy', 'MoustacheMagnum']}}},
            "ShaggyMullet":{
                'fields': {'facial_hair_name':{'available_names': ['Blank', 'MoustacheFancy', 'MoustacheMagnum']}}},
            "StraightStrand":{
                'fields': {'facial_hair_name':{'available_names': ['Blank', 'MoustacheFancy', 'MoustacheMagnum']}}},
            "Straight1":{
                'fields': {'facial_hair_name':{'available_names': ['Blank', 'MoustacheFancy', 'MoustacheMagnum']}}},
            "Straight":{
                'fields': {'facial_hair_name':{'available_names': ['Blank', 'MoustacheFancy', 'MoustacheMagnum']}}},
        },
        'all': [
            'hat_name', 'hat_color',
            'accesories_name'
        ]
    },
    'accesories_name': {
        'all': [
            'hat_name', 'hat_color',
            'hair_name', 'hair_color',
            'glasses_name'
        ]
    },
    'glasses_name': {
        'all': [
            'accesories_name'
        ]
    },
    'clothing_name': {
        'names': {
            'BlazerShirt': {'fields': {'graphic_name': { 'available_names': []},}},
            'BlazerSweater': {'fields': {'graphic_name': { 'available_names': []},}},
            'ShirtScoopNeck': {'fields': {'graphic_name': { 'available_names': []},}},
            'ShirtVNeck': {'fields': {'graphic_name': { 'available_names': []},}},
            'Overall': {'fields': {'graphic_name': { 'available_names': []},}},
            'Hoodie': {'fields': {'graphic_name': { 'available_names': []},}},
        },
    },

}

OPTIONAL_FIELDS = [
    "hat_name", 
    'hat_color',

    "hair_name",
    'hair_color',
    
    "facial_hair_name",
    'facial_hair_color',
    
    "glasses_name",
    "accesories_name",
    'graphic_name',
] 

def generate_avatar(
        output_type: Literal['png_bytes', 'svg_string']='svg_string', 
        config: dict={}, 
        auto_optional: bool=True):
    """
    Config example. If field in OPTIONAL_FIELDS and auto_optional == True , all optional field will be filled in automatically.
    All required fields (fields that are not in OPTIONAL_FIELDS)  that are not specified in the config will be automatically filled

        config = {
            'eyebrow_name': '',
            'eyes_name': '',
            'mouth_name': '',
            'skin_color': '',
            "clothing_name": '',
            "clothing_color": '',

            'graphic_name': '',

            'hat_name': '',
            'hat_color': '',

            'hair_name': '',
            'hair_color': '',

            'facial_hair_name': '',
            'facial_hair_color': '',

            'glasses_name': '', 

            'accesories_name': '',
        }
        
    OPTIONAL_FIELDS = [
        "hat_name", 
        'hat_color',

        "hair_name",
        'hair_color',
        
        "facial_hair_name",
        'facial_hair_color',
        
        "glasses_name",
        "accesories_name",
        'graphic_name',
    ] 
            
    
    
    
    
    
    
    """
    
    output_string = '<?xml version="1.0"?>'
    output_string += '<svg width = "264" height = "280" viewBox = "0 0 264 280" fill = "none" xmlns = "http://www.w3.org/2000/svg" >'
    

    for field_name, available_list in CONFIG_FIELDS.items():
        if config.get(field_name):
            need_choice = False
        elif field_name in OPTIONAL_FIELDS and auto_optional:
            need_choice = random.choice([True, False])
        else:
            need_choice = True
    
        _config_fields_validator(
            available_list=available_list, 
            config=config, 
            field=field_name, 
            need_error=field_name.find('name') != -1,
            need_choice=need_choice
        )
    
    
    for field_name, field_config in NOT_AVAILABLE_FIELDS.items():
        field = config.get(field_name)
        if not field:
            continue
        
        if 'all' in field_config:
            for delete_field in field_config['all']:
                config.pop(delete_field, '')
        
        if 'names' in field_config:
            if field in field_config.get('names', []):
                for for_delete_field_name, for_delete_field_name_config in field_config['names'][field]['fields'].items():
                    if config.get(for_delete_field_name) not in for_delete_field_name_config['available_names']:
                        config.pop(for_delete_field_name, '')
    
    
    
    output_string += get_skin(config)   
    output_string += get_face(config)
    output_string += get_clothing(config)
    output_string += get_top(config)
    
    
    output_string += '</svg>'

    if output_type == 'svg_string':
        return output_string
    
    if output_type == 'png_bytes':
        with Image(blob=output_string.encode(), background=Color('rgba(0, 0, 0, 0)')) as image:
            png_image = image.make_blob("png")
            return png_image

generate_avatar()