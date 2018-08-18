#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import teams_and_flags
import os
import subprocess as sp

BASE_PORT = 36000

def reverse(fname):
    with open(fname, 'rb') as f:
        b = f.read()
    b = bytes(reversed(b))
    with open(fname, 'wb') as f:
        f.write(b)

def cat(fname1, fname2, fname_out):
    with open(fname1, 'rb') as f:
        b1 = f.read()
    with open(fname2, 'rb') as f:
        b2 = f.read()
    with open(fname_out, 'wb') as f:
        f.write(b1)
        f.write(b2)

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

def encrypt(s):
    return str(bytes([i ^ 0xFF for i in bytes(s, 'utf-8')]))[2:-1]

def main():
    if len(sys.argv) < 2:
        print('Usage: gen.py <team_id>')
        return

    # Prepare magic and flag
    team_no = int(sys.argv[1])
    team_id = get_team_id(team_no)
    flag = teams_and_flags.data[team_id]

    # Prepare directory
    try:
        os.stat('team_' + team_id)
        sh('rm', '-rf', 'team_' + team_id)
    except FileNotFoundError:
        pass
    sh('cp', '-r', '--no-target-directory', 'dist/', 'team_' + team_id)
    os.chdir('team_' + team_id)

    # EXECUTABLE 1

    # Generate source code
    with open('sh3/build.sh3') as file:
        s = file.read()
    s = s.replace('@@__MESSAGE__@@', encrypt('There are no flags here...'))
    with open('sh3/build.sh3', 'w') as file:
        file.write(s)

    # Compile source code
    sh('../bin/sh3', 'build', env=False)

    # Clean up
    sh('cp', 'task', 'task1')

    # EXECUTABLE 2

    # Generate source code
    with open('sh3/build.sh3') as file:
        s = file.read()
    s = s.replace(encrypt('There are no flags here...'), encrypt(flag))
    with open('sh3/build.sh3', 'w') as file:
        file.write(s)

    # Compile source code
    sh('../bin/sh3', 'build', env=False)

    # Clean up
    sh('cp', 'task', 'task2')

    # COMBINE
    reverse('task2')
    cat('task1', 'task2', 'task')

    sh('cp', 'task', '../task_' + team_id)
    os.chdir('..')
    sh('rm', '-rf', 'team_' + team_id)
    print('Done')

if __name__ == '__main__':
    main()
