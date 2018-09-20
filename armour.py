#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Body Armour Certification
"""

# list of dictionaries for body armour grade types
certification = [{'Type I': '', 'Mass': 4.4, 'Velocity': 325.5, 'Acceleration': 132438, 'Force': 583},
               {'Type II': '', 'Mass': 9.1, 'Velocity': 393.5, 'Acceleration': 193553, 'Force': 1761},
               {'Type III': '', 'Mass': 9.6, 'Velocity': 847, 'Acceleration': 896761, 'Force': 8609},
               {'Type IV': '', 'Mass': 10.8, 'Velocity': 878, 'Acceleration': 963605, 'Force': 10407}]

# Calculate acceleration
def acceleration(velocity):
    velocity = float(velocity)
    distance = float(0.4)
    acceleration = (0.5 * velocity**2) / (distance)
    return acceleration


# Caculate force
def force(mass, acceleration):
    mass = float(mass)
    force = mass * acceleration
    return force


# Calculate force in newtons
def force_newtons():
    new_acceleration = acceleration(velocity)
    new_force = force(mass, new_acceleration)
    return round(new_force/1000)


# User prompt for mass and velocity inputs
mass = float(input("Mass(g): "))
velocity = float(input("Velocity(m/s): "))

