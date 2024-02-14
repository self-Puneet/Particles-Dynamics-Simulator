import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import functions
from functions import *
import time
import math
import tkinter as tk
from tkinter import ttk

def simulate_particles():
    
    pass

def create_gui():
    root = tk.Tk()
    root.title("Particle Simulation")

    particle_label = ttk.Label(root, text="Number of particles:")
    particle_label.grid(row=0, column=0, padx=10, pady=10)
    particle_entry = ttk.Entry(root)
    particle_entry.grid(row=0, column=1, padx=10, pady=10)

    time_label = ttk.Label(root, text="Desired time:")
    time_label.grid(row=1, column=0, padx=10, pady=10)
    time_entry = ttk.Entry(root)
    time_entry.grid(row=1, column=1, padx=10, pady=10)

    division_label = ttk.Label(root, text="Time division (10^t):")
    division_label.grid(row=2, column=0, padx=10, pady=10)
    division_entry = ttk.Entry(root)
    division_entry.grid(row=2, column=1, padx=10, pady=10)

    simulate_button = ttk.Button(root, text="Simulate", command=simulate_particles)
    simulate_button.grid(row=3, column=0, columnspan=2, pady=20)

    result_label = ttk.Label(root, text="")
    result_label.grid(row=4, column=0, columnspan=2)

    root.mainloop()

# Your simulation parameters will be taken from the GUI entry fields
# For example:
# n = int(particle_entry.get())
# t = float(time_entry.get())
# t1 = int(division_entry.get())
# ...

# The rest of your simulation code goes here

if __name__ == "__main__":
    create_gui()
