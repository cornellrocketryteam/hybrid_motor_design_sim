"""Hybrid Motor Design and Combustion Modeling."""
import numpy as np
import constants as c

# Specific potential Energy Difference from altitude change.
delta_e_potential = -1*(c.mu/(c.R_earth + c.tenk_srad_altitude) - c.mu/(c.R_earth + c.ground_altitude))

# Equate the specific PE to specific KE to find a velocity change.

# This is the speed the rocket needs to be sent from ground in order to rach the desired apogee.
V_up_from_ground = np.sqrt(2*delta_e_potential)

# Event at apogee (3.05km) the difference between gravity from gravity at sea level is negligible.
delta_V_gravity_loss = c.g*c.burn_time_guess
# Low gravity loss typically means the trajectory has low drag loss.
# Therefore we assume they are the same value.
delta_V_drag_loss = delta_V_gravity_loss

# Total delta_V_estimate
delta_V_estimate = V_up_from_ground + delta_V_gravity_loss + delta_V_drag_loss
print('Estimated Delta V for launch: ' + str(delta_V_estimate))

# Use Tsiolkovsky's rocket equation to solve for desired mass ratio.
# Mass ratio = (rocket mass at ignition)/ (rocket mass at burnout)
rocket_mass_ratio = np.exp(delta_V_estimate/c.Ce)
print('Rocket Mass Ratio Estimate: ' + str(rocket_mass_ratio))

propellant_mass = c.rocket_dry_mass*(rocket_mass_ratio)
print('Rocket Propellant Mass Estimate: ' + str(propellant_mass))
c.propellant_mass = propellant_mass

avg_acceleration_guess = delta_V_estimate/c.burn_time_guess
print('Avg. Acceleration Estimate: ' + str(avg_acceleration_guess))
# F = ma, thrust - grav = (dry + prop) * avg_accel_est
thrust_estimate_initial = c.g*(c.rocket_dry_mass + c.propellant_mass) + (c.rocket_dry_mass + c.propellant_mass)*avg_acceleration_guess
print('Estimate of thrust produced by engine: ' + str(thrust_estimate_initial))



