import random
import math

BOLTZMANN_CONSTANT = 1.380649e-23  # J/K
GRAVITY_ACCELERATION = 9.80665  # m/s^2
PI = math.pi


def progress(particle_radius,
             particle_mass,
             particle_volume,
             fluid_viscosity,
             fluid_density,
             temperature,
             time,
             unit_time,
             particle_count):
    diffusion_coefficient = BOLTZMANN_CONSTANT * temperature / (6 * PI * fluid_viscosity * particle_radius)
    step_length = (6 * diffusion_coefficient * unit_time) ** 0.5
    settling_velocity = (particle_mass - fluid_density * particle_volume) * GRAVITY_ACCELERATION / (
            6 * PI * fluid_viscosity * particle_radius)
    step_count = int(time / unit_time)

    particle_positions = []
    for _ in range(particle_count):
        x, y, z = 0.0, 0.0, 0.0
        for _ in range(step_count):
            theta = random.uniform(0, 2 * PI)
            cos_phi = random.uniform(-1, 1)
            phi = math.acos(cos_phi)

            dx = step_length * math.sin(phi) * math.cos(theta)  # dx = dl⋅sin(ϕ)⋅cos(θ)
            dy = step_length * math.sin(phi) * math.sin(theta)  # dy = dl⋅sin(ϕ)⋅sin(θ)
            dz = step_length * cos_phi - settling_velocity * unit_time  # dz = dl⋅cos(ϕ) - vs⋅dt (침강 고려)
            x += dx
            y += dy
            z = - abs(z + dz)
        particle_positions.append([x, y, z])
    return particle_positions
