from .Hat import Hat
from .Hijab import Hijab
from .Turban import Turban
from .WinterHat1 import WinterHat1
from .WinterHat2 import WinterHat2
from .WinterHat3 import WinterHat3
from .WinterHat4 import WinterHat4


HATS = {
    "Hat": Hat,
    "Hijab": Hijab,
    "Turban": Turban,
    "WinterHat1": WinterHat1,
    "WinterHat2": WinterHat2,
    "WinterHat3": WinterHat3,
    "WinterHat4": WinterHat4,
}
HATS_NAMES = list(HATS.keys())


def get_hats(config):
    name = config.get('hat_name')
    if not name:
        return ''
    color = config.get('hat_color')
    
    return (
        '<g id="hat">'
            f'{HATS[name](color)}'
        '</g>'    
    )
