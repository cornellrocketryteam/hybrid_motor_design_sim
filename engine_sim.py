"""Engine simulation."""
import numpy as np
import constants as c

"""Final vapor mass"""
mass_vapor = 0.12*c.propellant_mass

# x is the propellant mass that when added to the final vapor mass, gives the required start propellant mass
x = c.propellant_mass*(1-0.12)
print("Mass of fuel required: " + str(mass_vapor) +  " kg")

"""The Nitrous Vapor Burn"""

"""How much nozzle mass flow rate?"""

R=287.1 #j/kg*k
y= 1.3 # fluids constant
pe= 101325 #pa
pcp= 350 #psi 
Tc=3300; #K 
Ft=7040; #N
pc=350*6894.76; #psi to pa 

ves=np.sqrt((2*R*y/(y-1))*Tc*(1-(pe/pc)**((y-1)/y))) #hybrid propulsion book pg 166
#ve=[str(ves) ' m/s']
V_exhaust = ves
print('Exhaust Velocity: ' + str(ves))

mdot=Ft/ves

gma=y*(2/(y+1))**((y+1)/(y-1));
cstar=np.sqrt(((R*Tc)/gma))
astar=(mdot*cstar)/pc ;
throat_diameter_cm=np.sqrt(astar/np.pi)*2*100 # throat diameter in cm 
print('Throat diameter estimate (cm): ' + str(throat_diameter_cm))
mox=mdot*(7/8)
print('Mass flowrate of oxidizer: ' + str(mox) + 'kg/s')

thrust_estimate_initial = 7040 #N
nozzle_mdot_initial = thrust_estimate_initial/V_exhaust

print('Initial mass flowrate (nozzle): ' + str(nozzle_mdot_initial) + 'kg/s')

# Combustion chamber:
