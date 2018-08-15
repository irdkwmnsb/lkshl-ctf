#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import sys
from os import getenv, scandir, getcwd, chdir
from PIL import Image, ImageDraw, ImageFont

font_dirs = [
    '/usr/share/fonts/TTF',
    '{}/.fonts'.format(getenv('HOME')) if getenv('HOME') is not None else None
]

def find_font(fontname):
    cwd = getcwd()
    for dir in font_dirs:
        if dir is None:
            continue
        try:
            chdir(dir)
            for i in scandir():
                if i.name.lower() == '{}.ttf'.format(fontname).lower():
                    try:
                        chdir(cwd)
                    except BaseError as e:
                        print(e)
                        raise e
                    return '{}/{}'.format(dir, i.name)
        except FileNotFoundError:
            chdir(cwd)
            continue
        except OSError:
            chdir(cwd)
            continue
    raise OSError('Resource not found')

def load_font(fontname, fontsize):
    try:
        font = ImageFont.truetype('{}.ttf'.format(fontname), fontsize)
        return font
    except OSError: # Because PIL searches for fonts only in W*ndows directory
        font = ImageFont.truetype('{}'.format(find_font(fontname)), fontsize)
        return font

def main():
    if len(sys.argv) < 4:
        print('Usage: write_text.py <original_image> <text> <save_path>')
        return
    font = load_font('UbuntuMono-R', 16)   # Нужно, чтобы UbuntuMono-R.ttf был в /usr/share/fonts/TTF
    imgpath = sys.argv[1]
    text = sys.argv[2]
    savepath = sys.argv[3]
    img = Image.open(imgpath)
    draw = ImageDraw.Draw(img)
    draw.text((100, 100), text, font=font, fill=(0, 0, 0))

    img.save(savepath)
    img.close()

if __name__ == '__main__':
    main()
