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

    ax2.scatter(X, Y, Z, c='blue', marker='o', s=4)
    ax2.set_box_aspect([1, 1, 1])

    # 그래프 표기 설정
    for ax in [ax1, ax2]:
        ax.set_xlabel('X Axis (m)', fontsize=7, labelpad=10)
        ax.set_ylabel('Y Axis (m)', fontsize=7, labelpad=10)
        ax.set_zlabel('Z Axis (m)', fontsize=7, labelpad=10)
        ax.tick_params(axis='both', which='major', labelsize=8)

    plt.show()


def _calculate_limit(X: List[float], Y: List[float], Z: List[float]) -> float:
    max_x = max(abs(v) for v in X)
    max_y = max(abs(v) for v in Y)
    max_z = max(abs(v) for v in Z)
    return max(max_x, max_y, max_z) * 1.05


def show_analysis_results(msd: float, rmsd: float, avg_depth: float, stddev_depth: float):
    print(f"Mean Square Displacement (MSD): {msd:.8e} m^2")
    print(f"Root Mean Square Displacement (RMSD): {rmsd:.8e} m")
    print(f"Average Depth: {avg_depth:.8e} m")
    print(f"Standard Deviation of Depth: {stddev_depth:.8e} m")
