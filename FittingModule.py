def fitter(data_file):

    from statistics import mean
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit

    data_array=np.loadtxt(data_file,skiprows=1)
    x=data_array[:,0]
    y=data_array[:,1]
    yerr=data_array[:,2]

    def line(x, a, b):
        return a*x+b
    popt, pcov =curve_fit(line, x,y, sigma=yerr)
    print("a=", popt[0], "+/-", pcov[0,0]**0.5)
    print("b=", popt[1], "+/-", pcov[1,1]**0.5)
    plt.figure(figsize=(8,4))
    plt.errorbar(x,y,yerr, fmt="ro")
    plt.plot(x, line(x, *popt))
    plt.xlabel("x values", fontsize=12)
    plt.ylabel("y values", fontsize=12)
    plt.show()