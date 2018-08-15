import argparse
import os
from itertools import count
from typing import Dict

from PIL import ImageDraw, Image


def make_pic(flag: str) -> Image:
    bits = ''.join('{0:08b}'.format(ord(x), 'b') for x in flag)
    image = Image.open("lkl_logo.png")  # type: Image
    image.load()
    w, h = image.size[0], image.size[1]

    c = (0xf0, 0xff, 0xff)

    draw = ImageDraw.Draw(image)
    for index, num in enumerate(bits):
        if num == '1':
            draw.rectangle((index * 2, h - 2, index * 2 + 1, h), c)

    return image

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Make dem tasks")
    parser.add_argument('where', help = "Where would you like task files outputted to")
    flag_group = parser.add_mutually_exclusive_group()
    flag_group.add_argument('--flags', help = "File to take flags from", type = list)
    flag_group.add_argument('--flag', help = "Single flag to be hidden")
    parser.add_argument('--v', help = "Open made QR", action = "store_true")
    g = parser.parse_args()
    output = dict() # type: Dict[str, Image]
    if g.flag:
        output[0] = make_pic(g.flag)
    elif g.flags:
        for flag, i in zip(count(), g.flags):
            output[i] = make_pic(flag)
    else:
        from flags_and_teams import data
        for team_id, flag in data.items():
            output[team_id] = make_pic(flag)

    if g.v:
        for team, pic in output.items():
            pic.show()
    else:
        if not os.path.exists(g.where):
            os.makedirs(g.where)
        for team_id, flag in output.items():
            flag.save(os.path.join(g.where, str(team_id) + ".bmp"))