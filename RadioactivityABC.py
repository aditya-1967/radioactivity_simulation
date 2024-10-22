# importing important libraries
import numpy as np

class RadioactivityABC:
    def __init__(self, hlifeA, hlifeB):
        self.tauA = hlifeA / np.log(2)
        self.tauB = hlifeB / np.log(2)


    def dx_dt(self, x, t):
        Na, Nb, Nc = x #getting the values of Na, Nb and Nc from the array x
        
        dNa_dt = (-Na / self.tauA)
        dNb_dt = (Na / self.tauA) - (Nb / self.tauB)
        dNc_dt = (Nb / self.tauB)
        
        return np.array([dNa_dt, dNb_dt, dNc_dt])