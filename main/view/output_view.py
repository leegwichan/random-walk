from typing import List, Tuple
import matplotlib.pyplot as plt

ParticlePosition = Tuple[float, float, float]


def show_particles(particle_positions: List[ParticlePosition], title: str):
    X = [pos[0] for pos in particle_positions]
    Y = [pos[1] for pos in particle_positions]
    Z = [pos[2] for pos in particle_positions]

    fig = plt.figure(figsize=(10, 5))
    fig.suptitle(title)
    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122, projection='3d')

    # 그래프 눈금 설정
    ax1.scatter(X, Y, Z, c='blue', marker='o', s=4)
    limit = _calculate_limit(X, Y, Z)
    ax1.set_xlim(-limit, limit)
    ax1.set_ylim(-limit, limit)
    ax1.set_zlim(-limit, 0)
    ax1.set_box_aspect([1, 1, 1])
    ax1.set_title("Fixed Scale", fontsize=10)

    ax2.scatter(X, Y, Z, c='blue', marker='o', s=4)
    ax2.set_box_aspect([1, 1, 1])
    ax2.set_title("Auto Scale", fontsize=10)

    # 그래프 표기 설정
    for ax in [ax1, ax2]:
        ax.set_xlabel('X Axis (m)', fontsize=7, labelpad=10)
        ax.set_ylabel('Y Axis (m)', fontsize=7, labelpad=10)
        ax.set_zlabel('Z Axis (m)', fontsize=7, labelpad=10)
        ax.tick_params(axis='both', which='major', labelsize=8)

    plt.savefig(f'../output/{title}.png', dpi=300, bbox_inches='tight', pad_inches=0.5)


def _calculate_limit(X: List[float], Y: List[float], Z: List[float]) -> float:
    max_x = max(abs(v) for v in X)
    max_y = max(abs(v) for v in Y)
    max_z = max(abs(v) for v in Z)
    return max(max_x, max_y, max_z) * 1.05


def show_title(title: str):
    print(f"\n== {title} ==")


def show_parameters(particle_radius: float,
                    particle_mass: float,
                    particle_volume: float,
                    fluid_viscosity: float,
                    fluid_density: float,
                    temperature: float,
                    time: float,
                    unit_time: float,
                    particle_count: int):
    print("\n== Simulation Parameters ==")
    print("particle_radius: %.2e m" % particle_radius)
    print("particle_mass: %.2e kg" % particle_mass)
    print("particle_volume: %.2e m^3" % particle_volume)
    print("fluid_viscosity: %.2e Pa·s" % fluid_viscosity)
    print("fluid_density: %.2e kg/m^3" % fluid_density)
    print("temperature: %.2f K" % temperature)
    print("time: %.2f s" % time)
    print("unit_time: %.2f s" % unit_time)
    print("particle_count: %d" % particle_count)


def show_elapsed_time(elapsed_time: float):
    print("\n== Simulation Elapsed Time ==")
    print(f"걸린 시간 (time.time()): {elapsed_time:.8f} s")


def show_analysis_results(msd: float, rmsd: float, avg_depth: float, stddev_depth: float):
    print("\n== Analysis Results ==")
    print(f"Mean Square Displacement (MSD): {msd:.8e} m^2")
    print(f"Root Mean Square Displacement (RMSD): {rmsd:.8e} m")
    print(f"Average Depth: {avg_depth:.8e} m")
    print(f"Standard Deviation of Depth: {stddev_depth:.8e} m")
