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
            raise OSError('Command failed (return status {})')
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

    # Prepare directory
    sh('cp', '-r', '--no-target-directory', 'dist/', 'team' + str(team_id))
    os.chdir('team' + str(team_id))

    # Generate picture file
    sh('../write_text.py', '../blank.png', flag, 'rootfs/untitled.png')

    # Compile image file. WARNING: takes 128 MiB of disk space! (but will be gzipped afterwards)
    sh('fallocate', '-l', str(128 * 2 ** 20), 'usb.img')
    sh('mkfs.vfat', 'usb.img')
    sh('mkdir', '-p', 'mnt')
    sh('mount', '-t', 'vfat', '-o', 'loop,noexec,nosuid,nodev,noatime,uid={}'.format(os.getuid()), 'usb.img', 'mnt/', sudo=True)
    os.chdir('rootfs')
    sh('cp', '-r', '.', '../mnt')
    os.chdir('..')
    sh('umount', 'mnt', sudo=True)
    sh('sync', sudo=True)
    sh('mkfs.vfat', 'usb.img')
    print('Compressing image...')
    sh('tar', '-czf', '../files-team{}.tar.gz'.format(team_id), 'usb.img')

    # Return back most of used disk space
    sh('rm', 'usb.img')
    print('Done')

if __name__ == '__main__':
    main()
