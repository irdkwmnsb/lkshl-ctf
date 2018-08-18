import _io
import argparse
from itertools import count
import os


def rot_char(c: str, rot: int):
    if ord(c) in range(ord('а'), ord('я') + 1):
        return chr((ord(c) - ord('а') + rot) % 32 + ord('а'))
    if ord(c) in range(ord('А'), ord('Я') + 1):
        return chr((ord(c) - ord('А') + rot) % 32 + ord('А'))
    if ord(c) in range(ord('a'), ord('z') + 1):
        return chr((ord(c) - ord('a') + rot) % 26 + ord('a'))
    if ord(c) in range(ord('A'), ord('Z') + 1):
        return chr((ord(c) - ord('A') + rot) % 26 + ord('A'))
    if ord(c) in range(ord('0'), ord('9') + 1):
        return chr((ord(c) - ord('0') + rot) % 10 + ord('0'))
    return c


def rot_str(c: str, rot: int):
    return ''.join([rot_char(i, rot) for i in c])


def make_flag(flag: str):
    org = "Ваш флаг - " + flag
    org = rot_str(org, -7)
    return org


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
        if not os.path.exists(g.where):
            os.makedirs(g.where)
        for team_id, flag in output.items():
            with open(os.path.join(g.where, str(team_id) + ".txt"), 'w', encoding="UTF-8") as f:
                f.write(str(flag))
