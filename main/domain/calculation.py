def mean_square_displacement(particle_positions):
    size = len(particle_positions)
    square_sum = 0.0
    for position in particle_positions:
        square_sum += position[0] ** 2 + position[1] ** 2 + position[2] ** 2
    return square_sum / size


def root_mean_square_displacement(particle_positions):
    return mean_square_displacement(particle_positions) ** 0.5


def average_depth(particle_positions):
    size = len(particle_positions)
    depth_sum = 0.0
    for position in particle_positions:
        depth_sum += position[2]
    return depth_sum / size


def standard_deviation_depth(particle_positions, average_depth):
    size = len(particle_positions)
    variance_sum = 0.0
    for position in particle_positions:
        variance_sum += (position[2] - average_depth) ** 2
    variance = variance_sum / size
    return variance ** 0.5
