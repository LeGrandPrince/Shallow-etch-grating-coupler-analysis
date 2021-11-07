import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def rawDataPlot(T, R, U, D, xline, xline_axis = '', axis_units = '', graph_title = ''):
    '''
    Plots the raw data: Transmission loss, Return loss, upward power and downward power.\n
    Make sure that dimensions match and follow same rules as for matplotlib.pyplot.\n

    T: ARRAY. Transmission loss.\n
    R: ARRAY. Return loss.\n 
    U: ARRAY. Upward power.\n 
    D: ARRAY. Downward power.\n
    '''
    
    #Plot respective arrays in [%], label them and assing colors. 
    #Use xline argument as x axis. 
    plt.plot(xline, T*100, label = 'Transmission loss', color = 'Cyan')
    plt.plot(xline, R*100, label = 'Return loss', color = 'Magenta')
    plt.plot(xline, U*100, label = 'Upward power', color = 'Yellow')
    plt.plot(xline, D*100, label = 'Downward power', color = 'Black')
    
    #Use xline_axis and axis_units arguments to label x axis
    plt.xlabel(xline_axis + ' [' + axis_units + ']')

    #Set Y axis and display legend.
    plt.ylabel('%')
    plt.legend()

    #Use graph_title argument to specify graph title
    plt.title(graph_title)
    plt.show()

    


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
    plt.plot(xline, D*100, marker='^', linewidth = 2, color = 'blue', label = 'Directionality')

    #Plot Power up and power down for better troubleshooting
    plt.plot(xline, Pup*100, color = 'cyan', label = 'Power up')
    plt.plot(xline, Pdown*100, color = 'magenta', label = 'Power down')
    
    #Set the axes
    plt.xlabel(xline_axis + " [" + axis_units + "]")
    plt.ylabel('Directionality [%]')

    #Set the title and legend
    plt.title(graph_title)
    plt.legend()
    plt.show()

    #Return the results
    return D
    



def scatteringEff(Pin = 0, Lr = 0, Lt =  0, xline = 0, xline_axis = "", axis_units = "", graph_title = "Scattering efficiency"):
    '''
    Calculates the scattering efficiency as a numpy array. \n

    Pin: Input power as selected for simulations. Default value is 1
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
    plt.plot(xline, SE*100, marker='^', linewidth = 2, color = 'blue', label = 'Scattering efficiency')

    #Plot return and transmission loss for better troubleshooting
    plt.plot(xline, Lr*100, color = 'cyan', label = 'Return loss')
    plt.plot(xline, Lt*100, color = 'magenta', label = 'Transmission loss')
    #Set the title
    plt.title(graph_title)

    #Set the axes 
    plt.xlabel(xline_axis + " [" + axis_units + "]")
    plt.ylabel('Scattering efficiency [%]')

    plt.legend()
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

    #Plot scattering efficiency as well as directionality for better troubleshooting
    plt.plot(xline, SE*100, color = 'cyan', label = 'Scattering efficiency')
    plt.plot(xline, D*100, color = 'magenta', label = 'Directionality')
    plt.plot(xline, O*100, color = 'yellow', label = 'Field overlap')

    #Set the title
    plt.title(graph_title)

    #Set the axes
    plt.xlabel(xline_axis + " [" + axis_units + "]")
    plt.ylabel('Coupling efficiency [%]')

    #Plot the threshold line
    plt.axhline(79, linestyle = '--', color = 'black', label = '50% threshold')
    
    #Display the legend and show
    plt.legend()
    plt.show()
    
    #Return the results
    return CE


#Shallow etch (Hw = 180nm, Hs = Hw/2) DC sweep on 1000nm raw data. Overlap from matlab. Cladding SiO2.
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


#Shallow etch (Hw = 180nm, Hs = Hw/2) period sweep in region <0.41;0.65>nm raw data. Overlap from matlab. Cladding SiO2.

Period = np.arange(0.41,0.66,0.02)

R = {'TE':np.array([0.1087, 0.0781, 0.0403, 0.0293, 0.0358, 0.0208, 0.3232, 0.0178, 0.0156, 0.0084, 0.0245, 0.0160, 0.0087]),
     'TM':np.array([0.7340, 0.3265, 0.3123, 0.1928, 0.0896, 0.0484, 0.0565, 0.0317, 0.0531, 0.0189, 0.0603, 0.0114, 0.0543])}

T={'TE':np.array([0.0247, 0.0184, 0.0524, 0.0725, 0.0694, 0.0624, 0.0650, 0.0374, 0.0309, 0.0388, 0.0337, 0.0302, 0.0254]),
   'TM':np.array([0.3186, 0.5902, 0.3701, 0.4355, 0.4740, 0.5081, 0.5909, 0.5701, 0.4836, 0.4496, 0.4664, 0.5119, 0.5249])}

Pu = {'TE':np.array([0.2330,  0.2016, 0.1418, 0.1413, 0.1657, 0.1881, 0.1095, 0.2025, 0.1919, 0.1755, 0.1567, 0.1469, 0.1470]),
      'TM':np.array([0.0274, 0.0397, 0.1346, 0.1845, 0.1921, 0.2110, 0.1337, 0.1123, 0.1507, 0.1731, 0.1525, 0.1228, 0.1007])}

Pd = {'TE':np.array([0.6232, 0.6811, 0.7273, 0.7118, 0.6767, 0.6748, 0.3671, 0.7018, 0.7198, 0.7320, 0.7391, 0.7632, 0.7726]),
      'TM':np.array([0.0827, 0.1254, 0.2554, 0.2845, 0.3169, 0.2966, 0.2961, 0.3522, 0.3899, 0.4123, 0.3977, 0.4005, 0.3953]
)}

FO = {'TE':np.array([0.9182, 0.9112, 0.7828, 0.6798, 0.6547, 0.6547, 0.5478, 0.6977, 0.6752, 0.6540, 0.6528, 0.6519, 0.6660]), 
     'TM':np.array([0.8315, 0.7551, 0.8378, 0.7944, 0.6908, 0.7219, 0.6900, 0.6202, 0.6764, 0.5893, 0.6098, 0.6034, 0.5914])
}


#Plot Transmission loss, return loss, up power and down power
rawDataPlot(R['TE'], T['TE'], Pu['TE'], Pd['TE'], Period*1000, 'Period', 'nm')

#Calculate scattering efficiency and plot scattering efficiency, return loss and transmission loss vs period.
SE = scatteringEff(1, R['TE'], T['TE'], Period*1000, 'Period', 'nm')

#Calculate directionality. Plot directionality with up power and down power vs. period
D = directionality('Down', Pu['TE'], Pd['TE'], Period*1000, 'Period', 'nm')

#Calculate coupling efficiency. Plot coupling efficiency with scattering efficiency, directionality and 
#field overlap vs. period. 
CE = couplingEff(D, SE, FO['TE'], Period*1000, 'Period', 'nm')







