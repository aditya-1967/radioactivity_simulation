# importing important libraries
from DEq_Solver import DEq_Solver

class EulerSolver(DEq_Solver):
    def __init__(self, kernel):
        self.kernel = kernel
    
    def makeStep(self):
        dx_dt = self.kernel.dx_dt(self.x, self.t)
        self.x += dx_dt * self.delta_t
        self.t += self.delta_t