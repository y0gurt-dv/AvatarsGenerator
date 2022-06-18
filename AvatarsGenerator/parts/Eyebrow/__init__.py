from .Angry import Angry
from .AngryNatural import AngryNatural
from .Default import Default
from .DefaultNatural import DefaultNatural
from .FlatNatural import FlatNatural
from .FrownNatural import FrownNatural
from .RaisedExcited import RaisedExcited
from .RaisedExcitedNatural import RaisedExcitedNatural
from .SadConcerned import SadConcerned
from .SadConcernedNatural import SadConcernedNatural
from .UpDown import UpDown
from .UpDownNatural import UpDownNatural


EYEBROWS = {
    'Angry': Angry,
    'AngryNatural': AngryNatural,
    'Default': Default,
    'DefaultNatural': DefaultNatural,
    'FlatNatural': FlatNatural,
    'FrownNatural': FrownNatural,
    'RaisedExcited': RaisedExcited,
    'RaisedExcitedNatural': RaisedExcitedNatural,
    'SadConcerned': SadConcerned,
    'SadConcernedNatural': SadConcernedNatural,
    'UpDown': UpDown,
    'UpDownNatural': UpDownNatural,
    'Blank': (lambda: '')
}

EYEBROWS_NAMES = list(EYEBROWS.keys())


def get_eyebrows(name):
    if name not in EYEBROWS_NAMES:
        raise ValueError('Invalid eyebrows name')
    
    return EYEBROWS[name]()