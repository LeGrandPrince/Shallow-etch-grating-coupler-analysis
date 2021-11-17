DISCLAIMER: Some of the scripts methods results are possible to obtain from proffesional software (like field overlap). Freeware versions of the scripts show problems using these tools, so scripts are designed to address these issues.

# Diffraction grating analysis

Repository, up to date, consists of two python scripts. 

First, the Bloch-Floquet-mode finds Bloch-Floquet refractive indices and calculates diffraction mode regions for various DC. 

Second - sweep calculates Scattering efficiency of grating, its Directionality and Coupling efficiency. Field overlap, up to date, has to be provided externally. 

Coming next will be script

# Use of the Bloch_Floquet_mode.py script

DISCLAIMER: This script is designed to calculate nb only for SHALLOW ETCH GRATING COUPLER. 

use blochFloquetIndex function to calculate effective bloch-floquet indices. Result is stored as Pandas DF.

use diffractionRegion function to find region where grating coupler is in the diffraction mode. n_bfm argument should be pandas dataframe generated by blochFloquetIndex function.

Both functions output pandas DF's, which you can then easily copy from command line and with few steps paste into excel to make neat worksheets. For this purpose, author suggests labeling the data not in this way:{'Label one':data,\n
                                   'Label two':data,\n
                                   ...\n
                                   }\n
\n                                                                                 
but in this way: {'Label_one':data,\n
                  'Label_two':data,\n
                  ...\n
                 }\n
\n                                
This way, excel will divide the data to columns the correct way. If you use spaces in labeling instead of underscoring, make sure to mark the labels in a distinct way.

# Use of the sweep.py script
Script consists of 4 functions and is written to calculate coupling efficiency of any given grating coupler. Script, however expects simulation data to be written by hand. Extracted CSV file will also work. 

Function plotRawData doesn't calculate anything, just plots the simulation data. 

Function scaterringEff calculates scattering efficiency and plots it in one graph with return loss and transmission loss.

Function directionality calculates directionality and plots it in one graph with upward and downward radiated powers. 

Function couplingEff calculates coupling efficiency and plots it in one graph with scattering efficiency, directionality and overlap integral. Overlap is part of the raw data. 

When you call each function, you can specify x axis data, label and units. 

