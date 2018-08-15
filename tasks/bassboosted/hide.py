#!/usr/bin/python3

import os
import wave
import struct

from argparse import ArgumentParser
from itertools import cycle


def get_args():
    parser = ArgumentParser()
    parser.add_argument('--dir', help='output directory', required=True)
    parser.add_argument('--ratio', help='amplitude multiplier (default 0.002)', type=float, default=0.002)
    parser.add_argument('--folders', help='put sounds in separate folders', action='store_true')
    parser.add_argument('--container', help='container to hiding a flag inside', required=True)
    return parser.parse_args()


def load_wav_amps(path):
    with wave.open(path, 'rb') as wav:
        raw = wav.readframes(wav.getnframes())
    amps = []
    for i in range(0, len(raw), 2):
        amps.append(struct.unpack('<h', raw[i:i+2])[0])
    return amps


def save_stereo_wav(path, amps):
    raw = [struct.pack('<h', amp) for amp in amps]
    with wave.open(path, 'wb') as wav:
        wav.setnchannels(2)
        wav.setsampwidth(2)
        wav.setframerate(8000)
        wav.writeframesraw(b''.join(raw))


def build_flag(flag):
    get_path = lambda symbol: 'speech/%s.wav' % symbol.lower()
    return sum(map(load_wav_amps, map(get_path, flag)), [])


def insert_flag(container, flag, ratio):
    result = []
    for c, f in zip(container, cycle(flag)):
        result.extend([c, c + int(f * ratio)])
    return result


if __name__ == '__main__':
    args = get_args()
    
    if not os.path.exists(args.dir):
        os.makedirs(args.dir)

    if args.folders:
        path = '%s/%%s/sound.wav' % args.dir
    else:
        path = '%s/%%s.wav' % args.dir

    i = 0
    container = load_wav_amps(args.container)
    from flags_and_teams import data
    for token, flag in data.items():
        print('%d: Processing token %s' % (i, token))
        result = insert_flag(container, build_flag(flag), args.ratio)
        if args.folders:
            os.makedirs('%s/%s' % (args.dir, token))
        save_stereo_wav(path % token, result)
        i += 1
