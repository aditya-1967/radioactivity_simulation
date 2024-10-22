# importing important libraries
import numpy as np
import matplotlib.pyplot as plt
from DEq_Solver import DEq_Solver
from Radioactivity import Radioactivity
from RadioactivityABC import RadioactivityABC
from EulerSolver import EulerSolver as Solver

# initial conditions

N = 1000 # initial number of atoms
half_life = 0.2
t0 = 0.0 # time of start of the simulation
t1 = 1.0 # time of finish of the simulation
delta_t = 0.01

# create a Radioactive object and initialize a solver
radioactive = Radioactivity(half_life) # getting the analytical answer
solver = Solver(radioactive) # assigning the solver

# first simulation delta_t = 0.01
x0 = np.array([N], dtype = 'f')
result = solver.solve(x0, t0, t1, delta_t)
time, amount = zip(*result)
errors = radioactive.relative_error(result, t0, t1)
time_error, amount_error = zip(*errors)
simulation_1 = {'time': time, 'true_value': amount, 'error_value': amount_error}

# second simulation delta_t = delta_t / 10
x0 = np.array([N], dtype = 'f')
result = solver.solve(x0, t0, t1, delta_t / 10)
time, amount = zip(*result)
errors = radioactive.relative_error(result, t0, t1)
time_error, amount_error = zip(*errors)
simulation_2 = {'time': time, 'true_value': amount, 'error_value': amount_error}

# third simulation delta_t = delta_t * 5
x0 = np.array([N], dtype = 'f')
result = solver.solve(x0, t0, t1, delta_t * 5)
time, amount = zip(*result)
errors = radioactive.relative_error(result, t0, t1)
time_error, amount_error = zip(*errors)
simulation_3 = {'time': time, 'true_value': amount, 'error_value': amount_error}

# analytical solutuion
time = np.arange(t0, t1, delta_t/ 100)
x = radioactive.analytical(N, time)

# plotting the results in one plot
fig, ax = plt.subplots(1, 1, figsize=(7, 7))
label = r"$\Delta t={0:1.3f}$".format(delta_t)
ax.plot(simulation_1['time'], simulation_1['true_value'], label = label, color = 'blue')
label = r"$\Delta t={0:1.3f}$".format(delta_t/10)
ax.plot(simulation_2['time'], simulation_2['true_value'], label = label, color = 'red')
label = r"$\Delta t={0:1.3f}$".format(delta_t*5)
ax.plot(simulation_3['time'], simulation_3['true_value'], label = label, color = 'green')
label = 'Analytical'
ax.plot(time, x, label = label, color = 'yellow')
ax.legend()

# Save the plot to a file
plt.savefig('radioactivity_simulation_plot.png')

# plotting the errors
fig, ax = plt.subplots(1, 1, figsize=(7, 7))
label = r"$\Delta t={0:1.3f}$".format(delta_t)
ax.plot(simulation_1['time'], simulation_1['error_value'], label = label, color = 'blue')
label = r"$\Delta t={0:1.3f}$".format(delta_t/10)
ax.plot(simulation_2['time'], simulation_2['error_value'], label = label, color = 'red')
label = r"$\Delta t={0:1.3f}$".format(delta_t*5)
ax.plot(simulation_3['time'], simulation_3['error_value'], label = label, color = 'green')
ax.legend()

# Save the plot to a file
plt.savefig('radioactivity_error_plot.png')

# simulation for 3 nucli model
hlifeAs = [0.7, 0.3]
hlifeBs = [0.9, 0.2]

Result = {}
for (hlifeA, hlifeB) in zip(hlifeAs, hlifeBs):
    rABC = RadioactivityABC(hlifeA, hlifeB)
    solver = Solver(rABC)

    x0 = np.array([1000000, 0, 0], dtype='f')
    result = solver.solve(x0, 0, 5, 0.01)

    na, nb, nc = solver.coordinateSteps()
    ts = solver.timeSteps()
    Result[hlifeA] = {}
    Result[hlifeA]["na"] = na
    Result[hlifeA]["nb"] = nb
    Result[hlifeA]["nc"] = nc
    Result[hlifeA]["ts"] = ts

# plotting the results in one plot
fig, ax  = plt.subplots(1, 2, figsize = (20, 7))
panels = np.arange(2)
for (hlifeA, hlifeB, panel) in zip(hlifeAs, hlifeBs, panels):
    na = Result[hlifeA]["na"]
    nb = Result[hlifeA]["nb"]
    nc = Result[hlifeA]["nc"]
    ts = Result[hlifeA]["ts"]
    
    label = r"$A(t)$"
    ax[panel].plot(ts, na, label=label, color='blue')
    label = r"$B(t)$"
    ax[panel].plot(ts, nb, label=label, color='red')
    label = r"$C(t)$"
    ax[panel].plot(ts, nc, label=label, color='yellow')
    ax[panel].legend()
    ax[panel].set_xlabel("time, t [s]")
    ax[panel].set_ylabel(r"Abundance")
    ax[panel].set_xlim([0,5])
    ax[panel].set_ylim([0,1000000])
    title = r"$h_A=${0:1.2f}, $h_B$={1:1.2f}".format(hlifeA, hlifeB)
    ax[panel].set_title(title)
# Save the plot to a file
plt.savefig('radioactivityABC_simulations_plot.png')
