README for reproducibility submission of paper ID #95

A) Source code info
Repository: https://github.com/tum-itsec/timestamps-unchained-data
List of Programming Languages: python, latex
Compiler Info: python 3.13.12, pdftex 3.141592653-2.6-1.40.29
Packages/Libraries Needed: matplotlib, atril, texlive-latex-base texlive-latex-recommended texlive-pictures texlive-latex-extra

B) Datasets info
Repository: https://github.com/tum-itsec/timestamps-unchained-data
Data generators: https://github.com/tum-itsec/timestamps-unchained

C) Hardware Info
(These are not strict requirements; just the machine we tested this VM on. Shouldn't really matter as our work is not very resource-intensive.)
C1) CPU: x86_64 Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz
C2) Caches:
	L1d:                       128 KiB (4 instances)
	L1i:                       128 KiB (4 instances)
	L2:                        1 MiB (4 instances)
	L3:                        8 MiB (1 instance)
C3) Memory: 8GB DDR3
C4) Storage: Secondary Storage SSD (min 20Gb)
C7) Additional hardware: ESP32-C3 (if data collection is desired)

D) Experimentation Info

NOTE: In the VM we provide the data that was collected during the experimentation phase described in the paper.
The scripts in the VM demonstrate how this raw data is evaluated to results that are then automatically plotted into the 
figures contained in our work.

Should you wish to recreate our physical experiments we also provide access to the source code that needs to be flashed on the 
target platform (ESP32-C3) [see B) Data generators].

Evaluation machine:
For artifact evaluation purposes, we also provide SSH access to a remote machine with phyiscal ESP32-C3 boards connected.
Credentials for this physical machine can be found inside the VM (just do `ssh timestampsunchained-eval`) and also have been provided to artifact evaluaters.
To ensure your privacy, you can of course use a VPN to connect.

D1) VM Credentials: wisec (pwd: 1234567), root (pwd: 1234567)
D2) Figure 6: enter /home/wisec/figure6 and run ./eval_experiment1.py -> raw data (contained in subdirectory) is processed in two stages to figure6.csv and then plotted into figure6.pdf
D2) Figure 7: enter /home/wisec/figure7 and run ./eval_experiment2.py -> raw data (contained in subdirectory) is processed in two stages to figure7.csv and then plotted into figure7.pdf
You may clean the directory by executing clean.sh

E) Software License: MIT 
