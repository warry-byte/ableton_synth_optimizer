#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 12:00:04 2023

@author: warrybyte
"""

from skopt import Optimizer, Space
from skopt.space import Integer, Real
from skopt.plots import plot_convergence

# Function to be optimized (returning a score based on user feedback)
def evaluate_numbers(guess):
    print(f"My guess: {guess}")
    feedback = input("Is it good, bad, or correct? ").lower()

    if feedback == "correct":
        return 0  # Score 0 for correct guess
    elif feedback == "good":
        return 1  # Score 1 for a good guess
    else:
        return -1  # Score -1 for a bad guess


search_space = Space([Integer(low=0, high=10, prior='uniform', transform='normalize'),
                      Integer(low=0, high=10, prior='uniform', transform='normalize')])

# Initialize the optimizer
opt = Optimizer(search_space,
                "GP",
                acq_func="EI",
                acq_optimizer="sampling",
                initial_point_generator="lhs")


# Optimize the numbers
res = None

for _ in range(20):  # Adjust the number of iterations as needed
    suggestion = opt.ask()
    score = evaluate_numbers(suggestion)
    if score == 0:
        break
    res = opt.tell(suggestion, score)

# Get the best numbers
best_numbers = res.x
print("Best Numbers:", best_numbers)
plot_convergence(res)

