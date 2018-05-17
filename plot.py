#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

u_filter = pd.read_csv("SLOAN_SDSS_u.dat", header=None, delimiter=" ")
print u_filter.head(10)

plt.figure()
plt.plot(u_filter[0], u_filter[1])
plt.show()

spectra_1 = pd.read_csv("1_edited.csv", header=None, skiprows=[0], usecols=[0,1])
print spectra_1.head(10)
