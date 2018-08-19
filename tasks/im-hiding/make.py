import _io
import argparse
from itertools import count
import os

BIN = {"0": "\u200B",
       "1": "\uFEFF"}

def decorate(func):
    def make_flag(flag):
        return "<flag>"+func(flag)+"</flag>"
    return make_flag

@decorate
def make_flag(flag: str):
    binary = ''.join([format(i, '08b') for i in flag.encode()])
    hidden = ''.join([BIN[i] for i in binary])
    return hidden


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Make dem tasks")
    parser.add_argument('where', help = "Where would you like task files outputted to")
    flag_group = parser.add_mutually_exclusive_group()
    flag_group.add_argument('--flags', help = "File to take flags from", type = list)
    flag_group.add_argument('--flag', help = "Single flag to be hidden")
    parser.add_argument('--v', help = "write output to stdout", action = "store_true")
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
        if not os.path.exists(g.where):
            os.makedirs(g.where)
        for team_id, flag in output.items():
            with open(os.path.join(g.where, str(team_id)+".txt"), 'w', encoding="UTF-8") as f:
                f.write(str(flag))

