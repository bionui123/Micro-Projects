import pygame as pg
import random


class Particle(object):
    def __init__(self, mass, charge):
        self.mass = mass
        self.charge = charge

class Neutrino(Particle):
    def __init__(self, flavor, mass, charge):
        super().__init__(mass, charge)
        self.flavor = flavor

class Electron(Neutrino):
    def __init__(self):
        super().__init__("electron", 0.00001, 0)

class Muon(Neutrino):
    def __init__(self):
        super().__init__("muon", 0.00001, 0)

class Tau(Neutrino):
    def __init__(self):
        super().__init__("tau", 0.00001, 0)

class Nucleon(Particle):
    def __init__(self, mass, charge):
        super().__init__(mass, charge)

class Proton(Nucleon):
    def __init__(self):
        super().__init__(1.6726219e-27, 1)

class Neutron(Nucleon):
    def __init__(self):
        super().__init__(1.674927471e-27, 0)

class ParticleInstance:
    def __init__(self, particle_type, position, velocity):
        self.particle_type = particle_type
        self.position = position
        self.velocity = velocity

def create_random_coordinates(boundaries):
    return (random.randint(0, boundaries[0]), random.randint(0, boundaries[1]))

def render_particle(particle, x, y):
    sphere = pg.Surface((10, 10), pg.SRCALPHA)
    if isinstance(particle, Electron):
        pg.draw.circle(sphere, (255, 0, 0), (x, y), 5)
    elif isinstance(particle, Muon):
        pg.draw.circle(sphere, (0, 255, 0), (x, y), 5)
    elif isinstance(particle, Tau):
        pg.draw.circle(sphere, (0, 0, 255), (x, y), 5)
    elif isinstance(particle, Proton):
        pg.draw.circle(sphere, (255, 255, 0), (x, y), 5)
    elif isinstance(particle, Neutron):
        pg.draw.circle(sphere, (255, 0, 255), (x, y), 5)
    else:
        pg.draw.circle(sphere, (255, 255, 255), (x, y), 5)
    return sphere

# gameplay
pg.init()
screen = pg.display.set_mode((640, 480))

screen_boundaries = (640, 480)
particles = [Electron(), Muon(), Tau(), Proton(), Neutron()]
particle_spheres = []

for particle in particles:
    coordinates = create_random_coordinates(screen_boundaries)
    particle_spheres.append(render_particle(particle, coordinates[0], coordinates[1]))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    for sphere in particle_spheres:
        screen.blit(sphere, sphere.get_rect(center=create_random_coordinates(screen_boundaries)))
    pg.display.flip()

pg.quit()