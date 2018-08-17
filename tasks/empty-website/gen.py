#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import teams_and_flags
import os
import subprocess as sp

def sh(*args, sudo=False, env=True, fatal=True):
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

def get_team_id(n):
    with open('team_ids.txt') as f:
        return f.read().split('\n')[n-1]

def main():
    if len(sys.argv) < 2:
        print('Usage: gen.py <team_id>')
        return

    # Prepare magic and flag
    team_id = int(sys.argv[1])
    flag = teams_and_flags.data[get_team_id(team_id)]

    sh('cp', '-r', 'webroot', 'webroot_team' + str(team_id))
    sh('sed', '-i', 's/@@_FLAG_@@/{}/g'.format(flag), 'webroot_team{}/admin/X9k2dLIA/index.html'.format(team_id))

    print('Done')

if __name__ == '__main__':
    main()
