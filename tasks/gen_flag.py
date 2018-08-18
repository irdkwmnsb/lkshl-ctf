import argparse
import random
from string import ascii_lowercase, ascii_uppercase, digits

ALPHABET = ascii_lowercase + ascii_uppercase + digits


def genstr(length):
    return ''.join([random.choice(ALPHABET) for _ in range(length)])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate flags")
    parser.add_argument('where', help="flags_and_teams.py", type=str)
    parser.add_argument('flag', help="Flag containing <magic>", type=str)
    parser.add_argument('count', help="How many flags", type=int, default=200)
    g = parser.parse_args()
    flag = g.flag
    flags = dict()
    for _ in range(g.count):
        team_id = genstr(12)
        new_flag = flag.replace('<magic>', genstr(8))
        flags[team_id] = new_flag

    with open(g.where, 'w+') as f:
        f.write("data = ")
        f.write(repr(flags))