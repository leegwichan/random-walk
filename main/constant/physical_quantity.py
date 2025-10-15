import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Fluid:
    name: str
    density: float  # kg/m^3
    viscosity: float  # Pa·s


@dataclass(frozen=True)
class Particle:
    name: str
    density: float  # kg/m^3
    radius: float  # m
    mass: float  # kg
    volume: float  # m^3

    @staticmethod
    def create(name: str, density: float, radius: float) -> 'Particle':
        volume = (4 / 3) * math.pi * (radius ** 3)
        mass = density * volume
        return Particle(name, density, radius, mass, volume)


WATER_FLUID = Fluid("Water", 997.0, 0.00089)  # 25°C
GLYCEROL_FLUID = Fluid("Glycerol", 1258.0, 0.934)  # 25°C
ETHANOL_FLUID = Fluid("Ethanol", 785.0, 0.00107)  # 25°C

EPS_PARTICLE = Particle.create("EPS", 50.0, 1e-6)
LATEX_PARTICLE = Particle.create("Latex", 1050.0, 500e-9)
PVC_PARTICLE = Particle.create("PVC", 1380.0, 1e-6)
SILICA_PARTICLE = Particle.create("Silica", 2650.0, 2e-6)
IRON_PARTICLE = Particle.create("Iron", 7874.0, 10e-6)
WATER_PARTICLE = Particle.create("Water", 997.0, 1.5e-10)
