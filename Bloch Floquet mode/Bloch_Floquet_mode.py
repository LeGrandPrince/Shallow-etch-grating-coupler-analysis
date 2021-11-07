import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def blochFloquetIndex(n_tooth, n_slab, duty_cycle):
    '''
    
    Outputs Bloch-Floquet mode as pandas DF for TM/TE modes.\n
    n_tooth: refractive index of unetched region\n
    n_slab: refractive index of etched region\n
    REMARK: both effective indices shall be specified as dicts with TE and TM keys. 
    
    '''
   
    #calculate the BF mode index for TE/TM and sotre it as a dict
    nb = {
          'TE':n_tooth['TE'] * duty_cycle + n_slab['TE'] * (1-duty_cycle),
          'TM':n_tooth['TM'] * duty_cycle + n_slab['TM'] * (1-duty_cycle),
          'DC':duty_cycle
         }
    
    #store the BF mode in pandas dataframe and print it out
    Bloch_Floquet = pd.DataFrame(nb)
    return Bloch_Floquet
    


def diffractionRegion(wavelength, n_bfm, n_cladd):
    '''

    Outputs the period for which grating behaves as diffraction medium.

    wavelength: operating wavelength. MUST BE SAME AS WAVELENGTH YOU USED TO CALCULATE EFFECTIVE REFRACTIVE INDICES!\n
    n_bfm: pandas DataFrame for Bloch-Floquet refractive index. CALCULATE USING blochFloquetIndex FUNCTION!\n
    n_cladd: refractive index of grating coupler cladding.
    
    '''

    #Store Bloch-Floquet modes for TE/TM and respective DC's 
    duty_cycle = n_bfm.loc[:, 'DC']
    TE = n_bfm.loc[:, 'TE']
    TM = n_bfm.loc[:, 'TM']
    print(TE, TM)
    #Calculate region boundaries for TE polarization   
    TE_pitch_min = wavelength / (TE + n_cladd)
    TE_pitch_max = np.minimum((- wavelength / (n_cladd - TE)),(2*wavelength / (n_cladd + TE)))

    #Calculate region boundaries for TM polarization
    TM_pitch_min = wavelength / (TM + n_cladd)
    TM_pitch_max = np.minimum(- wavelength / (n_cladd - TM),(2*wavelength / (n_cladd + TM)))

    #Store the results in dictionary
    DR = {'TE_min': TE_pitch_min,
          'TE_max': TE_pitch_max,
          'TM_min': TM_pitch_min,
          'TM_max': TM_pitch_max,
          'DC': duty_cycle}

    #Create a DataFrame from dictionary and return it
    diffractionRegion = pd.DataFrame(DR)
    return diffractionRegion


#Define parameters
DC = np.arange(0.1,0.95,0.05)
neff_tooth = {'TE':2.85259568, 'TM':2.01981205}
neff_slab = {'TE':2.26512399, 'TM':1.51336215}
n_cladding = 1.444
wavelength = 1310

#Call function to calculate Bloch-Floquet mode
Bloch_Floquet = blochFloquetIndex(neff_tooth, neff_slab, DC)
print(Bloch_Floquet)
#Call function to calculate upper and lower boundaries of period for diffraction mode
pitchRegion = diffractionRegion(wavelength, Bloch_Floquet, n_cladding)
print(pitchRegion)

#Plot the results
plt.figure()

#Plot the lower boundary
plt.plot(pitchRegion.loc[:, 'DC'], pitchRegion.loc[:, 'TE_min'], 'blue', label = 'TE Lower boundary', marker =  'v' )

#Plot the upper boundary
plt.plot(pitchRegion.loc[:, 'DC'], pitchRegion.loc[:, 'TE_max'], 'red', label = 'TE Upper boundary', marker = '^' )

#Plot the lower boundary
plt.plot(pitchRegion.loc[:, 'DC'], pitchRegion.loc[:, 'TM_min'], 'green', label = 'TM Lower boundary', marker =  'v' )

#Plot the upper boundary
plt.plot(pitchRegion.loc[:, 'DC'], pitchRegion.loc[:, 'TM_max'], 'magenta', label = 'TM Upper boundary', marker = '^' )

#Set the labels
plt.xlabel('Duty cycle [-]')
plt.ylabel('Period [nm]')

#Set the title
plt.title('Regions of period for grating coupler in the diffraction mode (TE)')

#Fill the region between two boundaries
plt.fill_between(pitchRegion.loc[:, 'DC'], 
                 pitchRegion.loc[:, 'TE_min'], 
                 pitchRegion.loc[:, 'TE_max'], 
                 label = 'Diffraction region', 
                 alpha = 0.3, 
                 facecolor = 'cyan')

#Set legend and show
plt.legend()
plt.show()


