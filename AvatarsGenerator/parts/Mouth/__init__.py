from .Concerned import MouthConcerned
from .Default import MouthDefault
from .Disbelief import MouthDisbelief
from .Eating import MouthEating
from .Grimace import MouthGrimace
from .Sad import MouthSad
from .ScreamOpen import MouthScreamOpen
from .Serious import MouthScreamOpen
from .Smile import MouthSmile
from .Tongue import MouthTongue
from .Twinkle import MouthTwinkle
from .Vomit import MouthVomit

MOUTHS = {
    "Concerned": MouthConcerned,
    "Default": MouthDefault,
    "Disbelief": MouthDisbelief,
    "Eating": MouthEating,
    "Grimace": MouthGrimace,
    "Sad": MouthSad,
    "ScreamOpen": MouthScreamOpen,
    "ScreamOpen": MouthScreamOpen,
    "Smile": MouthSmile,
    "Tongue": MouthTongue,
    "Twinkle": MouthTwinkle,
    "Vomit": MouthVomit,
}

MOUTHS_NAMES = list(MOUTHS.keys())


def get_mouth(name):
    if name not in MOUTHS_NAMES:
        raise ValueError('Invalid mouths name')
    return MOUTHS[name]()
