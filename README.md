🔭 Brian Prendes | Computational Physics & Software Portfolio

Hi, I'm Brian Prendes, a Physics and Mechanical Engineering major at Yale University.

I am deeply passionate about designing, building, and exploring the intersection of quantum science and software engineering. This repository serves as a showcase of my ability to translate complex physical phenomena and advanced mathematics into optimized, visual, and highly efficient code.

📫 Let's Connect & Explore More of My Work

LinkedIn: brian-prendes-ab158a375

Email: brianlprendes@gmail.com

Hardware/Engineering Portfolio: (Insert the link to your other GitHub repository here!)

💻 Inside This Repository: Physics Simulation Suite

This repository contains a collection of Python-based simulation engines and data visualization tools designed to model physical systems and algorithmic behavior using advanced numerical methods.

1. Vectorized N-Body Electrostatic Simulator

File: vectorized_n_body_simulator.py

Physics: Simulates micro-universe interactions between protons and electrons using Coulomb's Law, tracking velocity, friction damping, and elastic boundary collisions.

Engineering Edge: Eliminates slow standard loops by utilizing NumPy vectorization and matrix broadcasting to calculate forces for 150+ particles simultaneously. Includes automated symbolic math verification using SymPy.

2. Numerical ODE Solver Dashboard

File: scipy_ode_solver_dashboard.py

Physics: Predicts the future dynamic states of a Spring-Mass Damper, a Non-Linear Pendulum (phase space tracking), and the chaotic 3D Lorenz Attractor.

Engineering Edge: Benchmarks native, custom-built Euler methods against optimized, industry-standard adaptive algorithms (SciPy's RK45) to demonstrate an understanding of numerical integration accuracy limits.

3. Monte Carlo Stochastic Physics Engine

File: monte_carlo_physics_simulator.py

Physics & Math: Leverages randomized algorithms to solve deterministic problems.

Features:

Approximates $\pi$ via geometric probability scattering.

Simulates quantum radioactive decay half-lives.

Maps 2D Brownian motion (random walks).

Simulates the thermodynamics of atomic magnetic spin alignments using the Metropolis-Hastings algorithm (Ising Model).

4. Real-Time Algorithm Visualizer

File: algorithm_visualizer.py

Computer Science: Bridges standard algorithmic logic with visual graphics. Uses Python yield generators to stream the intermediate array states of a sorting algorithm directly into a Matplotlib animation loop frame-by-frame.

⚙️ How to Run Locally

If you would like to run these simulations on your own machine, you will need Python installed along with a few standard scientific libraries.

1. Install Required Dependencies:

pip install numpy scipy sympy matplotlib pytest


2. Execute a Simulation:

python vectorized_n_body_simulator.py


(Simply replace the filename with whichever simulation you'd like to view).
