from .Eyes import get_eyes
from .Mouth import get_mouth
from .Eyebrow import get_eyebrows
from .Nose import get_nose

def get_face(config):
    eyebrow_name= config.get('eyebrow_name')
    eyes_name= config.get('eyes_name')
    mouth_name= config.get('mouth_name')
    return (
        '<g id="face" transform="translate(76.000000, 82.000000)" fill="#000000">'
            '<g id="nose" transform="translate(28.000000, 40.000000)" fill-opacity="0.16" style="fill-opacity: 0.16;">'
                f'{get_nose()}'
            '</g>'
            '<g id="Mouth" transform="translate(2.000000, 52.000000)">'
                f'{get_mouth(mouth_name)}'
            '</g>'
            '<g id="Eyes" transform="translate(0.000000, 8.000000)">'
                f'{get_eyes(eyes_name)}'
            '</g>'
            '<g id="EyeBrow">'
                f'{get_eyebrows(eyebrow_name)}'
            '</g>'
        '</g>'
    )
