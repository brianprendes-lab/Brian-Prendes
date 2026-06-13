"""
================================================================================
PROJECT: Numerical Ordinary Differential Equation (ODE) Solver
DESCRIPTION: Demonstrates the ability to model real-world dynamic physical 
             systems using advanced numerical integration (SciPy's RK45) vs. 
             custom naive implementations (Euler's method).
================================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ==========================================
# PHYSICS SYSTEM DEFINITIONS
# ==========================================

def spring_mass(t, state):
    """
    ODE for a simple harmonic oscillator (mass attached to a spring with friction).
    State tracking: [position, velocity]
    """
    x, v = state
    m = 1.0   # Mass of the object
    k = 20.0  # Spring stiffness coefficient
    c = 0.5   # Damping coefficient (friction)
    
    # Newton's Second Law: Acceleration = F/m = (-kx - cv) / m
    acceleration = -(k/m)*x - (c/m)*v
    return [v, acceleration]

def pendulum(t, state):
    """
    ODE for a non-linear swinging pendulum.
    State tracking: [angle, angular_velocity]
    """
    theta, omega = state
    g = 9.81  # Gravity constant
    L = 1.0   # Length of the pendulum string
    
    # Angular Acceleration = -(g/L) * sin(theta)
    alpha = -(g/L) * np.sin(theta)
    return [omega, alpha]

def lorenz(t, state):
    """
    ODE for the Lorenz Attractor (modeling chaotic atmospheric convection).
    Famous for demonstrating the 'Butterfly Effect'.
    State tracking: [x, y, z] coordinates
    """
    x, y, z = state
    sigma = 10.0
    rho = 28.0
    beta = 8.0 / 3.0
    
    # The coupled differential equations
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]

# ==========================================
# CUSTOM NAIVE SOLVER (For Benchmark)
# ==========================================
def euler_method(func, y0, t_eval):
    """
    A basic, first-order numerical procedure for solving ODEs.
    We build this manually to show why advanced solvers like RK45 are necessary.
    It predicts the next step by drawing straight tangent lines.
    """
    dt = t_eval[1] - t_eval[0] # Calculate time step size
    y = np.zeros((len(y0), len(t_eval)))
    y[:, 0] = y0
    
    for i in range(len(t_eval) - 1):
        # Next State = Current State + (Rate of Change * Time Step)
        rates = np.array(func(t_eval[i], y[:, i]))
        y[:, i+1] = y[:, i] + rates * dt
        
    return y

# ==========================================
# MAIN DASHBOARD VISUALIZATION
# ==========================================
if __name__ == "__main__":
    # Create a 2x2 grid. Note the special 3D projection for subplot 4.
    fig = plt.figure(figsize=(14, 10), facecolor='#0f172a')
    fig.suptitle("SciPy ODE Solvers: Predicting Physics", color='white', fontsize=20, fontweight='bold')
    
    ax1 = fig.add_subplot(221, facecolor='#1e293b')
    ax2 = fig.add_subplot(222, facecolor='#1e293b')
    ax3 = fig.add_subplot(223, facecolor='#1e293b')
    ax4 = fig.add_subplot(224, projection='3d', facecolor='#1e293b')

    # Apply modern styling
    for ax in [ax1, ax2, ax3]:
        ax.tick_params(colors='white')
        for spine in ax.spines.values():
            spine.set_color('#334155')

    # --- PLOT 1: Spring-Mass (Euler vs SciPy RK45) ---
    t_span_spring = [0, 10]
    t_eval_spring = np.linspace(0, 10, 150) # Coarse steps to expose Euler's flaws
    state_0 = [2.0, 0.0] # Initial state: Pulled to x=2, released from rest

    # Solve using SciPy's optimized Runge-Kutta 4(5) algorithm
    sol_rk = solve_ivp(spring_mass, t_span_spring, state_0, t_eval=t_eval_spring, method='RK45')
    # Solve using our naive manual method
    sol_euler = euler_method(spring_mass, state_0, t_eval_spring)

    ax1.plot(sol_rk.t, sol_rk.y[0], label="SciPy (Runge-Kutta)", color='lime', linewidth=2)
    ax1.plot(t_eval_spring, sol_euler[0], label="Basic Euler (Overshooting)", color='red', linestyle='--')
    ax1.set_title("1. Spring-Mass (Solver Accuracy Comparison)", color='white')
    ax1.set_ylabel("Position (x)", color='white')
    ax1.legend()

    # --- PLOT 2: Pendulum (Time Series) ---
    t_span_pend = [0, 10]
    t_eval_pend = np.linspace(0, 10, 500)
    
    # Start the pendulum almost completely upside down (3.1 radians)
    sol_pend = solve_ivp(pendulum, t_span_pend, [3.1, 0.0], t_eval=t_eval_pend)

    ax2.plot(sol_pend.t, sol_pend.y[0], color='cyan', linewidth=2)
    ax2.set_title("2. Non-Linear Pendulum (Angle Tracking)", color='white')
    ax2.set_ylabel("Angle (Radians)", color='white')

    # --- PLOT 3: Pendulum (Phase Space) ---
    # Phase spaces plot Position vs. Velocity to visualize the energy state
    ax3.plot(sol_pend.y[0], sol_pend.y[1], color='magenta', linewidth=2)
    ax3.set_title("3. Pendulum Phase Space (Energy Conservation)", color='white')
    ax3.set_xlabel("Angle", color='white')
    ax3.set_ylabel("Angular Velocity", color='white')

    # --- PLOT 4: Lorenz Attractor (3D Chaos) ---
    t_span_lor = [0, 40]
    t_eval_lor = np.linspace(0, 40, 5000)
    sol_lor = solve_ivp(lorenz, t_span_lor, [1.0, 1.0, 1.0], t_eval=t_eval_lor)

    ax4.plot(sol_lor.y[0], sol_lor.y[1], sol_lor.y[2], color='yellow', linewidth=0.5)
    ax4.set_title("4. Lorenz Attractor (3D Chaotic Path)", color='white')
    
    # 3D styling adjustments
    ax4.xaxis.set_pane_color((0.11, 0.16, 0.23, 1.0))
    ax4.yaxis.set_pane_color((0.11, 0.16, 0.23, 1.0))
    ax4.zaxis.set_pane_color((0.11, 0.16, 0.23, 1.0))
    ax4.tick_params(colors='white')

    plt.tight_layout()
    plt.show()