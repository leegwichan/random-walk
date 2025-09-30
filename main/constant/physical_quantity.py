import math

# 유체 물리량 (25°C / 298.15 K 기준)
WATER_DENSITY = 997.0  # kg/m^3
WATER_VISCOSITY = 0.00089  # Pa·s
GLYCEROL_DENSITY = 1258.0  # kg/m^3 (25°C)
GLYCEROL_VISCOSITY = 0.934  # Pa·s (25°C)
ETHANOL_DENSITY = 785.0  # kg/m^3 (25°C)
ETHANOL_VISCOSITY = 0.00107  # Pa·s (25°C)

# 입자 물리량
# EPS 입자
EPS_DENSITY = 50.0  # kg/m^3
EPS_PARTICLE_RADIUS = 1e-6  # m
# 라텍스 입자
LATEX_DENSITY = 1050.0  # kg/m^3
LATEX_PARTICLE_RADIUS = 500e-9  # m
# PVC 입자
PVC_DENSITY = 1380.0  # kg/m^3
PVC_PARTICLE_RADIUS = 1e-6  # m
# 실리카 입자
SILICA_DENSITY = 2650.0  # kg/m^3
SILICA_PARTICLE_RADIUS = 2e-6  # m
# 철 입자
IRON_DENSITY = 7874.0  # kg/m^3
IRON_PARTICLE_RADIUS = 10e-6  # m


def mass(density, radius):
    return 4 / 3 * math.pi * density * (radius ** 3)


def volume(radius):
    return 4 / 3 * math.pi * (radius ** 3)
