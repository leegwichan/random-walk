from vpython import *
import random

# 3D 캔버스 설정
scene.title = "N Particles Visualization"
scene.width = 800
scene.height = 600
scene.background = color.black
scene.autoscale = False # 자동 스케일링 끄기 (장면이 너무 커지는 것을 방지)
scene.range = 10 # 시야 범위 설정

num_particles = 5000
particles = []

# N개의 입자 생성
for i in range(num_particles):
    # -5에서 5 사이의 랜덤한 x, y, z 좌표 생성
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    z = random.uniform(-5, 5)

    # 각 입자를 sphere 객체로 생성
    # pos: 위치, radius: 반지름, color: 색상
    particle_sphere = sphere(pos=vector(x, y, z),
                             radius=0.03,
                             color=color.green)
    particles.append(particle_sphere)

print(f"{num_particles}개의 입자가 3D 공간에 시각화되었습니다.")

while True:
    rate(30) # 초당 30프레임으로 업데이트