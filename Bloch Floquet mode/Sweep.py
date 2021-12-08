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
    Calculates the directionality as a numpy array and plots the data. \n

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
    Calculates the scattering efficiency as a numpy array and plto the data. \n

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
    Calculates the couplingg efficiency as a numpy array and plot the data \n

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
    plt.axhline(79, linestyle = '--', color = 'black', label = '79% threshold')
    
    #Display the legend and show
    plt.legend()
    plt.show()
    
    #Return the results
    return CE

'''
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


#Shallow etch (Hw = 180nm, Hs = Hw/2) period sweep in region <0.41;0.78>nm raw data. Overlap from matlab. Cladding SiO2.

Period = np.arange(0.37,0.8,0.02)

R = {'TE':np.array([0.3608, 0.2087, 0.1087, 0.0781, 0.0403, 0.0293, 0.0358, 0.0208, 0.3232, 0.0178, 0.0156, 0.0084, 0.0245, 0.0160, 0.0087, 0.01446, 0.0309,   0.0452,   0.0498,  0.0551,  0.1673, 0.5080]),
     'TM':np.array([0.7340, 0.3265, 0.3123, 0.1928, 0.0896, 0.0484, 0.0565, 0.0317, 0.0531, 0.0189, 0.0603, 0.0114, 0.0543])}

T={'TE':np.array([0.0605, 0.0919, 0.0247, 0.0184, 0.0524, 0.0725, 0.0694, 0.0624, 0.0650, 0.0374, 0.0309, 0.0388, 0.0337, 0.0302, 0.0254, 0.0209,  0.0100,  0.0033,  0.0005, 0.0006,  0.0011, 0.0005]),
   'TM':np.array([0.3186, 0.5902, 0.3701, 0.4355, 0.4740, 0.5081, 0.5909, 0.5701, 0.4836, 0.4496, 0.4664, 0.5119, 0.5249])}

Pu = {'TE':np.array([0.0772, 0.1130, 0.2330,  0.2016, 0.1418, 0.1413, 0.1657, 0.1881, 0.1095, 0.2025, 0.1919, 0.1755, 0.1567, 0.1469, 0.1470,  0.1653,   0.1886,   0.2426,  0.2441, 0.2583, 0.2110, 0.1134]),
      'TM':np.array([0.0274, 0.0397, 0.1346, 0.1845, 0.1921, 0.2110, 0.1337, 0.1123, 0.1507, 0.1731, 0.1525, 0.1228, 0.1007])}

Pd = {'TE':np.array([0.5323, 0.5823, 0.6232, 0.6811, 0.7273, 0.7118, 0.6767, 0.6748, 0.3671, 0.7018, 0.7198, 0.7320, 0.7391, 0.7632, 0.7726, 0.7630,  0.7319,   0.6938,  0.6202, 0.6416,  0.5704, 0.3369]),
      'TM':np.array([0.0827, 0.1254, 0.2554, 0.2845, 0.3169, 0.2966, 0.2961, 0.3522, 0.3899, 0.4123, 0.3977, 0.4005, 0.3953]
)}

FO = {'TE':np.array([0.9127, 0.7652, 0.9182, 0.9112, 0.7828, 0.6798, 0.6547, 0.6547, 0.5478, 0.6977, 0.6752, 0.6540, 0.6528, 0.6519, 0.6660, 0.7255, 0.7982, 0.8775, 0.8615, 0.8807, 0.8850, 0.8565]), 
     'TM':np.array([0.8315, 0.7551, 0.8378, 0.7944, 0.6908, 0.7219, 0.6900, 0.6202, 0.6764, 0.5893, 0.6098, 0.6034, 0.5914])
}


'''


