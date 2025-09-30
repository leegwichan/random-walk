import view.output_view as output_view
import domain.random_walk as random_walk
from constant.physical_quantity import *

FLUID_DENSITY = WATER_DENSITY
FLUID_VISCOSITY = WATER_VISCOSITY

PARTICLE_RADIUS = LATEX_PARTICLE_RADIUS
PARTICLE_MASS = mass(LATEX_DENSITY , PARTICLE_RADIUS)
PARTICLE_VOLUME = volume(PARTICLE_RADIUS)

TEMPERATURE = 298.15  # K (25 degrees Celsius)
TIME = 10  # seconds
UNIT_TIME = 0.01  # seconds
PARTICLE_COUNT = 5000

TITLE = "Random Walk Simulation of Latex Particles in Water"

if __name__ == "__main__":
    particle_positions = random_walk.progress(
        particle_radius=PARTICLE_RADIUS,
        particle_mass=PARTICLE_MASS,
        particle_volume=PARTICLE_VOLUME,
        fluid_viscosity=FLUID_VISCOSITY,
        fluid_density=FLUID_DENSITY,
        temperature=TEMPERATURE,
        time=TIME,
        unit_time=UNIT_TIME,
        particle_count=PARTICLE_COUNT
    )
    output_view.show_particles(particle_positions, TITLE)
