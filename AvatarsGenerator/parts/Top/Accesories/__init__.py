from .Eyepatch import EyePatch
from random import choice


ACCESORIES = {
    'EyePatch': EyePatch
}
ACCESORIES_NAMES = list(ACCESORIES.keys())



def get_accesories(config):
    name = config.get('accesories_name')
    if not name:
        return ''

    return (
        '<g id="accesories" transform="translate(-1.000000, 0.000000)">'
            f'{ACCESORIES[name]()}'
        '</g>'
    )
