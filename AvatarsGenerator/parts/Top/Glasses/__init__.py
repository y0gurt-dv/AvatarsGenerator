from .Kurt import Kurt
from .Prescription1 import Prescription1
from .Prescription2 import Prescription2
from .Round import Round
from .Sunglasses import Sunglasses
from .Wayfarers import Wayfarers

GLASSES = {
    'Blank': (lambda: ''),
    "Kurt": Kurt,
    "Prescription1": Prescription1,
    "Prescription2": Prescription2,
    "Round": Round,
    "Sunglasses": Sunglasses,
    "Wayfarers": Wayfarers,
}
GLASSES_NAMES = list(GLASSES.keys())


def get_glasses(config):
    name = config.get('glasses_name')
    if not name:
        return ''

    return (
        '<g id="glasses" transform="translate(62.000000, 85.000000)">'
            f'{GLASSES[name]()}'
        '</g>'
    )