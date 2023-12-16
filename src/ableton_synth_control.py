#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 18:22:30 2023

@author: warrybyte
"""

#%% Imports
import live
import random
from skopt import BayesSearchCV
import tkinter as tk
import sys

#%% User defined functions
# Define objective function with user evaluations
def objective_function():
    global set
    global user_evaluation
    global root
    
    set.start_playing()
    # Assuming your user provides evaluations (0 or 1 for bad/good) interactively
    root = tk.Tk()
    root.title("Rate what you are hearing")
    
    # Button for "Good"
    good_button = tk.Button(root, text="Good", command=lambda: set_evaluation(1))
    good_button.pack(side=tk.LEFT, padx=10)

    # Button for "Bad"
    bad_button = tk.Button(root, text="Bad", command=lambda: set_evaluation(0))
    bad_button.pack(side=tk.LEFT, padx=10)
    
    # Button for "Close"
    close_button = tk.Button(root, text="Close", command=lambda: close())
    close_button.pack(side=tk.RIGHT, padx=10)
    
    root.mainloop()
    
    return -user_evaluation  # Minimize, so use negative of user evaluation

# Return different evaluation and kill open dialog
def set_evaluation(value):
    global user_evaluation
    user_evaluation = value
    
    if user_evaluation == 0:
        print("User evaluation: BAD!")
    else: 
        print("User evaluation: GOOD!")
    
    
def close():
    global root
    global set
    set.stop_playing()
    root.update() # process pending events
    root.after(100, root.destroy)  # 100 milliseconds delay
    #root.destroy()
    sys.exit()

#%% Synth information
synth_name = "DS Clang"
excluded_param = ["Volume", "Device On"] # List of parameters that will not be part of the optimization process
user_evaluation = 0
root = None

#%% Get Live object
set = live.Set()
set.scan_import()  # Import all 

#%% Get track
track = set.tracks[0]
print("Track name %s" % track.name)

#%% Check synths parameters
param_list = track.get_device_named(synth_name).parameters

for p in param_list:
    print(p.name)
    
relevant_parameters_list = [ele for ele in param_list if (ele.name not in excluded_param)]

#%% Test objective function
objective_function()

    
