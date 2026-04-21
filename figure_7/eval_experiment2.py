#!/usr/bin/env python3

import subprocess
import shutil
from os import listdir

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

    raw_data_2 = listdir("raw_data_experiment_2")

    # Process raw data of experiment 2
    l = len(raw_data_2)
    printProgressBar(0, l, prefix = 'Processing raw data exp2:', suffix = 'Complete', length = 50)
    for i, f in enumerate(raw_data_2):
        subprocess.run(["./n-party-presence.py", "raw_data_experiment_2/" + f, "processed_fig7"], stdout=subprocess.DEVNULL) 
        printProgressBar(i + 1, l, prefix = f'Processing {f}:', suffix = 'Complete', length = 50)

    # Get cutoff at 10meters
    cutoff = float(subprocess.check_output(["./n-party-presence.py", "raw_data_experiment_2/npp-2026-02-18_15-23-58_v2_10m.log", "processed_fig7"]))
    print(f"cutoff (10m): {cutoff}")

    processed_data_2 = listdir("processed_fig7")
    subprocess.run(["./n-party-presence-ugly-plotter.py"] + ['BAR', f'{cutoff}'] + [f"processed_fig7/{f}" for f in processed_data_2]) 

    # Build figure using latex
    subprocess.run(['pdflatex', '-output-directory', 'latex', 'figure7.tex']) 
    shutil.copyfile('latex/figure7.pdf', 'figure7.pdf')
    subprocess.Popen(['atril', 'figure7.pdf'])



if __name__ == "__main__":
	main()

