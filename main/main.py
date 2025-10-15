from constant.physical_quantity import *
import domain.random_walk as random_walk
import domain.calculation as calculation
import view.output_view as output_view
import time

FLUID_DENSITY = WATER_DENSITY
FLUID_VISCOSITY = WATER_VISCOSITY

# PARTICLE_RADIUS = SILICA_PARTICLE_RADIUS
# PARTICLE_MASS = mass(SILICA_DENSITY, PARTICLE_RADIUS)
# PARTICLE_VOLUME = volume(PARTICLE_RADIUS)

PARTICLE_RADIUS = WATER_PARTICLE_RADIUS
PARTICLE_MASS = mass(WATER_DENSITY, PARTICLE_RADIUS)
PARTICLE_VOLUME = volume(PARTICLE_RADIUS)

TEMPERATURE = 298.15  # K (25 degrees Celsius)
TIME = 240  # seconds
UNIT_TIME = 0.1  # seconds
PARTICLE_COUNT = 500

TITLE = "Silica Particles in Water (%d Particles, %d seconds)" % (PARTICLE_COUNT, TIME)

if __name__ == "__main__":
    print("== Simulation Parameters ==")
    print("particle_radius: %.2e m" % PARTICLE_RADIUS)
    print("particle_mass: %.2e kg" % PARTICLE_MASS)
    print("particle_volume: %.2e m^3" % PARTICLE_VOLUME)
    print("fluid_viscosity: %.2e Pa·s" % FLUID_VISCOSITY)
    print("fluid_density: %.2e kg/m^3" % FLUID_DENSITY)
    print("temperature: %.2f K" % TEMPERATURE)
    print("time: %.2f s" % TIME)
    print("unit_time: %.2f s" % UNIT_TIME)
    print("particle_count: %d" % PARTICLE_COUNT)

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
    print("== Simulation Completed ==")
    print(f"걸린 시간 (time.time()): {elapsed_time:.8f} s")

    msd = calculation.mean_square_displacement(particle_positions)
    rmsd = calculation.root_mean_square_displacement(particle_positions)
    avg_depth = calculation.average_depth(particle_positions)
    stddev_depth = calculation.standard_deviation_depth(particle_positions, avg_depth)

    output_view.show_analysis_results(msd, rmsd, avg_depth, stddev_depth)
    output_view.show_particles(particle_positions, TITLE)
