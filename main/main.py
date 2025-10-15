from constant.physical_quantity import *
import domain.random_walk as random_walk
import domain.calculation as calculation
import view.output_view as output_view
import time

FLUID_DENSITY = WATER_DENSITY
FLUID_VISCOSITY = WATER_VISCOSITY

PARTICLE_RADIUS = SILICA_PARTICLE_RADIUS
PARTICLE_MASS = mass(SILICA_DENSITY, PARTICLE_RADIUS)
PARTICLE_VOLUME = volume(PARTICLE_RADIUS)

TEMPERATURE = 298.15  # K (25 degrees Celsius)
TIME = 300  # seconds
UNIT_TIME = 0.1  # seconds
PARTICLE_COUNT = 500

TITLE = "Silica Particles in Water (%d Particles, %d seconds)" % (PARTICLE_COUNT, TIME)

if __name__ == "__main__":
    start_time = time.time()
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
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"걸린 시간 (time.time()): {elapsed_time:.8f} s")

    msd = calculation.mean_square_displacement(particle_positions)
    rmsd = calculation.root_mean_square_displacement(particle_positions)
    avg_depth = calculation.average_depth(particle_positions)
    stddev_depth = calculation.standard_deviation_depth(particle_positions, avg_depth)

    output_view.show_analysis_results(msd, rmsd, avg_depth, stddev_depth)
    output_view.show_particles(particle_positions, TITLE)
