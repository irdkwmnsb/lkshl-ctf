#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from tqdm import tqdm

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

def array_to_csv(a):
    return ', '.join(map(str, a))

def encrypt(s):
    b = bytes(s, 'utf-8')
    n = len(b)
    key = [((i + 143) * 185) % 253 for i in range(n)]
    return [i ^ j for i, j in zip(b, key)]

def get_team_id(n):
    with open('team_ids.txt') as f:
        return f.read().split('\n')[n-1]

def main():
    for team_id, flag in tqdm(teams_and_flags.data.items()):
        # Prepare directory
        sh('cp', '-r', '--no-target-directory', 'dist/', 'team_' + team_id)
        os.chdir('team_' + team_id)

        # Generate source code
        with open('templates/main.cs') as file:
            s = file.read()
        s = s.replace('@@_PERMITTED_KEY_@@', array_to_csv(encrypt(flag)))
        with open('src/main.cs', 'w') as file:
            file.write(s)

        # Compile source code
        sh('../bin/sh3', 'build', env=False)

        # Clean up
        sh('cp', 'task.exe', '../out/{}.exe'.format(team_id))
        os.chdir('..')
        sh('rm', '-rf', 'team_' + team_id)
        print('Done')


    print('Done')

if __name__ == '__main__':
    main()
