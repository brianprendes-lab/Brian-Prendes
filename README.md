#  Brian Prendes — Physics, Engineering & Software Portfolio

**Physics & Mechanical Engineering · Yale University**
> Bridging quantum science, engineering and software together for accurate results

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat&logo=scipy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=matplotlib&logoColor=white)
![Yale](https://img.shields.io/badge/Yale_University-00356B?style=flat&logoColor=white)

---

## 📫 Let's connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-brian--prendes-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/brian-prendes-ab158a375/)
[![Email](https://img.shields.io/badge/Email-brianlprendes%40gmail.com-D14836?style=flat&logo=gmail&logoColor=white)](mailto:brianlprendes@gmail.com)
[![Hardware Portfolio](https://brian-prendes.github.io/)](#)

---

## 💻 Physics simulation suite

A collection of Python-based simulation engines and data visualization tools designed to model physical systems and algorithmic behavior using advanced numerical methods.

---

### 01 · Vectorized N-Body Electrostatic Simulator
`vectorized_n_body_simulator.py`

**Physics:** Simulates micro-universe interactions between protons and electrons using Coulomb's Law, tracking velocity, friction damping, and elastic boundary collisions.

**Engineering edge:** Eliminates slow loops via NumPy vectorization and matrix broadcasting to calculate forces for 150+ particles simultaneously. Includes automated symbolic math verification using SymPy.

![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![SymPy](https://img.shields.io/badge/SymPy-3B5526?style=flat-square&logoColor=white)

---

### 02 · Numerical ODE Solver Dashboard
`scipy_ode_solver_dashboard.py`

**Physics:** Predicts the future dynamic states of a Spring-Mass Damper, a Non-Linear Pendulum (phase space tracking), and the chaotic 3D Lorenz Attractor.

**Engineering edge:** Benchmarks native custom-built Euler methods against SciPy's RK45 adaptive algorithms to demonstrate understanding of numerical integration accuracy limits.

![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white)

---

### 03 · Monte Carlo Stochastic Physics Engine
`monte_carlo_physics_simulator.py`

**Physics & math:** Leverages randomized algorithms to solve deterministic problems.

- Approximates π via geometric probability scattering
- Simulates quantum radioactive decay half-lives
- Maps 2D Brownian motion (random walks)
- Models atomic magnetic spin thermodynamics via Metropolis-Hastings (Ising Model)

![Monte Carlo](https://img.shields.io/badge/Monte_Carlo-Stochastic-success?style=flat-square)
![Ising Model](https://img.shields.io/badge/Metropolis--Hastings-Ising_Model-blueviolet?style=flat-square)

---

### 04 · Real-Time Algorithm Visualizer
`algorithm_visualizer.py`

**Computer science:** Bridges algorithmic logic with live visual graphics. Uses Python `yield` generators to stream intermediate array states of sorting algorithms directly into a Matplotlib animation loop, frame-by-frame.

![Matplotlib](https://img.shields.io/badge/Matplotlib-Animation-11557C?style=flat-square)
![Generators](https://img.shields.io/badge/Python-yield_generators-3776AB?style=flat-square&logo=python&logoColor=white)

---

## How to run locally

**1. Install dependencies:**

```bash
pip install numpy scipy sympy matplotlib pytest
```

**2. Run any simulation:**

```bash
python vectorized_n_body_simulator.py
```

Replace the filename with whichever simulation you'd like to explore.
