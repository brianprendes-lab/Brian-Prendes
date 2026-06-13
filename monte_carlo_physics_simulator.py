"""
================================================================================
PROJECT: Monte Carlo Physics Simulation Suite
DESCRIPTION: Leverages stochastic (randomized) algorithms and large numbers of 
             trials to solve complex, non-deterministic physical problems.
================================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_pi_estimation(ax):
    """
    Estimates the value of Pi by randomly scattering points inside a square 
    and calculating the ratio of points that fall inside an inscribed circle.
    """
    N_darts = 10000
    
    # Generate random X and Y coordinates between -1 and 1
    x = np.random.uniform(-1, 1, N_darts)
    y = np.random.uniform(-1, 1, N_darts)
    
    # Check if points fall within the unit circle (x^2 + y^2 <= r^2)
    distance = x**2 + y**2
    inside_circle = distance <= 1 
    
    # Calculate Pi: (Area of Circle / Area of Square) = (Pi*r^2 / 4*r^2) = Pi/4
    # Therefore, Pi = 4 * (Points Inside / Total Points)
    pi_estimate = 4 * np.sum(inside_circle) / N_darts
    
    # Render the scatter plot
    ax.scatter(x[inside_circle], y[inside_circle], color='cyan', s=2, alpha=0.5, label='Inside')
    ax.scatter(x[~inside_circle], y[~inside_circle], color='red', s=2, alpha=0.5, label='Outside')
    ax.set_title(f"1. Estimate Pi (Result: {pi_estimate:.4f})", color='white')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

def simulate_radioactive_decay(ax):
    """
    Simulates the stochastic quantum decay of unstable isotopes over time
    to visualize the emergence of the exponential half-life curve.
    """
    N_atoms = 1000
    decay_probability = 0.05 # 5% chance an atom decays per time step
    time_steps = 100
    
    # Array representing the living atoms (1 = alive, 0 = decayed)
    atoms = np.ones(N_atoms)
    survival_history = []
    
    for t in range(time_steps):
        # Record current population
        survival_history.append(np.sum(atoms)) 
        
        # Generate a random roll (0.0 to 1.0) for every single atom instantly
        random_rolls = np.random.rand(N_atoms)
        
        # If the roll is less than the decay threshold, the atom "dies"
        decayed_this_step = (random_rolls < decay_probability)
        atoms[decayed_this_step] = 0 
        
    ax.plot(survival_history, color='lime', linewidth=3)
    ax.set_title("2. Radioactive Decay (Half-Life Curve)", color='white')
    ax.set_ylabel("Surviving Atoms", color='white')
    ax.set_xlabel("Time (Steps)", color='white')

def simulate_random_walk(ax):
    """
    Simulates Brownian motion (e.g., a particle suspended in fluid being 
    bombarded by invisible molecules) using a 2D random walk.
    """
    N_steps = 5000
    
    # Generate random positional nudges using a standard normal distribution
    dx = np.random.randn(N_steps)
    dy = np.random.randn(N_steps)
    
    # Use cumulative sum to map the continuous path taken
    x = np.cumsum(dx)
    y = np.cumsum(dy)
    
    # Draw the path and highlight start/end positions
    ax.plot(x, y, color='yellow', linewidth=0.8, alpha=0.8)
    ax.scatter(0, 0, color='green', s=100, label='Start', zorder=5) 
    ax.scatter(x[-1], y[-1], color='red', s=100, label='End', zorder=5) 
    ax.set_title("3. 2D Random Walk (Brownian Motion)", color='white')

def simulate_ising_model(ax):
    """
    Simulates ferromagnetism. Atoms try to align their magnetic spins 
    with their neighbors to lower total system energy, but ambient 
    temperature creates random chaotic flipping. Uses Metropolis-Hastings.
    """
    grid_size = 50
    temperature = 2.0 # Heat injects randomness. Higher temp = less organization.
    sweeps = 50       
    
    # Initialize a random lattice of atomic spins (+1 or -1)
    spins = np.random.choice([-1, 1], size=(grid_size, grid_size))
    
    # Metropolis-Hastings loop
    for _ in range(sweeps * grid_size**2):
        # Pick a random coordinate
        i, j = np.random.randint(0, grid_size, 2)
        current_spin = spins[i, j]
        
        # Calculate local neighborhood interactions (with periodic boundaries)
        neighbors = (spins[(i+1)%grid_size, j] + 
                     spins[(i-1)%grid_size, j] + 
                     spins[i, (j+1)%grid_size] + 
                     spins[i, (j-1)%grid_size])
        
        # Calculate energy delta if we were to flip this spin
        delta_energy = 2 * current_spin * neighbors
        
        # Rule 1: Always accept flips that lower the energy
        # Rule 2: Intermittently accept flips that raise energy based on thermal probability
        if delta_energy < 0 or np.random.rand() < np.exp(-delta_energy / temperature):
            spins[i, j] *= -1 

    # Render the lattice state as an image array
    ax.imshow(spins, cmap='coolwarm')
    ax.set_title(f"4. Ising Model (Temp: {temperature})", color='white')
    ax.axis('off')

# ==========================================
# DASHBOARD ORCHESTRATION
# ==========================================
if __name__ == "__main__":
    # Setup the main grid framework
    fig, axs = plt.subplots(2, 2, figsize=(12, 10), facecolor='#0f172a')
    fig.suptitle("Monte Carlo Physics Simulator Suite", color='white', fontsize=20, fontweight='bold')
    
    # Apply standard styling across all subplots
    for row in axs:
        for ax in row:
            ax.set_facecolor('#1e293b')
            ax.tick_params(colors='white')
            for spine in ax.spines.values():
                spine.set_color('#334155')

    # Execute and map simulations
    simulate_pi_estimation(axs[0, 0])
    simulate_radioactive_decay(axs[0, 1])
    simulate_random_walk(axs[1, 0])
    simulate_ising_model(axs[1, 1])

    plt.tight_layout()
    plt.show()