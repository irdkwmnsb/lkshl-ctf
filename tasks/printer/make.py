import argparse
import os
from itertools import count, cycle
from multiprocessing.pool import Pool
from typing import Dict, Tuple

from PIL import Image
import numpy as np


def make_pic(flag):
    bits = ''.join('{0:08b}'.format(ord(x), 'b') for x in flag)
    ar = np.array(Image.open("org.bmp"))
    ar = np.rot90(ar)
    for i, c in zip(range(ar.shape[0]), cycle(bits)):
        ari = np.logical_or(ar[i], np.uint8(np.round(np.random.rand(ar[0].shape[0]) * 0.6)))
        if (c == '1'):
            ar[i] = ari
        else:
            ar[i] = np.zeros(ar[i].shape)
    ar = np.rot90(ar, k=3)

    img = Image.fromarray(np.uint8((1-ar)*255))
    img = img.convert("RGBA")
    img = img.resize((img.width*4, img.height*4))
    white = Image.new("RGBA", img.size, (256,) * 4)
    white2 = Image.new("RGBA", img.size, (240,) * 4)
    off = 180
    img = img.resize((img.width - off, img.height - off))

    white.paste(img, (off//2,)*2)
    img = white

    img = img.rotate(2.34, Image.BICUBIC)

    img = Image.alpha_composite(white2, img)
    img = img.convert("L")
    return img


where = "./out"


def initializer(*_where: str) -> None:
    global where
    where = ''.join(_where)

def make_and_save(data: Tuple[str,str]):
    team = data[0]
    flag = data[1]
    p = make_pic(flag)
    p.save(os.path.join(where, str(team) + ".jpg"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make dem tasks")
    flag_group = parser.add_mutually_exclusive_group(required=True)
    flag_group.add_argument('--flags', help="File to take flags from", type=list)
    flag_group.add_argument('--flag', help="Single flag to be hidden")
    flag_group.add_argument('--from-file', help="Input from flags_and_teams.py", action="store_true")

    output_group = parser.add_mutually_exclusive_group(required=True)
    output_group.add_argument('--where', help="Where would you like task files outputted to")
    output_group.add_argument('--v', help="Open made scan", action="store_true")

    g = parser.parse_args()
    output = dict()  # type: Dict[str, Image]

    if g.flag:
        output.update([make_pic(['0', g.flag])])
    elif g.flags:
        for flag, i in zip(count(), g.flags):
            output[i] = make_pic([i, flag])[1]

    elif g.where and g.from_file:
        from flags_and_teams import data
        pool = Pool(5, initializer=initializer, initargs=(g.where))
        if not os.path.exists(g.where):
            os.makedirs(g.where)
        pool.map(make_and_save, list(data.items()))
        exit(0)

    elif g.from_file:
        from flags_and_teams import data
        for team_id, flag in data.items():
            output.update([make_pic([team_id, flag])])

    print(output)
    if g.v:
        for team, pic in output.items():
            pic.show()
    elif g.where:
        if not os.path.exists(g.where):
            os.makedirs(g.where)
        for team_id, flag in output.items():
            save((team_id, flag))
