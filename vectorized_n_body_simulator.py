"""
================================================================================
PROJECT: Vectorized N-Body Particle Simulator
DESCRIPTION: Simulates electrostatic interactions between protons and electrons 
             using Coulomb's Law. 
             
             ENGINEERING HIGHLIGHT: Instead of using slow nested 'for' loops 
             (which would cripple the CPU), this engine uses NumPy vectorization 
             and matrix broadcasting to calculate forces for all particles 
             simultaneously.
================================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import sympy as sp
import pytest

# ==========================================
# 1. SYMPY: Mathematical Verification
# ==========================================
def verify_physics_formula():
    """
    I like to use SymPy to symbolically prove my physics formulas before 
    running simulations. Here, we prove that our force calculation is 
    the correct derivative of the potential energy function.
    """
    print("--- Running SymPy Math Verification ---")
    r, k, q1, q2 = sp.symbols('r k q1 q2')
    
    # Potential energy formula (U = k*q1*q2 / r)
    potential_energy = (k * q1 * q2) / r
    
    # Force is the negative derivative of potential energy with respect to distance
    derived_force = -sp.diff(potential_energy, r)
    print(f"Calculated Force (F) : {derived_force}\n")


# ==========================================
# 2. THE CORE ENGINE (NumPy Optimized)
# ==========================================
class VectorizedNBody:
    def __init__(self, n_particles=150):
        self.N = n_particles
        self.k = 200          # Coulomb's constant (scaled up so we can see the effects)
        self.softening = 400  # A classic physics trick: prevents infinite forces/crashing when particles overlap
        self.box_size = 800   # Boundary limits for our container

        # Randomly assign particles as protons (True) or electrons (False)
        is_proton = np.random.rand(self.N) > 0.5
        
        # We use np.where here because it's much faster than iterating through a list.
        # It assigns properties