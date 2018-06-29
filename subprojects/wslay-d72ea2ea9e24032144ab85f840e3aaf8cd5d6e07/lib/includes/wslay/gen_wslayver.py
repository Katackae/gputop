#!/usr/bin/env python2

import argparse
import textwrap

from mako.template import Template

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='Where to read the input file.',
                        required=True)
    parser.add_argument('--output', help='Where to write the output file.',
                        required=True)
    parser.add_argument('--variable', help='Variable to replace',
                        action='append', required=True)
    args = parser.parse_args()

    with open(args.input, "rt") as fin:
        with open(args.output, "wt") as fout:
            for line in fin:
                for v in args.variable:
                    kv = v.split('=')
                    fout.write(line.replace("@%s@" % kv[0], kv[1]))


if __name__ == '__main__':
    main()
