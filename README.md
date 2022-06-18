# AvatarGenerator

A simple avatar generator with the ability to export to PNG and SVG. 

The whole system is built on SVG.

The idea and all the parts were taken from [getavataaars.com](https://getavataaars.com)



Developed by y0gurt-dv 2022.

# Parts

Lists of all the preset parts you can import from the library. 

You can specify your own colors in the color fields, but if the color is not specified, it will be selected from the preset ones.

```python
from AvatarsGenerator import (
    HAIR_COLORS,
    PALETTE_COLORS,
    SKIN_COLORS,
    MOUTHS_NAMES,
    EYEBROWS_NAMES,
    EYES_NAMES,
    HATS_NAMES,
    FACIALHAIRS_NAMES,
    GLASSES_NAMES,
    ACCESORIES_NAMES,
    HAIRS_NAMES,
    CLOTHING_NAMES,
    GRAPHICS_NAMES,
)
```

### Examples of How To Use

```python
from AvatarsGenerator import generate_avatar

# Example of config 
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
png_bytes = generate_avatar(
    config=config, 
    output_type='png_bytes', 
    #Optional parameter. Default True
    auto_optional=True
)
with open('avatar.png', 'wb') as fp:
    fp.write(png_bytes)


```

if auto_optional == True

- All optional field will be filled in automatically

- All required fields (fields that are not in OPTIONAL_FIELDS)  that are not specified in the config 


