import argparse
from itertools import count
from typing import Dict, Tuple


def make_task(flag: str) -> str:
    key = 0xee  # some x 0<x<256
    encrypted_flag = []
    for i in range(len(flag)):
        encrypted_flag.append(ord(flag[i]) ^ key)
    encrypted_flag.reverse()
    return " ".join(str(e) for e in encrypted_flag)

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
