#!/bin/sh

rm -rf venv

python3 -m venv venv
venv/bin/pip install --upgrade pip
venv/bin/pip install -r requirements.txt

venv/bin/python3 dobot.py
