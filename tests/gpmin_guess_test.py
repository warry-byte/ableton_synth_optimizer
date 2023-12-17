#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 12:00:04 2023

@author: warrybyte
"""

from skopt import Optimizer, Space, gp_minimize
from skopt.space import Integer, Real
from skopt.plots import plot_convergence

# Function to be optimized (returning a score based on user feedback)
def evaluate_numbers(guess):
    print(f"My guess: {guess}")
    feedback = input("How close is it to your pair? ")

    return int(feedback)


print("I will try to guess the two numbers you have in mind...")
print("Please help me in my search!")

search_space = Space([Real(low=0, high=10, prior='uniform', transform='normalize'),
                      Real(low=0, high=10, prior='uniform', transform='normalize')])


# Optimize the numbers
res = gp_minimize(func=evaluate_numbers,
                  dimensions=search_space,
                  n_calls=20,
                  n_initial_points=5,
                  acq_func='EI',
                  acq_optimizer='sampling',
                  noise="gaussian")

# Get the best numbers
best_numbers = res.x
print("Best Numbers:", best_numbers)
plot_convergence(res)

