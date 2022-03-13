from Particle import Particle
from dependences import F, U
import numpy as np 
import random


def init_particles(num, x_lim, y_lim):
    _particles = []
    for i in range(num):
        _particles.append(
                Particle(
                m=random.randint(1, 2), 
                x_0=random.randint(0, x_lim), 
                y_0=random.randint(0, y_lim), 
                vx_0=random.randint(-3, 3), 
                vy_0=random.randint(-3, 3)
                ))
    return np.array(_particles)


def calc_forces(_particles, time_moment, x_lim, y_lim):
    for i in range(len(_particles)):
        _particles[i].fx = 0
        _particles[i].fy = 0
        for j in range(len(_particles)):
            if i != j: 
                dist_x = _particles[i].xs[time_moment] - _particles[j].xs[time_moment]
                dist_y = _particles[i].ys[time_moment] - _particles[j].ys[time_moment]                
                              
                # boundary conditions
                if abs(dist_x) > x_lim / 2:
                    dist_x = dist_x - np.sign(dist_x) * x_lim
                if abs(dist_y) > y_lim / 2:
                    dist_y = dist_y - np.sign(dist_y) * y_lim
                
                dist = (dist_x**2 + dist_y**2)**0.5
                
                force = F(dist)
                
                cos_phi = -dist_x / dist
                sin_phi = -dist_y / dist 
                                
                _particles[i].fx += force * cos_phi 
                _particles[i].fy += force * sin_phi 

                
def integrate(_particles, start, stop, step, x_lim, y_lim):
    steps = int((stop - start) / step)

    for particle in _particles:
        x_verlet = particle.xs[0] - particle.vxs[0] * step
        y_verlet = particle.ys[0] - particle.vys[0] * step
        second_x = 2 * particle.xs[0] - x_verlet + particle.fx * step**2 / particle.m
        second_y = 2 * particle.ys[0] - y_verlet + particle.fy * step**2 / particle.m
        second_vx = (second_x - particle.xs[0]) / step
        second_vy = (second_y - particle.ys[0]) / step
        particle.x_update(second_x % x_lim)
        particle.y_update(second_y % y_lim)
        particle.vx_update(second_vx)
        particle.vy_update(second_vy)
        
    calc_forces(_particles, time_moment=1, x_lim=x_lim, y_lim=y_lim)
    
    for i in range(2, steps):
        for j in range(len(_particles)):            
            _particles[j].x = 2 * _particles[j].xs[i-1] - _particles[j].xs[i-2] + _particles[j].fx / _particles[j].m * step**2
            _particles[j].y = 2 * _particles[j].ys[i-1] - _particles[j].ys[i-2] + _particles[j].fy / _particles[j].m * step**2
            _particles[j].x_update( _particles[j].x % x_lim )
            _particles[j].y_update( _particles[j].y % y_lim )
            
            _particles[j].vx = ((_particles[j].xs[i-1] - _particles[j].xs[i-2]) % x_lim) / step
            _particles[j].vy = ((_particles[j].ys[i-1] - _particles[j].ys[i-2]) % y_lim) / step
            _particles[j].vx_update( _particles[j].vx )
            _particles[j].vy_update( _particles[j].vy )
        calc_forces(_particles, time_moment=i, x_lim=x_lim, y_lim=y_lim)

def get_energy(_particles, x_lim, y_lim): 
    particles_potential = []
    for i in range(len(_particles)):
        for j in range(len(_particles)):
            if i != j:
                dist_x = np.array(_particles[i].xs) - np.array(_particles[j].xs)
                dist_y = np.array(_particles[i].ys) - np.array(_particles[j].ys)
                
                for d_x in dist_x:
                    if abs(d_x) > x_lim / 2:
                        d_x = d_x - np.sign(d_x) * x_lim
                for d_y in dist_y:
                    if abs(d_y) > y_lim / 2:
                        d_y = d_y - np.sign(d_y) * y_lim
                        
                dist = (dist_x**2 + dist_y**2)**0.5
                particles_potential.append(U(dist))
    system_potential = sum(particles_potential)    
            
    particles_kinetic = []
    for particle in _particles:
        particles_kinetic.append(particle.m * (np.array(particle.vxs)**2 + np.array(particle.vys)**2) / 2)
    system_kinetic = sum(particles_kinetic)
    
    return system_kinetic, system_potential, system_kinetic + system_potential
                
def special_init(par1, par2):
    _particles = []
    particle1 = Particle(
            m = par1[0],
            x_0 = par1[1],
            y_0 = par1[2], 
            vx_0 = par1[3],
            vy_0 = par1[4]
        )
    particle2 = Particle(
            m = par2[0],
            x_0 = par2[1],
            y_0 = par2[2], 
            vx_0 = par2[3],
            vy_0 = par2[4]
        )
    _particles.append(particle1)
    _particles.append(particle2)
    
    return np.array(_particles)
    
    
    
    
    
    
    
    
    
    
    
    