#!/bin/bash

./token_generator.py \
    --seed "redbutton" \
    --mask "LKL{bo0Om_%s}" \
    --count 500 \
    --length 3 \
    --pretty \
> tokens.py
