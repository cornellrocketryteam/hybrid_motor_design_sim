import numpy as np
import constants as c
from trajectory_guess_generator import rocket_calcs
from engine_sim import engine_calcs, minimotor_calcs_OD, minimotor_calcs_ID

# Desired burntime
burn_time_guess = 5 # seconds
# primary input
desired_altitude =410000 # meters
# or input desired initial thrust
desired_thrust = 250*4.448 # 250-pounds in Newtons
# Main:

propellant_mass_estimate, thrust_estimate_initial = rocket_calcs(desired_altitude, burn_time_guess)

nozzle_mdot_initial, throat_diameter, mox, V_exhaust,mdot = engine_calcs(propellant_mass_estimate, thrust_estimate_initial)

#OD, ID = minimotor_calcs_OD(0.125*propellant_mass_estimate, 0.2)
OD = 0.09525 # 3.75 inches in m
grain_length = 0.165
ID = minimotor_calcs_ID(0.125*propellant_mass_estimate, 0.09525, grain_length)

print('Mini Motor Propellant Mass Estimate: ' + str(propellant_mass_estimate) + ' kg')
print('Mini Motor Fuel Grain Mass Estimate: ' + str(0.125*propellant_mass_estimate) + ' kg')
print('Motor Thrust Estimate: ' + str(thrust_estimate_initial) + 'N')
print('Initial mass flowrate (nozzle): ' + str(nozzle_mdot_initial) + ' kg/s')
print('Mass flowrate of oxidizer: ' + str(mox) + ' kg/s')
print('Fuel Grain Outer Diameter: ' + str(OD) + ' meters')
print('Fuel Grain Inner Diameter: ' + str(ID) + ' meters')
print('Fuel Grain Length: ' + str(grain_length) + ' meters')