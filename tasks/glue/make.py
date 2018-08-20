import _io
import argparse
from itertools import count
import os

def make_flag(flag: str):
    from subprocess import check_output
    from hashlib import md5
    s = check_output(['bash','./Generation/generator', flag, md5(b'holy_fullking_shit').hexdigest()])
    return s.split(b'\n')[-1].decode()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make dem tasks")
    parser.add_argument('where', help="Where would you like task files outputted to")
    flag_group = parser.add_mutually_exclusive_group()
    flag_group.add_argument('--flags', help="File to take flags from", type=list)
    flag_group.add_argument('--flag', help="Single flag to be hidden")
    parser.add_argument('--v', help="write output to stdout", action="store_true")
    g = parser.parse_args()
    output = dict()
    if g.flag:
        output[0] = make_flag(g.flag)
    elif g.flags:
        for flag, i in zip(count(), g.flags):
            output[i] = make_flag(flag)
    else:
        from flags_and_teams import data

        for team_id, flag in data.items():
            output[team_id] = make_flag(flag)

    if g.v:
        print(output)
    else:
        nd = dict()
        for team_id, outp in output.items():
            nd[team_id] = (outp, data[team_id])
        with open(g.where, 'w+') as f:
            f.write("data = ")
            f.write(repr(nd))
