#import numpy as np
import pandas as pd


def scale_within_range(filter, spectra):
    if filter is 'u':
        u_filter = pd.read_csv("SLOAN_SDSS_u.dat", header=None, delimiter=" ")
        get_u_fac = lambda w: get_fac(w, u_filter)
        get_u_facs = vectorize(get_u_fac)
        
        spectra_facs = get_u_facs(spectra[0]) # assuming order is the same
        scaled = spectra[1] * spectra_facs

def get_fac(wavelength, filter_df): 
    fac = filter_df[filter_df[0] == wavelength]
    if len(fac) is 0:
        f = inter(filter_df[0], filter_df[1])
        return f(wavelength)
    else:
        return fac[1]


