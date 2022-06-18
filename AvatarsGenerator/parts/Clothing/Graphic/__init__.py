from .Bat import Bat
from .Bear import Bear
from .Cumbia import Cumbia
from .Deer import Deer
from .Diamond import Diamond
from .Hola import Hola
from .Pizza import Pizza
from .Resist import Resist
from .Selena import Selena
from .SkullOutline import SkullOutline
from .Skull import Skull

GRAPHICS = {
    # 'Blank': (lambda: ''),
    'Bat': Bat,
    'Bear': Bear,
    'Cumbia': Cumbia,
    'Deer': Deer,
    'Diamond': Diamond,
    'Hola': Hola,
    'Pizza': Pizza,
    'Resist': Resist,
    'Selena': Selena,
    'SkullOutline': SkullOutline,
    'Skull': Skull
}

GRAPHICS_NAMES = list(GRAPHICS.keys())


def get_graphic(config):
    name = config.get('graphic_name')
    if not name:
        return '' 
    return GRAPHICS[name]()