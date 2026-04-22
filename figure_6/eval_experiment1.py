#!/usr/bin/env python3

import subprocess
import shutil
from os import listdir, makedirs

# From https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters
# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '#', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def main():
    # This script calls all the scripts we used in our workflow in the correct order
    # on the correct raw data to generate the figures

    raw_data_1 = listdir("raw_data_experiment_1")

    # Process raw data of experiment 1
    makedirs("processed_fig6", exist_ok=True)
    l = len(raw_data_1)
    printProgressBar(0, l, prefix = 'Processing raw data exp1:', suffix = 'Complete', length = 50)
    for i, f in enumerate(raw_data_1):
        subprocess.run(["./n-party-presence.py", "raw_data_experiment_1/" + f, "processed_fig6"], stdout=subprocess.DEVNULL) 
        printProgressBar(i + 1, l, prefix = f'Processing {f}:', suffix = 'Complete', length = 50)

    # Process data of experiment 1 into figure 6
    processed_data_1 = listdir("processed_fig6")
    subprocess.run(["./n-party-presence-plotter.py"] + ['BOX', 'ignored'] + [f"processed_fig6/{f}" for f in processed_data_1]) 

    # Build figure using latex
    makedirs("latex", exist_ok=True)
    subprocess.run(['pdflatex', '-output-directory', 'latex', 'figure6.tex']) 
    shutil.copyfile('latex/figure6.pdf', 'figure6.pdf')
    subprocess.Popen(['atril', 'figure6.pdf'])



if __name__ == "__main__":
	main()

