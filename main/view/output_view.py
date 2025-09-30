from typing import List, Tuple
import matplotlib.pyplot as plt

ParticlePosition = Tuple[float, float, float]


def show_particles(particle_positions: List[ParticlePosition], title: str):
    X = [pos[0] for pos in particle_positions]
    Y = [pos[1] for pos in particle_positions]
    Z = [pos[2] for pos in particle_positions]

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # 그래프 눈금 설정
    ax.scatter(X, Y, Z, c='blue', marker='o', s=1)
    limit = _calculate_limit(X, Y, Z)
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.set_zlim(-limit, 0)
    ax.set_box_aspect([1, 1, 1])

    # 그래프 표기 설정
    ax.set_xlabel('X Axis (m)')
    ax.set_ylabel('Y Axis (m)')
    ax.set_zlabel('Z Axis (m)')
    ax.set_title(title)
    plt.show()

def _calculate_limit(X: List[float], Y: List[float], Z: List[float]) -> float:

    max_x = max(abs(v) for v in X)
    max_y = max(abs(v) for v in Y)
    max_z = max(abs(v) for v in Z)
    return max(max_x, max_y, max_z) * 1.1