# importing important libraries
import numpy as np

class Radioactivity:
    def __init__(self, hlife):
        self.tau = hlife / np.log(2) # half_life of a radioactive element is ln(2) times mean life time
    
    def dx_dt(self, x, t):
        return -(x / self.tau)
    
    def analytical(self, x0, t):
        return x0 * np.exp(-t / self.tau)
    
    def relative_error(self, test, t0, t1):
        res = []
        for t, x in test:
            if len(res) == 0:
                x0 = x
            res.append((t, x / self.analytical(x0, t - t0) - 1))
        return res