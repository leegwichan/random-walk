# Diffusion and Sedimentation of Brownian Particles via Random Walk Monte Carlo Simulation

[한국어 버전](./README.md)

This repository contains the implementation code for a study that analyzes the simultaneous diffusion (Brownian motion) and sedimentation (Stokes settling) of microparticles in a viscous fluid using a random-walk-based Monte Carlo simulation. It simulates three particle types — EPS, latex, and silica — in 3D and visualizes how the relationship between particle density and fluid density governs the competition between the two transport mechanisms.

## Background

Microparticles in a fluid undergo Brownian diffusion and gravity/buoyancy-driven sedimentation at the same time. Which mechanism dominates depends on the particle's physical properties (density, radius), and this behavior is central to applications such as environmental monitoring, colloidal separation, and microfluidics.

This study implements a 3D random walk simulation that includes both mechanisms together, allowing the effect of particle properties on the time-evolving spatial distribution to be both quantitatively analyzed and visually inspected.

## Key Results

All scenarios use the same environment: 500 particles in water at 25 ℃ with $\Delta t = 0.1\,s$. Only the particle type varies.

### EPS particles (density 50 kg/m³, radius 1 µm)

Particles are much lighter than the fluid, so buoyancy dominates — almost no sedimentation occurs and the distribution stays near the surface (z = 0), governed by diffusion.

|   30 s   |  120 s   |  300 s   |
|:--------:|:--------:|:--------:|
| ![EPS 30s](./images/EPS_Particles_in_Water_030s.png) | ![EPS 120s](./images/EPS_Particles_in_Water_120s.png) | ![EPS 300s](./images/EPS_Particles_in_Water_300s.png) |

### Latex particles (density 1380 kg/m³, radius 1 µm)

Particles are slightly heavier than the fluid — diffusion and sedimentation compete on a comparable scale, producing a fairly isotropic distribution.

|   30 s   |  120 s   |  300 s   |
|:--------:|:--------:|:--------:|
| ![Latex 30s](./images/Latex_Particles_in_Water_030s.png) | ![Latex 120s](./images/Latex_Particles_in_Water_120s.png) | ![Latex 300s](./images/Latex_Particles_in_Water_300s.png) |

### Silica particles (density 2650 kg/m³, radius 2 µm)

Particles are denser than the fluid and have a larger radius, so sedimentation dominates — the cloud of particles drifts visibly downward (negative z) over time.

|   30 s   |  120 s   |  300 s   |
|:--------:|:--------:|:--------:|
| ![Silica 30s](./images/Silica_Particles_in_Water_030s.png) | ![Silica 120s](./images/Silica_Particles_in_Water_120s.png) | ![Silica 300s](./images/Silica_Particles_in_Water_300s.png) |

## Getting Started

### Requirements

- Python 3.11.x
- matplotlib 3.10.x

### Run

```bash
cd main
python main.py
```

Edit the `PARTICLES`, `FLUIDS`, and `TIMES` lists at the top of `main.py` to change scenarios. Result images are written to the `output/` directory at the repository root.

## Project Structure

```
main/
├── constant/    Particle / Fluid definitions
├── domain/      Simulation core and statistical analysis (MSD, RMSD, ...)
├── view/        Visualization and console output
└── main.py      Entry point
docs/
└── simulation-model.md   Physical model, boundary conditions, formulas, parameters (Korean)
images/                  Result snapshots used in this README
output/                  Simulation images produced at runtime
```

## Detailed Model and Formulas

For the full technical specification — physical model, assumptions, boundary conditions, formulas, parameter definitions, and the core logic — see [docs/simulation-model.md](./docs/simulation-model.md). The document is currently available in Korean only.
