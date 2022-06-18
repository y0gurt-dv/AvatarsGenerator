from .BlazerShirt import BlazerShirt
from .BlazerSweater import BlazerSweater
from .CollarSweater import CollarSweater
from .ShirtCrewNeck import ShirtCrewNeck
from .Shirt import Shirt
from .ShirtScoopNeck import ShirtScoopNeck
from .ShirtVNeck import ShirtVNeck
from .Overall import Overall
from .Hoodie import Hoodie
from .Graphic import get_graphic

CLOTHING = {
    "BlazerShirt": BlazerShirt,
    "BlazerSweater": BlazerSweater,
    'CollarSweater': CollarSweater,
    "ShirtCrewNeck": ShirtCrewNeck,
    "Shirt": Shirt,
    "ShirtScoopNeck": ShirtScoopNeck,
    "ShirtVNeck": ShirtVNeck,
    'Overall': Overall,
    'Hoodie': Hoodie
}
CLOTHING_NAMES = list(CLOTHING.keys())


def get_clothing(config):
    name = config.get('clothing_name')
    if not name:
        return ''
    color = config.get('clothing_color')
    

    return (
        '<g id="Clothing" transform="translate(0.000000, 170.000000)">'
            f'{CLOTHING[name](color)}'
            '<g transform="translate(77.000000, 60.000000)">'
                f'{get_graphic(config)}'
            '</g>'
        '</g>'
    )