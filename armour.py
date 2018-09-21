#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Body Armour Certification
"""
from tkinter import *
from tkinter import ttk

 # Caculate acceleration
def acceleration(velocity):
    velocity = float(velocity)
    distance = float(0.4)
    acceleration = (0.5 * velocity**2) / (distance)
    return acceleration


# Caculate velocity
def force(mass, acceleration):
    mass = float(mass)
    force = mass * acceleration
    return force


# Calculate force(in newtons)
def force_newtons(mass, velocity):
    new_acceleration = acceleration(velocity)
    new_force = force(mass, new_acceleration)
    return round(new_force/1000)


# Match new calculation of force in newtons with certification grade type
def grade_type(mass, velocity):
    # Dictionary of grade types with corresponding force in newtons
    grade = {'Type I': 583, 'Type II': 1761, 
             'Type III': 8609, 'Type IV': 10407}
        
    # Create new_calculation variable from calling force_newtons()
    new_calculation = force_newtons(mass, velocity)
        
    # Check to see which grade type matches with new calculation
    if grade['Type I'] >= float(new_calculation):
        return 'Grade: Type I'    
    elif grade['Type II'] >= float(new_calculation):
        return 'Grade: Type II'   
    elif grade['Type III'] >= float(new_calculation):
        return 'Grade: Type III'   
    else:
        return 'Grade: Type IV'

# Make calculations taking mass and velocity inputs from user
def calculate(*args): 
    try:
        mass = float(mass_entry.get())
        velocity = float(velocity_entry.get())
        new_grade_type = grade_type(mass, velocity)
        print_grade_type.set(new_grade_type)
        return calculate
    except ValueError:
        pass 

   
root = Tk()
root.title("Armour Grade Certification")

# Mainframe configuration for GUI
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Get inputs from GUI and print result on GUI
mass_entry = StringVar()
velocity_entry = StringVar()
print_grade_type = StringVar()

# Mass input box
mass_entry = ttk.Entry(mainframe, width=7, textvariable=mass_entry)
mass_entry.grid(column=2, row=1, sticky=(W, E))

# Velocity input box
velocity_entry = ttk.Entry(mainframe, width=7, textvariable=velocity_entry)
velocity_entry.grid(column=2, row=2, sticky=(W, E))

# Text labels on GUI
ttk.Label(mainframe, text="Mass(g):").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Velocity(m/s):").grid(column=1, row=2, sticky=W)
ttk.Button(mainframe, text="Find", command=calculate).grid(column=3, row=1, sticky=W)

# Display variable grade types on GUI
ttk.Label(mainframe, textvariable=print_grade_type).grid(column=3, row=2, sticky=W)#output area

# Simultaneously apply padding configuration for all widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Initiates calculations when "Find" button is pressed
root.bind('<Return>', calculate)

mass_entry.focus()
velocity_entry.focus()
root.mainloop()