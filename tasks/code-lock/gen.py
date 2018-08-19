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

def get_team_num(n):
    with open('team_ids.txt') as f:
        return f.read().split('\n')[n-1]

def main():
    sh('rm', '-rf', 'out')
    sh('mkdir', '-p', 'out')
    # Prepare magic and flag
    for team_id, flag in teams_and_flags.data.items():
        sh('cp', '-r', 'wsroot', 'out/' + team_id)
        sh('sed', '-i', 's/@@_FLAG_@@/{}/g'.format(flag), 'out/{}/flag.php'.format(team_id))

    #sh('cp', 'lighttpd.conf', 'lighty_team{}.conf'.format(team_num))
    #sh('sed', '-i', 's/@@_PORT_@@/{}/g'.format(BASE_PORT + team_num), 'lighty_team{}.conf'.format(team_num))
    #sh('sed', '-i', 's#@@_ROOT_@@#{}#g'.format(os.path.join(os.getcwd(), 'team' + str(team_num))), 'lighty_team{}.conf'.format(team_num))

    print('Done')

if __name__ == '__main__':
    main()
