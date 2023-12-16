#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 18:22:30 2023

@author: warrybyte
"""

#%% Imports
import live
import random

#%% Synth information
synth_name = "DS Clang"
excluded_param = ["Volume", "Device On"] # List of parameters that will not be part of the optimization process

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

#%% Init optimizer
a = 0 
    
