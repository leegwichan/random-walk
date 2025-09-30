import math

WATER_DENSITY = 997  # kg/m^3 at 25 degrees Celsius
WATER_VISCOSITY = 0.00089  # Pa·s (N·s/m^2) at 25 degrees Celsius
GLYCEROL_DENSITY = 1260  # kg/m^3 at 20 degrees Celsius
GLYCEROL_VISCOSITY = 1.412  # Pa·s (N·s/m^2) at 20 degrees Celsius
ETHANOL_DENSITY = 789  # kg/m^3 at 20 degrees Celsius
ETHANOL_VISCOSITY = 0.0012  # Pa·s (N·s/m^2)

IRON_DENSITY = 7874  # kg/m^3 (밀도가 높은 경우)
IRON_PARTICLE_RADIUS = 10e-6 # m
SILICA_DENSITY = 2650  # kg/m^3 (확산과 침강의 균형)
SILICA_PARTICLE_RADIUS = 2e-6  # m
LATEX_DENSITY = 1050  # kg/m^3 (물과 밀도가 비슷하여 순수한 브라운 운동)
LATEX_PARTICLE_RADIUS = 500e-9  # m


def mass(density, radius):
    return 4/3 * math.pi * density * (radius ** 3)
def volume(radius):
    return 4/3 * math.pi * (radius ** 3)