# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Random-walk Monte Carlo simulation of Brownian particles undergoing simultaneous diffusion (Brownian motion) and sedimentation (Stokes' law) in a viscous fluid, with a reflective boundary at the water surface (z=0). Outputs per-particle 3D end positions, quantitative analysis (MSD, RMSD, mean/stddev depth), and matplotlib scatter plots. `README.md` is the project intro (Korean primary, `README.en.md` for English); the full physics derivation, formulas, and parameter spec live in `docs/simulation-model.md`.

The code, comments, and console output are largely in Korean — preserve language when editing existing strings.

## Running

The simulation must be run from inside `main/` because:
- Imports are written as top-level packages (e.g. `from constant.physical_quantity import *`, `import domain.random_walk`) rather than `main.constant...`, so `main/` is the implicit source root.
- `view/output_view.py` saves figures to `../output/` relative to CWD.

```powershell
# From repo root
cd main
python main.py
```

Dependencies (no requirements.txt — install ad hoc):
- Python 3.11.x
- matplotlib 3.10.x

There is no test runner, linter, or build step configured. The `test/` directory contains standalone matplotlib/vpython demos (`test/matplotlib_example.py`, `test/vpython_random_walk_example.py`), not a test suite.

## Architecture

Three-layer split inside `main/`, each layer importing only from layers above it:

- `constant/physical_quantity.py` — frozen `@dataclass` value objects `Fluid` and `Particle` plus pre-defined instances (`WATER_FLUID`, `EPS_PARTICLE`, `LATEX_PARTICLE`, `SILICA_PARTICLE`, etc.). `Particle.create(name, density, radius)` derives mass and volume from a sphere assumption — always construct particles via this factory rather than the raw dataclass.
- `domain/random_walk.py` — `progress(...)` is the simulation kernel. Computes diffusion coefficient `D = kT / (6πηr)`, step length `l = √(6·D·Δt)`, and terminal settling velocity `vs = (m − ρ_fluid·V)·g / (6πηr)`. Each step picks a uniform random direction on the sphere, then applies `dz = l·cos(φ) − vs·Δt`. Surface reflection at z=0 is implemented as `z = -abs(z + dz)` (folds positive z back into the fluid). All particles start at the origin.
- `domain/calculation.py` — pure functions over the position list: `mean_square_displacement`, `root_mean_square_displacement`, `average_depth`, `standard_deviation_depth`.
- `view/output_view.py` — `print(...)` reporters plus `show_particles(...)`, which writes a dual-panel (fixed-scale + auto-scale) 3D scatter to `../output/<title>.png`. The output directory is git-ignored except for `.gitkeep`; it must exist at runtime.

`main.py` is the orchestrator — a triple loop over `PARTICLES × FLUIDS × TIMES` calling `start(...)` per combination. Adding new scenarios means appending to those module-level lists, not changing `start`.

## Conventions specific to this repo

- Physical constants live next to the code that uses them (`BOLTZMANN_CONSTANT`, `GRAVITY_ACCELERATION`, `PI` in `domain/random_walk.py`), not in `constant/` — `constant/` is reserved for domain value objects.
- The simulation kernel takes a flat positional argument list (radius, mass, volume, viscosity, density, temperature, time, unit_time, count) — when adding parameters, update both `random_walk.progress` and the call site in `main.start`.
- Particle positions are passed around as `list[list[float]]` of `[x, y, z]`, not as the `ParticlePosition = Tuple[float, float, float]` alias declared in `output_view.py`. The alias is descriptive, not enforced.
- Output filenames are derived from the scenario `title` string (e.g. `EPS in Water (500 Particles, 300 seconds).png`) — keep titles filesystem-safe when adding scenarios.
