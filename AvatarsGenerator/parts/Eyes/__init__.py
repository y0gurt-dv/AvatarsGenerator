from .Closed import Closed
from .Cry import Cry
from .Default import Default
from .EyeRoll import EyeRoll
from .Happy import Happy
from .Hearts import Hearts
from .Side import Side
from .Squint import Squint
from .Surprised import Surprised
from .Wink import Wink
from .WinkWacky import WinkWacky
from .XDizzy import XDizzy

EYES = {
    "Closed": Closed,
    "Cry": Cry,
    "Default": Default,
    "EyeRoll": EyeRoll,
    "Happy": Happy,
    "Hearts": Hearts,
    "Side": Side,
    "Squint": Squint,
    "Surprised": Surprised,
    "Wink": Wink,
    "WinkWacky": WinkWacky,
    "XDizzy": XDizzy,
}
EYES_NAMES = list(EYES.keys())

def get_eyes(name):
    if name not in EYES_NAMES:
        raise ValueError('Invalid eyes name')
    return EYES[name]()