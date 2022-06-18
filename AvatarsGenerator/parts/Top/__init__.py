from random import choice
from .Accesories import get_accesories
from .Hats import get_hats
from .Glasses import get_glasses
from .Hairs import get_hair, HAIRS_DOWN
from ..FacialHair import get_facial_hairs

def get_top(config):
   hair = get_hair(config)
   accesories = get_accesories(config)
   hats = get_hats(config)
   glasses = get_glasses(config)
   facial_hairs = get_facial_hairs(config)

   output = [
      '<g id="Top" transform="translate(-1.000000, 0.000000)">',
   ]
   hair_name = config.get('hair_name')
   if hair_name and hair_name in HAIRS_DOWN:
      output.extend([facial_hairs, hair])
   else:
      output.extend([hair, facial_hairs])

   output.extend([
      hats,
      glasses,
      accesories,
   ])

   output.append('</g>')
   return '\n'.join(output)
    
    