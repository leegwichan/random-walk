from typing import List, Tuple
from vpython import *

# 3D 캔버스 설정
scene.title = "N Particles Visualization"
scene.width = 800
scene.height = 600
scene.background = color.black
scene.autoscale = False
scene.show_axis = True

ParticlePosition = Tuple[float, float, float]
particles = []


def show_particles(particle_positions: List[ParticlePosition]):
    max_x = max(abs(pos[0]) for pos in particle_positions)
    max_y = max(abs(pos[1]) for pos in particle_positions)
    max_z = max(abs(pos[2]) for pos in particle_positions)

    max_movement = max(max_x, max_y, max_z)
    scene.range = max_movement * 1.5
    visual_radius = scene.range * 0.005
    scene.center = vector(0, 0, -max_z / 2)
    scene.camera.pos = vector(0, 0, scene.range)


    for pos in particle_positions:
        x, y, z = pos
        print(x, y, z)
        particle_sphere = sphere(pos=vector(x, y, z), radius=visual_radius, color=color.green)
        particles.append(particle_sphere)
    print(f"{len(particle_positions)}개의 입자가 3D 공간에 시각화되었습니다.")

    while True:
        rate(30)  # 초당 30프레임으로 업데이트