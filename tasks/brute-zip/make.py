import argparse
import base64
import os
from itertools import count
from typing import Dict, Tuple

def sh(*args, sudo=False, env=True, fatal=True):
    import subprocess as sp
    if sudo:
        print('Requesting sudo privileges for command:')
        print('  ' + ' '.join(args))
        args = ['sudo', *args]
    if env:
        args = ['/usr/bin/env', *args]
    ret = sp.call(args)
    if ret != 0:
        if fatal:
            print('Command failed (return status {}):'.format(ret))
            print('  ' + ' '.join(args))
            raise OSError('Command failed (return status {})'.format(ret))
        else:
            return False
    return True

def make_task(flag: str) -> str:
    password = "9258"
    with open('flag.txt', 'w+') as f:
        f.write(flag)
    sh('zip', '--password', password, 'task.zip', 'flag.txt')
    with open('task.zip', 'rb') as f:
        out = base64.standard_b64encode(f.read()).decode()
    sh('rm', 'task.zip')
    sh('rm', 'flag.txt')
    return out

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
