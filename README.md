# Diffraction grating analysis

Repository, up to date, consists of two python scripts. 

First, the Bloch-Floquet-mode finds Bloch-Floquet refractive indices and calculates diffraction mode regions for various DC. 

Second - sweep calculates Scattering efficiency of grating, its Directionality and Coupling efficiency. Field overlap, up to date, has to be provided externally. 

# Use of the Bloch-Floquet mode script

DISCLAIMER: This script is designed to calculate nb only for SHALLOW ETCH GRATING COUPLER. 

use blochFloquetIndex to calculate effective bloch-floquet indices. Result is stored as Pandas DF.

use diffractionRegion function to find region where grating coupler is in the diffraction mode. n_bfm argument should be pandas dataframe. 
