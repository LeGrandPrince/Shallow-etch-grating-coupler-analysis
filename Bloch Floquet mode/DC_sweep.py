import numpy as np
import matplotlib.pyplot as plt
#Results of DC sweep 

def directionality(Dir = 'Up', Pup = 0, Pdown = 0):

    DC = np.arange(0.1,0.96,0.05)

    if Dir == 'Up':
        D = Pup/(Pdown + Pup)
    elif Dir == 'Down':
        D = Pdown/(Pdown + Pup)
    else:
        'DIRECTIONALITY: Wrong input parameter. Specify as Dir = "Up" or Dir = "Down"'
    
    #Plot the results in %
    plt.figure()

    plt.plot(DC, D*100, marker='^', linewidth = 2)

    plt.xlabel('Duty cycle [-]')
    plt.ylabel('Directionality [%]')

    plt.title('Directionality for TE mode' )
    plt.show()

    return D
    



def scatteringEff(Pin, Lr, Lt):
    
    DC = np.arange(0.1,0.96,0.05)
    SE = (Pin  - Lt - Lr)/Pin
    #Plot the results in %

    plt.figure()

    plt.plot(DC, SE*100, marker='^', linewidth = 2)

    plt.xlabel('Duty cycle [-]')
    plt.ylabel('Scattering efficiency [%]')
    plt.show()

    return SE
    


def couplingEff(D, SE, O):

    CE = SE*D*O

    #Plot the results in %
    plt.figure()

    plt.plot(DC, CE*100, marker='^', linewidth = 2, color =  'blue')

    plt.xlabel('Duty cycle [-]')
    plt.ylabel('Coupling efficiency [%]')
    plt.axhline(50, linestyle = '--', color = 'black', label = '50% threshold')
    plt.legend()
    plt.show()
    return CE


Reflection = {
            'TE_1310':np.array([0.0920, 0.1525, 0.2172, 0.2203, 0.2082, 0.1818, 0.2092, 0.2061, 0.1460, 0.0613, 0.0286, 0.0299, 0.0243, 0.0251, 0.0240, 0.0606, 0.0094, 0.0121]),
            'TM_1310':np.array([0.1035, 0.1258, 0.0068, 0.0459, 0.0229, 0.4109, 0.3859, 0.1312, 0.0724, 0.0771, 0.0456, 0.0658, 0.1559, 0.2091, 0.1889, 0.1312, 0.0730, 0.0290])
            }

Transmission = {
            'TE_1310':np.array([0.0796, 0.0021, 0.0018, 0.0018, 0.0063, 0.0121, 0.0034, 0.0020, 0.0336, 0.1449, 0.0769, 0.0186, 0.01, 0.0055, 0.0164, 0.1791, 0.4855, 0.6115]),
            'TM_1310':np.array([0.7403, 0.7668, 0.7217, 0.6738, 0.6824, 0.3570, 0.3037, 0.3522, 0.4606, 0.4967, 0.4202, 0.3299, 0.3023, 0.2841, 0.2811, 0.3346, 0.4598, 0.6737])
            }

Power_up = {
            'TE_1310':np.array([0.219, 0.268, 0.2577, 0.2596, 0.295, 0.2902, 0.2672, 0.2573, 0.2167, 0.1267, 0.1715, 0.2022, 0.2209, 0.2475, 0.2828, 0.2093, 0.0931, 0.0482]),
            'TM_1310':np.array([0.0843, 0.0750, 0.0785, 0.0905, 0.1296, 0.1191, 0.1014, 0.1487, 0.2142, 0.2492, 0.2721, 0.2777, 0.2628, 0.2545, 0.2662, 0.2717, 0.2351, 0.1401])
    }

Power_down = {
            'TE_1310':np.array([0.565, 0.5615, 0.5097, 0.5, 0.5157, 0.5248, 0.5054, 0.5126, 0.5729, 0.6546, 0.7241, 0.7260, 0.7204, 0.6949, 0.6631, 0.511, 0.2877, 0.1076]),
            'TM_1310':np.array([0.0950, 0.0961, 0.0965, 0.1095, 0.1522, 0.1299, 0.1081, 0.1527, 0.2203, 0.2490, 0.2710, 0.2784, 0.2742, 0.2682, 0.2666, 0.2536, 0.2134, 0.1320])
    }

Field_overlap = {
            'TE_1310':np.array([0.5428, 0.7111, 0.8706, 0.8739, 0.7991, 0.7623, 0.8042, 0.7733, 0.6209, 0.5411, 0.6397, 0.7078, 0.7112, 0.6229, 0.5950, 0.4795, 0.4010, 0.2558]),
            'TM_1310':np.array([0.0925, 0.0968, 0.1259, 0.1449, 0.1469, 0.4921, 0.4912, 0.4871, 0.4064, 0.3009, 0.4796, 0.2882, 0.3347, 0.3952, 0.4168, 0.4097, 0.3732, 0.3127])
    }

DC = np.arange(0.1,0.96,0.05)

#Calculate Directionality and Scattering for TE mode efficiency in %
SE_TE = scatteringEff (1, Reflection['TE_1310'], Transmission['TE_1310'])
D_TE = directionality('Down' ,Power_up['TE_1310'], Power_down['TE_1310'])

#Calculate coupling efficiency in %
Coupling_efficiency_TE = couplingEff(D_TE, SE_TE, Field_overlap['TE_1310'])

SE_TM = scatteringEff(1, Reflection['TM_1310'], Transmission['TM_1310'])
D_TM = directionality('Down' ,Power_up['TM_1310'], Power_down['TM_1310'])
Coupling_efficiency_TM = couplingEff(D_TM, SE_TM, Field_overlap['TM_1310'])



#Store the results as dict
TE_1310 = {'DC':DC,
           'Scattering_efficiency':SE_TE*100,
           'Directionality':D_TE*100,
           'Field_overlap':Field_overlap['TE_1310']*100,
           'Coupling_efficiency':Coupling_efficiency_TE*100}

TM_1310 = {'DC':DC,
           'Scattering_efficiency':SE_TM*100,
           'Directionality':D_TM*100,
           'Field_overlap':Field_overlap['TM_1310']*100,
           'Coupling_efficiency':Coupling_efficiency_TM*100}

#Import pandas package 
import pandas as pd

#Create a Dataframe from the results
Grating_efficiency_TE = pd.DataFrame(TE_1310)
Grating_efficiency_TM = pd.DataFrame(TM_1310)
print(Grating_efficiency_TE.to_string())
print(Grating_efficiency_TM.to_string())

plt.figure()
plt.plot(DC, Grating_efficiency_TE['Coupling_efficiency'], marker='^', linewidth = 2, color = 'blue', label = 'TE')
plt.plot(DC, Grating_efficiency_TM['Coupling_efficiency'],  marker='^', linewidth = 2, color = 'red', label = 'TM')
plt.axhline(50, linestyle = '--', color = 'black',label = '50% threshold')
plt.xlabel('Duty cycle')
plt.ylabel('Coupling efficiency [dB]')
plt.legend()
plt.show()



