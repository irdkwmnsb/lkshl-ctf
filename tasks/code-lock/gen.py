#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import teams_and_flags
import os
import subprocess as sp

BASE_PORT = 36000

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
        print('Usage: gen.py <NUM_TEAMS>')
        return

    # Prepare magic and flag
    n = int(sys.argv[1])
    for i in range(n):
        team_id = get_team_id(i + 1)
        print('({}/{}) Generating subdir for team with id {}'.format(i + 1, n, team_id))
        flag = teams_and_flags.data[team_id]

        try:
            os.stat(team_id)
            sh('rm', '-rf', team_id)
        except FileNotFoundError:
            pass
        sh('cp', '-r', 'wsroot', team_id)
        sh('sed', '-i', 's/@@_FLAG_@@/{}/g'.format(flag), team_id + '/flag.php')
        
        # Пофиг на это, мы не поднимаем N инстансов lighttpd, обойдёмся одним nginx'ом
        # sh('cp', 'lighttpd.conf', 'lighty_team{}.conf'.format(team_num))
        # sh('sed', '-i', 's/@@_PORT_@@/{}/g'.format(BASE_PORT + team_num), 'lighty_team{}.conf'.format(team_num))
        # sh('sed', '-i', 's#@@_ROOT_@@#{}#g'.format(os.path.join(os.getcwd(), 'team' + str(team_num))), 'lighty_team{}.conf'.format(team_num))

    print('Done')

if __name__ == '__main__':
    main()
