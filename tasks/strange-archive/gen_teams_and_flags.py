#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random as rd
import sys
import os

def random_str(chars, length):
    return ''.join([rd.choice(chars) for i in range(length)])

chars = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
magic_len = 10
flag_template = 'LKL{{S4Y_H3LLO_T0_G1T_{magic}}}'

if len(sys.argv) < 2:
    print('Usage: gen_teams_and_flags.py <teams_count>')
    print('Generates new teams_and_flags.py file')
    exit()

rd.seed(int.from_bytes(os.urandom(8), 'little'))
n = int(sys.argv[1])

content = '''#!/usr/bin/env false
# -*- coding: utf-8 -*-

data = {
'''

with open('team_ids.txt') as f:
    ids = f.read().split('\n')

for i in range(n):
    team_id = ids[i]
    content += '    "{}": "{}",\n'.format(team_id, flag_template.format(magic=random_str(chars, magic_len)))

content += '}\n'

with open('teams_and_flags.py', 'w') as file:
    file.write(content)
print('Done')
