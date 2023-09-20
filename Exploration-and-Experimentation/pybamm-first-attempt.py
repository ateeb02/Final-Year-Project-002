import pybamm as pb
import numpy as np
import matplotlib as plt


battery_models = [
    
]


print("where is my terminal ?!?!")

pb.print_citations()
# To get all variables/plots in simulation, run the following line
# print(model_dfn.variable_names())
# and for keyword based search, run
# print(model_dfn.variables.search('variable name'))

model_dfn = pb.lithium_ion.DFN()
model_spm = pb.lithium_ion.SPM()

sim_dfn = pb.Simulation(model_dfn)
sim_spm = pb.Simulation(model_spm)

sim_dfn.solve([0,3600])
sim_spm.solve([0,3600])

#print(model_dfn.variable_names())

print('nevermind found it')

sol_dfn = sim_dfn.solution #will pass an object to sol_dfn
print(sol_dfn) #location of the solution

sol_spm = sim_spm.solution #will pass an object to sol_spm
print(sol_spm) #location of the solution

sim_dfn.plot()
sim_spm.plot()

sim_dfn.plot([['Terminal voltage [V]', 'Battery open-circuit voltage [V]'], ['Electrolyte current density [A.m-2]', 'Electrode current density [A.m-2]']])
sim_spm.plot([['Terminal voltage [V]', 'Battery open-circuit voltage [V]'], ['Electrolyte current density [A.m-2]', 'Electrode current density [A.m-2]']])


tv_dfn = sol_dfn['Terminal voltage [V]']
tv_spm = sol_spm['Terminal voltage [V]']


plt.pyplot.title('Terminal Voltage [V]')

#plt.pyplot.subplot(1,2,1)
plt.pyplot.plot(tv_dfn.data, label='DFN')

#plt.pyplot.subplot(1,2,2)
plt.pyplot.plot(tv_spm.data, label='SPM')

plt.pyplot.legend(loc="upper right")
plt.pyplot.show()

#sim_spm.plot()


print('--------Exit--------')