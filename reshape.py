#!/usr/bin/env python2
import argparse
import datetime
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
import copy

def normalize(mat, M, N):
    umat = copy.deepcopy(mat)
    for i in range(0, M):
        s = 0
        flip = False
        for j in range(0, N):
            idx = (N-1)-j
            if flip == True:
                umat[i][idx] = 1
            else:
                v = umat[i][idx]
                s = s + v
                if s > 0:
                    flip = True
    return umat

def dump_to_csv(mat, M, N, dates, files):
    outfile = open('out3.csv', 'w')
    outfilewriter = csv.writer(outfile)
    header = ['file']
    for d in dates:
        t = datetime.datetime.fromtimestamp(float(d)).strftime('%Y-%m-%d %H:%M:%S')
        header.append(t)
    outfilewriter.writerow(header)
    for i in range(0, M):
        row = [files[i]]
        for j in range(0, N):
            row.append(str(mat[i][j]))
        outfilewriter.writerow(row)
    return

def main(args):
    lines = [ i.strip().split(" ") for i in open(args.inp, 'r').readlines()]
    table = {}
    inputfiles = set()
    inputfile_idx_to_file = {}
    for i in lines:
        if i[0] == "Time":
            continue
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
    f_idx = 0
    for f in inputfiles:
        row = []
        for d in dates:
            r = table.get(d)
            row.append(int(r.get(f, 0)))
        mat.append(row)
        inputfile_idx_to_file[f_idx] = f
        f_idx = f_idx + 1

    max_rows = len(inputfiles)
    max_cols = len(dates)
    nmat = normalize(mat, max_rows, max_cols)
    dump_to_csv(nmat, max_rows, max_cols, dates, inputfile_idx_to_file)
    mat = nmat
    prev_sum = None
    changes = {}
    sums = {}
    for x in range(0, max_cols):
        s = 0
        for y in range(0, max_rows):
            s = s + mat[y][x]
        sums[x] = s
    for d in sums:
        t = datetime.datetime.fromtimestamp(float(dates[d])).strftime('%Y-%m-%d %H:%M:%S')
        print "%s (%s) : %d crashing" % (t,dates[d],sums[d])
    for x in range(0, max_cols):
        s = 0
        changed_files = set()
        for y in range(0, max_rows):
            if x > 0:
                if mat[y][x-1] != mat[y][x]:
                    changed_files.add(inputfile_idx_to_file[y])
            s = s + mat[y][x]
        if prev_sum != None:
            if s != prev_sum:
                changes[x] = (changed_files,prev_sum > s)
                prev_sum = s 
        else:
            prev_sum = s

    # Also scan to see if anything regresses
    """
    regressions = set()
    for y in range(0, len(inputfiles)):
        row = mat[y]
        crashes = True
        regresses = False
        for c in row:
            if crashes:
                if c != 1:
                    crashes = False
            else:
                if c != 0:
                    regresses = True
                    break
        if regresses:
            regressions.add(inputfile_idx_to_file[y])

    if len(regressions) > 0:
        print "Regressions:"
        for r in regressions:
            print r
    """
    changes_keys = changes.keys()
    changes_keys.sort()
    for i in changes_keys:
        s = float(dates[i])
        fs,b = changes[i]
        t = datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S')
        print "At %s (%d), %d changes %s decrease" % (str(t), s, len(fs),str(b))
        #if len(changes[i]) < 10:
        #    for c in changes[i]:
        #        print c

    #print mat[0][480:500]
    #print mat[0][491:494]
    #print dates[492]
    print "|dates| == %d" % len(dates)
    print "|inputfiles| == %d" % len(inputfiles)
    #npa = np.array(mat)
    #plt.imshow(np.transpose(npa), cmap='hot', interpolation='nearest')
    #plt.savefig('plot.png')
    #for i in table[dates[-1]]:
    #    if table[dates[-1]][i] != "0":
    #        print i
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser('reshaper')
    parser.add_argument('inp')
    args = parser.parse_args()
    sys.exit(main(args))
