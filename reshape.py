#!/usr/bin/env python2
import argparse
import sys
import matplotlib.pyplot as plt
import numpy as np

def main(args):
    lines = [ i.strip().split(" ") for i in open(args.inp, 'r').readlines()]
    table = {}
    inputfiles = set()
    for i in lines:
        date = i[0]
        inputfile = i[1]
        crashy = i[2]
        row = {}
        if table.has_key(date):
            row = table[date]
        row[inputfile] = crashy
        table[date] = row
        inputfiles.add(inputfile)

    dates = table.keys()
    dates.sort()
    mat = []
    for f in inputfiles:
        row = []
        for d in dates:
            r = table.get(d)
            row.append(float(r.get(f, 0)))
        mat.append(row)
  
    npa = np.array(mat)
    plt.imshow(npa, cmap='hot', interpolation='nearest')
    plt.show()
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser('reshaper')
    parser.add_argument('inp')
    args = parser.parse_args()
    sys.exit(main(args))
