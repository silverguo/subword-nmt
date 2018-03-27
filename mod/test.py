import sys
import codecs
import re
import copy
import argparse
from collections import defaultdict, Counter


def create_parser():

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="learn BPE-based word segmentation")

    parser.add_argument(
        '--input', '-i', type=argparse.FileType('r', encoding='UTF-8'),
        metavar='PATH', required=True, 
        help="Input file (required)")

    return parser


if __name__ == '__main__':

    parser = create_parser()
    args = parser.parse_args()

    for i in args.input:
        print(i.strip())
        print('*')
