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

def main():
    if len(sys.argv) < 2:
        print('Usage: gen.py <team_id>')
        return

    # Prepare magic and flag
    team_id = int(sys.argv[1])
    flag = teams_and_flags.data['team_' + str(team_id)]
    flag_subst = 'LKSHL{U5E_STR1NG5_UT1LITY_##########}'

    try:
        os.stat('src/program')
    except FileNotFoundError:
        os.chdir('src/')
        sh('deps/sh3', 'build', env=False)
        os.chdir('..')
    sh('cp', 'src/program', 'program_team' + str(team_id))
    sh('sed', '-i', 's/{}/{}/g'.format(flag_subst, flag), 'program_team' + str(team_id))
    print('Done')

if __name__ == '__main__':
    main()
