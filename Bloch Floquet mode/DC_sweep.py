import numpy as np
import matplotlib.pyplot as plt
#Results of DC sweep 

def directionality(Dir = 'Up', Pup = 0, Pdown = 0, xline = 0, xline_axis = "",  axis_units = "", graph_title = "Directionality"):
    '''
    Calculates the directionality as a numpy array. \n

    Dir: STRING. Specifies the direction. Must be Either "Up" or "Down".\n

    Pup: ARRAY. Power radiated to the fiber or towards the cladding obtained from simulations. 
    Default value is 0. Can be of any type as long as it satisfies matplotlib.pyplot.\n

    Pdown: Power radiated to the substrate obtained from simulations. 
    Default value is 0. Can be of any type as long as it satisfies matplotlib.pyplot.\n

    xline: ARRAY of values for x axis. Obligatory argument. Can be of any type as long as it satisfies matplotlib.pyplot.\n 

    xline_axis: STRING. Title of the x axis. Default value is an empty string.\n

    axis_units: STRING. Units to be displayed after axis title. Default value is an empty string.\n

    graph_title: STRING. Default value is "Directionality".
    '''
    
    #Calculations of directionalities themselves
    if Dir == 'Up':
        D = Pup/(Pdown + Pup)
    elif Dir == 'Down':
        D = Pdown/(Pdown + Pup)
    else:
        'DIRECTIONALITY: Wrong input parameter. Specify as Dir = "Up" or Dir = "Down"'
    
    #Plot the results in %
    plt.figure()
    plt.plot(xline, D*100, marker='^', linewidth = 2)

    #Set the axes
    plt.xlabel(xline_axis + " [" + axis_units + "]")
    plt.ylabel('Directionality [%]')

    #Set the title
    plt.title(graph_title)
    plt.show()

    #Return the results
    return D
    



def scatteringEff(Pin = 0, Lr = 0, Lt =  0, xline = 0, xline_axis = "", axis_units = "", graph_title = "Scattering efficiency"):
    '''
    Calculates the scattering efficiency as a numpy array. \n

    Pin: Input power as selected for simulations. 
    Can be any type as long as it satisfies the equations below.\n

    Lr: ARRAY. Reflected power/reflection loss obtained from simulations. 
    Default value is 0. Can be of any type as long as it satisfies matplotlib.pyplot.\n

    Lt: ARRAY. Power transmitted/transmission loss obtained from simulations.
    Can be of any type as long as it satisfies matplotlib.pyplot. Default value is 0. 
    Can be of any type as long as it satisfies matplotlib.pyplot.\n

    xline: ARRAY of values for x axis. Obligatory argument. Can be of any type as long as it satisfies matplotlib.pyplot.\n 

    xline_axis: STRING. Title of the x axis. Default value is an empty string.\n

    axis_units: STRING. Units to be displayed after axis title. Default value is an empty string.\n

    graph_title: STRING. Default value is "Directionality".
    '''

    #Calculation of scattering efficiency itself
    SE = (Pin  - Lt - Lr)/Pin
    
    #Plot the results in %
    plt.figure()
    plt.plot(xline, SE*100, marker='^', linewidth = 2)

    #Set the title
    plt.title(graph_title)

    #Set the axes
    plt.xlabel(xline_axis + " [" + axis_units + "]")
    plt.ylabel('Scattering efficiency [%]')

    plt.show()

    #Return the result
    return SE
    


def couplingEff(D, SE, O, xline = 0, xline_axis = "", axis_units = "", graph_title = "Coupling efficiency"):
    '''
    Calculates the couplingg efficiency as a numpy array. \n

    D: ARRAY. Directionality. Can be obtained from directionality method. 
    Can be any type as long as it satisfies the equation below.\n

    SE: ARRAY. Scattering efficiency. Can be obtained from scatteringEff method. 
    Can be any type as long as it satisfies the equation below.\n

    O: ARRAY. Overlap integral. Obtained from simulations.  
    Can be any type as long as it satisfies the equation below.\n

    xline: ARRAY of values for x axis. Obligatory argument. Can be of any type as long as it satisfies matplotlib.pyplot.\n 

    xline_axis: STRING. Title of the x axis. Default value is an empty string.\n

    axis_units: STRING. Units to be displayed after axis title. Default value is an empty string.\n

    graph_title: STRING. Default value is "Directionality".
    '''

    #Calculation of coupling efficiency itself
    CE = SE*D*O

    #Plot the results in %
    plt.figure()
    plt.plot(xline, CE*100, marker='^', linewidth = 2, color =  'blue')
    
    #Set the title
    plt.title(graph_title)

    #Set the axes
    plt.xlabel(xline_axis + " [" + axis_units + "]")
    plt.ylabel('Coupling efficiency [%]')

    #Plot the threshold line
    plt.axhline(50, linestyle = '--', color = 'black', label = '50% threshold')
    
    #Display the legend and show
    plt.legend()
    plt.show()
    
    #Return the results
    return CE


#Raw data from simulations. Get overlap from matlab. 
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




#Raw data
Single_etch = {
'wavelength':np.arange(1.27,1.35, 0.01),
'R':np.array([0.0839, 0.0726, 0.2107, 0.0827, 0.0547, 0.1022, 0.0709, 0.0400, 0.0798]),
'T':np.array([0.0050, 0.0080, 0.0026, 0.0095, 0.0093, 0.1258, 0.0110, 0.0132, 0.0119]),
'Up':np.array([0.5453, 0.5647, 0.5206, 0.6269, 0.6769, 0.6552, 0.6441, 0.6857, 0.6446]),
'Down':np.array([0.3289, 0.3173, 0.2347, 0.2456, 0.2402, 0.2085, 0.2442, 0.2308, 0.2355]),
'Overlap':np.array([0.8409, 0.7898, 0.8869, 0.8149, 0.8038, 0.8100, 0.77420, 0.7690, 0.7316])
}


#Calculate scattering efficiency and specify wavelength as an argument for x axis.
single_SE = scatteringEff(1,Single_etch['R'], Single_etch['T'], Single_etch['wavelength'], "Wavelength", "nm")

#Calculate directionality and specify wavelength as an argument for x axis.
single_Dir = directionality('Up', Single_etch['Up'], Single_etch['Down'], Single_etch['wavelength'], "Wavelength", "nm")

#Calculate coupling efficiency and specify wavelength as an argument for x axis.
single_CE = couplingEff(single_Dir, single_SE, Single_etch['Overlap'], Single_etch['wavelength'], "Wavelength", "nm")



#Plot the coupling efficiency in log scale
plt.figure()
plt.plot(Single_etch['wavelength'], 10*np.log10(single_CE), marker='^', linewidth = 2, color =  'blue')
plt.xlabel('Wavelength [nm]')
plt.ylabel('Coupling efficiency [dB]')
plt.axhline(-1, linestyle = '--', color = 'black', label = '-1dB threshold')
plt.legend()
plt.show()
