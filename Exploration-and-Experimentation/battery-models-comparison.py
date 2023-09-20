import pybamm as pb
import numpy as np
import matplotlib.pyplot as plt

START_TIME = 0
END_TIME = 3600

battery_models = {
    'dfn'   : pb.lithium_ion.DFN(),
    'spm'   : pb.lithium_ion.SPM(),
    'spme'  : pb.lithium_ion.SPMe(),
    'mpm'   : pb.lithium_ion.MPM()
}

solutions = {}

for key in battery_models:
    print('Simulating', key, end='')
    model = battery_models.get(key)
    simulation = pb.Simulation(model)
    solution = simulation.solve([START_TIME, END_TIME])
    solutions.update({key: solution})
    print('\t....Done')
    print(len(solutions))
    print(solutions[key])

#Use this line to plot generic parameters
pb.dynamic_plot(list(solutions.values()))

#For more specific parameters, use the below given code,
#And to search the required parameters run this line:
#print(model_dfn.variable_names())

for key in solutions:
    sol = solutions[key]

    print('Plotting', key, end='')
    plt.subplot(1,2,1)
    plt.title('Terminal Voltage [V]')
    plt.plot(sol['Terminal voltage [V]'].data, label=key)
    
    plt.subplot(1,2,2)
    plt.title('Open-circuit voltage [V]')
    plt.plot(sol['Battery open-circuit voltage [V]'].data, label=key)
    print('\t....Done')

plt.legend(loc="upper right")
plt.show()


print('--------Exit--------')