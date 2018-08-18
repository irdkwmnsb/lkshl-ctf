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

def make_task(flag, team_id):
    sh('mkdir', '-p', 'team' + str(team_id))
    os.chdir('team' + str(team_id))
    with open('flag.txt', 'w') as f:
        f.write(flag)
    with open('file.txt', 'w') as f:
        f.write('There is nothing here')
    sh('git', 'init')
    sh('git', 'add', '.')
    sh('git', 'config', 'commit.gpgSign', 'false')
    sh('git', 'config', 'user.name', 'n0b0dy')
    sh('git', 'config', 'user.email', 'n0b0dy@sicamp.ru')
    sh('git', 'commit', '-m', 'Initial commit')
    sh('rm', 'flag.txt')
    sh('git', 'add', 'flag.txt')
    sh('git', 'commit', '-m', 'Removed flag.txt')
    sh('zip', '-r', '../out/{}.zip'.format(team_id), 'file.txt', '.git')
    os.chdir('..')
    sh('rm', '-rf', 'team' + str(team_id))

def main():
    sh('mkdir', 'out')
    for team_id, flag in teams_and_flags.data.items():
        make_task(flag, team_id)
    print('Done')

if __name__ == '__main__':
    main()
