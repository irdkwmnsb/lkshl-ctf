#!/bin/bash

./token_generator.py --seed "redbutton" --mask "LKL{bo0Om_%s}" --count 200 --length 3  --pretty > tokens.py