DC = np.arange(0.45, 0.55, 0.01 )
print(DC)
Reflection = {'DC=0.3':np.array([0.6053, 0.8059, 0.2117, 0.0261, 0.0248, 0.0267, 0.0332, 0.1167, 0.0551, 0.0904, 0.0573]),
              'DC=0.45':np.array([0.1215, 0.0370, 0.0118, 0.0226, 0.0360, 0.0294, 0.0124, 0.0142, 0.0309, 0.0246, 0.0596]),
              'DC=0.6':np.array([0.0672, 0.0189, 0.0156, 0.0454, 0.0129, 0.0103, 0.0630, 0.0837, 0.0611, 0.0611, 0.0417]),
              'DC=0.75':np.array([0.0580, 0.1470, 0.0088, 0.0966, 0.0642, 0.1253, 0.1834, 0.0489, 0.1081, 0.0617, 0.6778]),
              'DC':np.array([0.0031, 0.0309, 0.0305, 0.0299, 0.0293, 0.0348, 0.0348, 0.0349, 0.0349, 0.0336, 0.0461]),
              'Sp':np.array([0.3080, 0.1466, 0.1394, 0.3327, 0.1584,  0.0241, 0.0348, 0.2127, 0.1155, 0.1404, 0.1043, ])
              }

Transmission = {'DC=0.3':np.array([0.0006, 0.0011, 0.1075, 0.2031, 0.1499, 0.1144, 0.0754, 0.0487, 0.0255, 0.0151, 0.0053]),
                'DC=0.45':np.array([0.0837, 0.0527, 0.0523, 0.0412, 0.0335, 0.0300, 0.0225, 0.0091, 0.0031, 0.0005, 0.0005]),
                'DC=0.6':np.array([0.0166, 0.3153, 0.0421, 0.0423, 0.0387, 0.0269, 0.0119, 0.0025, 0.0007, 0.0006, 0.0026]),
                'DC=0.75':np.array([0.1210, 0.0814, 0.1480, 0.1490, 0.1052, 0.0708, 0.0267, 0.0165, 0.0505, 0.0480, 0.0012]),
                'DC':np.array([0.0031, 0.0032, 0.0026, 0.0020, 0.0014, 0.0012, 0.0012, 0.0012, 0.0010, 0.0009, 0.0007]),
                'Sp':np.array([0.0013, 0.0011, 0.0017, 0.0013, 0.0011, 0.0014, 0.0016, 0.0021, 0.0014, 0.0021, 0.0028])}

Power_up = {'DC=0.3':np.array([0.0786, 0.0287, 0.0934,  0.1519, 0.1468, 0.1376, 0.1347, 0.1221, 0.1469, 0.1516, 0.1942]),
            'DC=0.45':np.array([0.1696, 0.1868, 0.1760, 0.1617, 0.1481, 0.1397, 0.1526, 0.1766, 0.2160, 0.2394, 0.2562]),
            'DC=0.6':np.array([0.1909, 0.1836, 0.1619, 0.1431, 0.1444, 0.1607, 0.1808, 0.2070, 0.2476, 0.2559, 0.2602]),
            'DC=0.75':np.array([0.1647, 0.1306, 0.1311, 0.1193, 0.1441, 0.1756, 0.1942, 0.2586, 0.2358, 0.1436, 0.0584]),
            'DC':np.array([0.2160, 0.2160, 0.2164, 0.2172, 0.2223, 0.2333, 0.2333, 0.2333, 0.2335, 0.2365, 0.2442, ]),
            'Sp':np.array([0.3723, 0.3611, 0.3605, 0.3517, 0.3523, 0.2212, 0.2333, 0.4112, 0.3854, 0.3722, 0.4768])}

Power_down = {'DC=0.3':np.array([0.2984, 0.1132, 0.3371, 0.5793, 0.6328, 0.6827, 0.7057, 0.6619, 0.7207, 0.7029, 0.7102]),
              'DC=0.45':np.array([0.5726, 0.6809, 0.7100, 0.7298, 0.7396, 0.7501, 0.7700, 0.7536, 0.7136, 0.6980, 0.6506]),
              'DC=0.6':np.array([0.6701, 0.7173, 0.7280, 0.7163, 0.7601, 0.7563, 0.7036, 0.6738, 0.6585, 0.6521, 0.6638]),
              'DC=0.75':np.array([0.6018, 0.5661, 0.6375, 0.5916, 0.6252, 0.5931, 0.5823, 0.6324, 0.6066, 0.4107, 0.2149]),
              'DC':np.array([0.7136, 0.7137, 0.7143, 0.7145, 0.7106, 0.6956, 0.6956, 0.6956, 0.6954, 0.6938, 0.6758, ]),
              'Sp':np.array([0.2864, 0.4612, 0.4699, 0.2766, 0.4572, 0.7154, 0.6956, 0.3358, 0.4733, 0.4583,  0.3807])}

