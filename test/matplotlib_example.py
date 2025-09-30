import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # 좌표 리스트 (Numpy 배열 형태로 준비)
    data = np.array([(0.01, 0.02, 0.03), (0.02, 0.01, -0.01), (-0.03, 0.00, 0.02), (0.00, 0.03, 0.01)])
    X, Y, Z = data[:, 0], data[:, 1], data[:, 2]

    # 3D 축 생성
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 3D 산점도 그리기
    ax.set_box_aspect([1, 1, 1])
    ax.scatter(X, Y, Z, c='blue', marker='o')

    # 축 레이블 설정
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('Particle Positions (Matplotlib 3D)')

    plt.show()
