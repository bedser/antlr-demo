#!/bin/bash
set -e
DIR=$(dirname $0)
curl -o "$DIR/antlr-4.9.3-complete.jar" https://www.antlr.org/download/antlr-4.9.3-complete.jar
cd $DIR
virtualenv venv
venv/bin/pip3 install antlr4-python3-runtime==4.9.3
ln -s venv/bin/python python
