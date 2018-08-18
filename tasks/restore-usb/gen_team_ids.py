#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random as rd
import sys
import os

def random_str(chars, length):
    return ''.join([rd.choice(chars) for i in range(length)])

chars = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

def expand(template, team_num):
    s = template.replace('#', str(team_num))
    return ''.join([rd.choice(chars) if c == '?' else c for c in s])

magic_len = 10
flag_template = 'LKL{{MD5_0F_TRRU3_1N_C0OK1E5_{magic}}}'

if len(sys.argv) < 2:
    print('Usage: gen_team_ids.py <teams_count> [team_id_template]')
    print('Generates new team_ids.txt file')
    print('Team id template is a string containing those sequences:')
    print(' # - team number')
    print(' ? - random char (a-z, A-Z, 0-9)')
    print('The default is "team_#_????????"')
    exit()

if len(sys.argv) == 2:
    template = 'team_#_????????'
else:
    template = sys.argv[2]

rd.seed(int.from_bytes(os.urandom(8), 'little'))
n = int(sys.argv[1])

content = ''
for i in range(n):
    content += expand(template, i + 1) + '\n'

with open('team_ids.txt', 'w') as file:
    file.write(content)
print('Done')
