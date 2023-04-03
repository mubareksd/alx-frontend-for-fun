#!/usr/bin/python3
"""markdown2html module
"""
import os
import sys

len = len(sys.argv)

if not len < 3:
    md = sys.argv[1]
    out = sys.argv[2]

if len < 3:
    print("Usage: ./markdown2html.py README.md README.html")
    exit(1)

if not os.path.exists(md):
    print("Missing {}".format(md))
    exit(1)
exit(0)
