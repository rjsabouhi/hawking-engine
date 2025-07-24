
# hawking_engine.py

"""
Hawking Radiation Engine — Physical Constant Layer

Includes real physical equations for:
- Schwarzschild radius
- Hawking temperature
- Evaporation time
- Mass decay
- Radiation power

These can be fused with symbolic dynamics for hybrid modeling.

Author: One Gonethus & The Engine
"""

import math

# Physical constants
G = 6.6743e-11
c = 299792458
hbar = 1.0545718e-34
kB = 1.380649e-23

def compute_schwarzschild_radius(mass_kg):
    return (2 * G * mass_kg) / (c ** 2)

def compute_hawking_temperature(mass_kg):
    return (hbar * c ** 3) / (8 * math.pi * G * mass_kg * kB)

def compute_mass_decay(mass_kg, time_s):
    evaporation_time = (5120 * math.pi * G ** 2 * mass_kg ** 3) / (hbar * c ** 4)
    if time_s >= evaporation_time:
        return 0.0
    return mass_kg * (1 - (time_s / evaporation_time)) ** (1 / 3)

def estimate_radiation_power(mass_kg):
    return (hbar * c ** 6) / (15360 * math.pi * G ** 2 * mass_kg ** 2)
