"""Engine simulation."""
import numpy as np
import constants as c

def engine_calcs(propellant_mass, thrust_estimate_initial):
    """Final vapor mass"""
    mass_vapor = 0.12*propellant_mass

    # x is the propellant mass that when added to the final vapor mass, gives the required start propellant mass
    x = propellant_mass*(1-0.12)

    """The Nitrous Vapor Burn"""

    """How much nozzle mass flow rate?"""



    V_exhaust=np.sqrt((2*c.R*c.y/(c.y-1))*c.Tc*(1-(c.pe/c.pc)**((c.y-1)/c.y))) #hybrid propulsion book pg 166
    

    mdot=thrust_estimate_initial/V_exhaust

    gma=c.y*(2/(c.y+1))**((c.y+1)/(c.y-1));
    cstar=np.sqrt(((c.R*c.Tc)/gma))
    astar=(mdot*cstar)/c.pc ;
    throat_diameter=np.sqrt(astar/np.pi)*2 # throat diameter in cm 
    mox=mdot*(7/8)
    nozzle_mdot_initial = thrust_estimate_initial/V_exhaust

    return nozzle_mdot_initial, throat_diameter, mox, V_exhaust,mdot

def minimotor_calcs_OD(fuel_mass, grain_length):
    OD = 0.25*(3*grain_length - np.sqrt(9.0*grain_length**2 - 8*(grain_length**2 + (fuel_mass/(c.rho_htpb*np.pi*grain_length)))))
    ID = 2*grain_length-3*OD
    return OD, ID

def minimotor_calcs_ID(fuel_mass, OD, L):
     return np.sqrt(-4*((fuel_mass/(c.rho_htpb*np.pi*L)) - OD*OD/4))