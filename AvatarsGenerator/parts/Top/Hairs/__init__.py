from .Bob import Bob
from .Bun import Bun
from .Curly import Curly
from .Dreads1 import Dreads1
from .Dreads2 import Dreads2
from .Dreads import Dreads
from .Frida import Frida
from .Frizzle import Frizzle
from .FroBand import FroBand
from .Fro import Fro
from .LongButNotTooLong import LongButNotTooLong
from .MiaWallace import MiaWallace
from .ShaggyMullet import ShaggyMullet
from .Shaggy import Shaggy
from .ShavedSides import ShavedSides
from .ShortCurly import ShortCurly
from .ShortFlat import ShortFlat
from .ShortRound import ShortRound
from .ShortWaved import ShortWaved
from .Sides import Sides
from .StraightStrand import StraightStrand
from .Straight1 import Straight1
from .Straight import Straight
from .TheCaesarSidePart import TheCaesarSidePart
from .TheCaesar import TheCaesar

HAIRS = {
    'Blank': (lambda color: ''),
    'Dreads': Dreads,
    'ShaggyMullet': ShaggyMullet,
    'StraightStrand': StraightStrand,
    'Straight1': Straight1,
    'Straight': Straight,
    'Dreads1': Dreads1,
    'Frizzle': Frizzle,
    'Shaggy': Shaggy,
    'ShortCurly': ShortCurly,
    'ShortFlat': ShortFlat,
    'ShortRound': ShortRound,
    'ShortWaved': ShortWaved,
    'Sides': Sides,
    'TheCaesarSidePart': TheCaesarSidePart,
    'TheCaesar': TheCaesar,
    'Bob': Bob,
    'Bun': Bun,
    'Curly': Curly,
    'Frida': Frida,
    'FroBand': FroBand,
    'Fro': Fro,
    'LongButNotTooLong': LongButNotTooLong,
    'MiaWallace': MiaWallace,
    'Dreads2': Dreads2,
    'ShavedSides': ShavedSides,
}
HAIRS_DOWN = [
    'Dreads1',
    'Frizzle',
    'Shaggy',
    'ShortCurly',
    'ShortFlat',
    'ShortRound',
    'ShortWaved',
    'Sides',
    'TheCaesarSidePart',
    'TheCaesar',
]
HAIRS_UP =[
    'Blank'
    'Bob',
    'Bun',
    'Curly',
    'Frida',
    'FroBand',
    'Fro',
    'LongButNotTooLong',
    'MiaWallace',
    'Dreads2',
    'ShavedSides',
]

HAIRS_NAMES = list(HAIRS.keys())




def get_hair(config):
    name = config.get('hair_name')
    if not name:
        return ''
    color = config.get('hair_color')
    return (
        '<g id="Hair" stroke-width="1" fill-rule="evenodd">'
            f'{HAIRS[name](color)}'
        '</g>'
    )