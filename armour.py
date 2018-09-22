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
    # Grade types with corresponding force in newtons
    grade = {'Type I': 583, 'Type II': 1761, 
             'Type III': 8609, 'Type IV': 10407}
        
    # Create new_calculation variable from calling force_newtons()
    new_calculation = force_newtons(mass, velocity)
        
    # Check which grade type matches with new calculation
    if grade['Type I'] >= float(new_calculation):
        return 'Grade: Type I'    
    elif grade['Type II'] >= float(new_calculation):
        return 'Grade: Type II'   
    elif grade['Type III'] >= float(new_calculation):
        return 'Grade: Type III'   
    else:
        return 'Grade: Type IV'


# Take user inputs to calculate force and return a matching grade type
def calculate(*args): 
    try:
        mass = float(mass_entry.get())
        velocity = float(velocity_entry.get())
        new_grade_type = grade_type(mass, velocity)
        print_grade_type.set(new_grade_type)
        return calculate
    except ValueError:
        pass 


# Initiate Tk   
root = Tk()
root.title("Armour Grade Certification")

# Mainframe configuration for GUI
mainframe = ttk.Frame(root, padding="5 5 5 5")# 3 3 12 12
mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Get inputs from GUI and print result on GUI
mass_entry = StringVar()
velocity_entry = StringVar()
print_grade_type = StringVar()

# Mass input box
mass_entry = ttk.Entry(mainframe, width=6, textvariable=mass_entry, justify='center')
mass_entry.grid(column=2, row=0, sticky=(E, W))

# Velocity input box
velocity_entry = ttk.Entry(mainframe, width=6, textvariable=velocity_entry, justify='center')
velocity_entry.grid(column=2, row=1, sticky=(E, W))

# Text labels on GUI
ttk.Label(mainframe, text="Mass(g):", anchor=E).grid(column=1, row=0, sticky=(E, W))
ttk.Label(mainframe, text="Velocity(m/s):", anchor=E).grid(column=1, row=1, sticky=(E, W))
ttk.Button(mainframe, text="Find", command=calculate).grid(column=3, row=0, sticky=(E, W))

# Display variable grade types on GUI
ttk.Label(mainframe, textvariable=print_grade_type, anchor=N).grid(column=3, row=1, sticky=(E, W))

# Configure resizing
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

mainframe.rowconfigure(1, weight = 1)
mainframe.columnconfigure(1, weight = 1)
mainframe.columnconfigure(2, weight = 3)
mainframe.columnconfigure(3, weight = 1)
mainframe.columnconfigure(4, weight = 3)

# Simultaneously apply padding configuration for all widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Initiates calculations when "Find" button is pressed
root.bind('<Return>', calculate)

# Cursor focused on mass input at program start up
mass_entry.focus()

# Start main loop
root.mainloop()