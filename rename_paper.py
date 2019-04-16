#!/usr/bin/env python
import os
import re
import sys
import argparse
import lxml.html
import subprocess
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('file')
args = parser.parse_args()

subprocess.call('pdf2txt.py -p1 -o /tmp/tmp.html "{}"'.format(args.file), shell=True)

with open('/tmp/tmp.html', encoding='utf-8') as f:
    html = f.read()

dom = lxml.html.fromstring(html)

styles = dom.xpath('//span[contains(@style, "font-size")][string-length(text()) > 10][not(contains(text(), "cid:"))]/@style')
font_sizes = np.array([int(i.split('font-size:')[-1].split('px')[0]) for i in styles])
title = dom.xpath('//span[contains(@style, "font-size")][string-length(text()) > 10][not(contains(text(), "cid:"))]')[font_sizes.argmax()].text_content()

name = '_'.join(title.split()).replace(',', '_').replace(':', '').replace('/', '').replace('?', '').lower() + '.pdf'

os.rename(args.file, os.path.join(os.path.dirname(args.file), name))
