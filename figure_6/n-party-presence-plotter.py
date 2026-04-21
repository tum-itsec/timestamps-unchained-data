#!/usr/bin/env python3

from sys import argv
import time
import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import re
import statistics
import math
import csv

# CUTOFF = 11.983734351568238

def correction(y):
    # loms, 30, 10%, calibrated 1st:
    #return 0.833 * y - 0.802

    # loms, 30, 10%, calibrated 1st+2nd
    #return 0.813 * y - 0.216

    return y

def main():
    if len(argv) < 4:
        print(f"Usage: {argv[0]} <BOX/BAR> <CUTOFF (only relevant for BAR)> <eval_file_1> [<eval_file_2>...<eval_file_n>]")
        return

    evalfiles = argv[3:]

    if argv[1] == 'BOX':
        CSV_BAR = False
        CSV_BOX = True
    elif argv[1] == 'BAR':
        CSV_BAR = True
        CSV_BOX = False
        CUTOFF = float(argv[2])
    else:
        raise Exception

    with open('figure6.csv' if CSV_BOX else 'figure7.csv', 'w+', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        if CSV_BOX:
            spamwriter.writerow(['x', 'lw', 'lq', 'med', 'uq', 'uw'])
        if CSV_BAR:
            spamwriter.writerow(['distance', 'acceptance'])
        summary_xs1 = []
        summary_ys1 = []
        summary_xs2 = []
        summary_ys2 = []
        box_vals1 = []
        box_vals2 = []
        
        for file in evalfiles:
            with open(file) as f:
                f.readline()
                ys_uncorr = list(map(float, f.readline().split(",")))
                xs = range(len(ys_uncorr))
            ys = list(map(correction, ys_uncorr))
            match = re.match(".*/npp-.*?_(v2_)?([0-9.]+)m.log.eval", file)
            if not match:
                col = (1, 0, 0)
                d = -1
                is_v2 = False
            else:
                d = float(match.group(2))
                is_v2 = bool(match.group(1))
                if is_v2:
                    dmin = 9
                    dmax = 11
                    col = lambda f: (0 if d != 10 else 1, f, 0)
                else:
                    dmin = 5
                    dmax = 15
                    col = lambda f: (0 if d != 10 else 1, f, 1)
                col = col(math.sqrt((d - dmin) / (dmax - dmin)))


            if CSV_BOX:
                if not is_v2:
                    row = []
                    row.append(d)
                    row.append(min(ys))
                    row += statistics.quantiles(ys, n=4)
                    row.append(max(ys))
                    spamwriter.writerow(row)
            elif CSV_BAR:
                ar = sum([1 if y < CUTOFF else 0 for y in ys]) / len(ys)
                if is_v2:
                    row = [d, ar]
                    spamwriter.writerow(row)
            else:
                raise Exception

if __name__ == "__main__":
	main()
