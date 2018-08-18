import argparse
import os
from itertools import count
from typing import Dict, Tuple

from PIL import Image


def text2Int(text):
    """Convert a text string into an integer"""
    from functools import reduce
    return reduce(lambda x, y: (x << 8) + y, map(ord, text))

def binpow(a, x, mod):
    res = 1
    a %= mod
    while (x):
        if (x & 1):
            res *= a
            res %= mod
        a *= a
        a %= mod
        x //= 2
    return res

def make_task(flag: str) -> str:
    p, q = 3133337, 12366840791999209948692555126473347817429082377404105602900112759029020897962103961700188060656739843170052707951730899288468934345783491185522360600642243
    n = p*q
    e = 65537
    m = text2Int(flag)
    c = binpow(m, e, n)
    s = f"e = {e}, n = {n}, c = {c}"
    return s

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Make dem tasks")
    parser.add_argument('where', help = "Where would you like task files outputted to")
    flag_group = parser.add_mutually_exclusive_group()
    flag_group.add_argument('--flags', help = "File to take flags from", type=list)
    flag_group.add_argument('--flag', help = "Single flag to be hidden")
    parser.add_argument('--v', help = "Print made tasks", action = "store_true")
    g = parser.parse_args()
    output = dict() # type: Dict[str, Tuple[str, str]]
    if g.flag:
        output[0] = make_task(g.flag)
    elif g.flags:
        for i, flag in zip(count(), g.flags):
            output[i] = make_task(flag)
    else:
        from flags_and_teams import data
        for team_id, flag in data.items():
            output[team_id] = make_task(flag)

    if g.v:
        print(output)
    else:
        nd = dict()
        for team_id, outp in output.items():
            nd[team_id] = (outp, data[team_id])
        with open(g.where, 'w+') as f:
            f.write("data = ")
            f.write(repr(nd))