Angle = {'DC=0.3':np.array([-0.9910, 0.2703, 3.1532, 6.5766, 9.6296, 12.3423, 14.8649, 17.3874, 19.5496, 21.5315, 23.6937]),
         'DC=0.45':np.array([1.7117, 5.1351, 8.1982, 10.9009, 13.6036, 16.6063, 18.6487, 21.1712, 23.6937, 25.8559, 28.7378]),
         'DC=0.6':np.array([4.5946, 8.1982, 11.2613, 14.3243, 17.0270, 19.7297, 22.2523, 24.7748, 28.0180, 30.5405, 32.8829]),
         'DC=0.75':np.array([8.0180, 11.6216, 14.8649, 17.9279, 20.8108, 23.8739, 26.5766, 29.2793, 32.3423, 35.4054, -36.4865]),
         'DC':np.array([24.55, 23.69, 23.87, 24.23, 24.77, 25.14, 25.14, 25.32, 25.50, 26.04, 26.76]),
         'Sp':np.array([39.91, 30.18, 31.08, 39.37, 29.28, 25.14, 38.65, 27.84, 28.20, 37.21])
         }

Field_overlap = {'DC=0.3':np.array([0.8140, 0.7986, 0.7344, 0.4860, 0.4577, 0.5174, 0.5602, 0.6435, 0.6727, 0.7325, 0.8112]),
                 'DC=0.45':np.array([0.6119, 0.6027, 0.6428, 0.6773, 0.6038, 0.6295, 0.6878, 0.7286, 0.8362, 0.8025, 0.8464]),
                 'DC=0.6':np.array([0.7653, 0.6984, 0.6810, 0.6695, 0.6626, 0.6977, 0.7877, 0.8614, 0.8485, 0.8939, 0.8657]),
                 'DC=0.75':np.array([0.6878, 0.6014, 0.6728, 0.6504, 0.6429, 0.6074, 0.5079, 0.8370, 0.7644, 0.5868, 0.8248]),
                 'DC':np.array([0.8362, 0.8361, 0.8385, 0.8392, 0.7848, 0.8797, 0.8798, 0.8796, 0.8797, 0.8758, 0.8994]),
                 'Sp':np.array([0.8242, 0.8216, 0.8101, 0.8580, 0.8312, 0.8394, 0.8797, 0.8794, 0.8216, 0.8133, 0.8733])
                }
                
Wlg = np.arange(1280, 1331, 5)

SE = scatteringEff(1, Reflection['Sp'], Transmission['Sp'], Wlg)

D = directionality("Down", Power_up['Sp'], Power_down['Sp'], Wlg)

CE = couplingEff(D, SE, Field_overlap['Sp'], Wlg)

from scipy.interpolate import interp1d




xnew = np.linspace(Wlg[0], Wlg[-1], num=100, endpoint=True)



f = interp1d(Wlg, D*100, kind = 'cubic')
f2 = interp1d(Wlg, CE*100, kind='cubic')
f3 = interp1d(Wlg, SE*100, kind='cubic')
f4 = interp1d(Wlg, Field_overlap['Sp']*100, kind = 'cubic')

plt.figure()
plt.plot(xnew, f2(xnew), color = 'blue', label = 'Coupling efficiency', linewidth = 3)
plt.xlabel('Wavelength [nm]', fontsize = 'medium')
plt.ylabel('Coupling efficiency [%]', fontsize = 'medium')
plt.legend(framealpha = 0.1, fontsize = 'small')
plt.show()
