#!/usr/bin/env bash

mkdir -p bin
if ! [[ -x "bin/nani" ]]; then
    mkdir -p tmp
    cd tmp
    git clone https://github.com/kodo-pp/nani
    mv nani/nani ../bin
    cd ..
    rm -rf tmp
    chmod +x bin/nani
fi

if ! which ncat &>/dev/null; then
    echo "You need to install the 'nmap' package to continue"
    exit 1
fi
