from constant.physical_quantity import *
import domain.random_walk as random_walk
import domain.calculation as calculation
import view.output_view as output_view
import time as timer

PARTICLES = [EPS_PARTICLE, LATEX_PARTICLE, SILICA_PARTICLE]
FLUIDS = [WATER_FLUID]
TIMES = [10, 100, 300]  # seconds

TEMPERATURE = 298.15  # K (25 degrees Celsius)
UNIT_TIME = 0.1  # seconds
PARTICLE_COUNT = 500


def start(particle: Particle, fluid: Fluid, progress_time: int):
    # 시뮬레이션 정보 출력
    title = f'{particle.name} in {fluid.name} ({PARTICLE_COUNT} Particles, {progress_time} seconds)'
    output_view.show_title(title)
    output_view.show_parameters(particle.radius, particle.mass, particle.volume,
                                fluid.viscosity, fluid.density,
                                TEMPERATURE, progress_time, UNIT_TIME, PARTICLE_COUNT)

    # 시뮬레이션 시작
    start_time = timer.time()
    particle_positions = random_walk.progress(particle.radius, particle.mass, particle.volume,
                                              fluid.viscosity, fluid.density,
                                              TEMPERATURE, progress_time, UNIT_TIME, PARTICLE_COUNT)
    end_time = timer.time()
    elapsed_time = end_time - start_time
    output_view.show_elapsed_time(elapsed_time)

    # 시뮬레이션 결과 분석 및 출력
    msd = calculation.mean_square_displacement(particle_positions)
    rmsd = calculation.root_mean_square_displacement(particle_positions)
    avg_depth = calculation.average_depth(particle_positions)
    stddev_depth = calculation.standard_deviation_depth(particle_positions, avg_depth)
    output_view.show_analysis_results(msd, rmsd, avg_depth, stddev_depth)

    # 시뮬레이션 결과 시각화 및 출력
    output_view.show_particles(particle_positions, title)


if __name__ == "__main__":
    for particle in PARTICLES:
        for fluid in FLUIDS:
            for time in TIMES:
                start(particle, fluid, time)
