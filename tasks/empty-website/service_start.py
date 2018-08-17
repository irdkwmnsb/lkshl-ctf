#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import subprocess as sp

BASE_PORT = 28000

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
        print('Usage: service_start.py <team_id>')
        print('Starts web server for specified team in foreground')
        return

    team_id = int(sys.argv[1])

    sh('bin/nani', '-p', str(BASE_PORT + team_id), '-d', 'webroot_team' + str(team_id))
    print('*** Exited ***')

if __name__ == '__main__':
    main()
