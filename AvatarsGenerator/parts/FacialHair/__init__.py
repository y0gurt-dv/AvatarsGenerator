from random import choice
from ..colors import HAIR_COLORS
from .BeardLight import BeardLight
from .BeardMagestic import BeardMagestic
from .BeardMedium import BeardMedium
from .MoustacheFancy import MoustacheFancy
from .MoustacheMagnum import MoustacheMagnum

FACIALHAIRS = {
    'Blank': (lambda color: ''),
    'BeardLight': BeardLight,
    'BeardMagestic': BeardMagestic,
    'BeardMedium': BeardMedium,
    'MoustacheFancy': MoustacheFancy,
    'MoustacheMagnum': MoustacheMagnum,

}
FACIALHAIRS_NAMES = list(FACIALHAIRS.keys())


def get_facial_hairs(config):
    name = config.get('facial_hair_name')
    if not name:
        return ''
    color = config.get('facial_hair_color')


    return (
        '<g id="FacialHair" transform="translate(49.000000, 72.000000)">'
            f'{FACIALHAIRS[name](color)}'
        '</g>'
    )