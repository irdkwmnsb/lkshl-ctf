import argparse
from itertools import count
from typing import Dict

import qrcode
import multiprocessing
from PIL import ImageDraw, Image
from _io import BufferedWriter

import os


def make_pic(flag: str) -> Image:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(flag)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.convert('RGB')
    draw = ImageDraw.Draw(img)
    color = (255,255,255)
    draw.line((0, 0, 110, 110), fill=color, width=20)
    draw.line((img.width, 0, img.width-110, 110), fill=color, width=20)
    draw.line((0, img.height, 110, img.height-110), fill=color, width=20)
    return img


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
            flag.save(os.path.join(g.where, str(team_id) + ".png"))