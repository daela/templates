#! /usr/bin/env python
# coding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import os


if __name__ == "__main__":
    
    print("!!")
    parser = argparse.ArgumentParser(description='Split image for A4 printing')
    parser.add_argument('image_file',help="the source image")
    parser.add_argument('-H', type=int, help="Minimum Horizontal number of page", default=1)
    parser.add_argument('-V', type=int, help="Minimum Veritcal number of page", default=1)
    parser.add_argument('-L', action='store_true', help="Landscape orientation")

    args = parser.parse_args()
    print(args)

    split_image(args.image_file, args.H, args.V, args.L)
