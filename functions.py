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


def calc_forces(_particles, time_moment):
    for i in range(len(_particles)):
        _particles[i].fx = 0
        _particles[i].fy = 0
        for j in range(len(_particles)):
            if i != j: 
                dist = ((_particles[i].xs[time_moment] - _particles[j].xs[time_moment])**2 + 
                           (_particles[i].ys[time_moment] - _particles[j].ys[time_moment])**2)**0.5
                force = F(dist)
                
                cos_phi = (_particles[j].xs[time_moment] - _particles[i].xs[time_moment]) / dist
                sin_phi = (_particles[j].ys[time_moment] - _particles[i].ys[time_moment]) / dist 

                _particles[i].fx += force * cos_phi
                _particles[i].fy += force * sin_phi
    
                
def integrate(_particles, start, stop, step, x_lim, y_lim):
    steps = int((stop - start) / step)

    for obj in _particles:
        x_verlet = obj.xs[0] - obj.vxs[0] * step
        y_verlet = obj.ys[0] - obj.vys[0] * step
        second_x = 2 * obj.xs[0] - x_verlet + obj.fx * step**2 / obj.m
        second_y = 2 * obj.ys[0] - y_verlet + obj.fy * step**2 / obj.m
        second_vx = (second_x - obj.xs[0]) / step
        second_vy = (second_y - obj.ys[0]) / step
        obj.x_update(second_x)
        obj.y_update(second_y)
        obj.vx_update(second_vx)
        obj.vy_update(second_vy)
        
    calc_forces(_particles, time_moment=1)
    
    for i in range(2, steps):
        for j in range(len(_particles)):
            _particles[j].vx = (_particles[j].xs[i-1] - _particles[j].xs[i-2]) / step
            _particles[j].vy = (_particles[j].ys[i-1] - _particles[j].ys[i-2]) / step
            _particles[j].vx_update( _particles[j].vx )
            _particles[j].vy_update( _particles[j].vy )
            
            _particles[j].x = 2 * _particles[j].xs[i-1] - _particles[j].xs[i-2] + _particles[j].fx / _particles[j].m * step**2
            _particles[j].y = 2 * _particles[j].ys[i-1] - _particles[j].ys[i-2] + _particles[j].fy / _particles[j].m * step**2
            _particles[j].x_update( _particles[j].x % x_lim )
            _particles[j].y_update( _particles[j].y % y_lim )
        calc_forces(_particles, time_moment=i)

def get_energy(_particles):        
    for i in range(len(_particles)):
        for j in range(len(_particles)):
            if i != j:
                dist = (( np.array(_particles[i].xs) - np.array(_particles[j].xs))**2 + 
                        (np.array(_particles[i].ys) - np.array(_particles[j].ys))**2)**0.5
                pot_energy = U(dist)
    
    kin_energy = []    
    for obj in _particles:
        kin_energy.append( obj.m * (np.array(obj.vxs)**2 + np.array(obj.vys)**2)**0.5 / 2  )
    kin_energy = np.array(kin_energy)
        
    return sum(kin_energy), sum(pot_energy), sum(kin_energy) + sum(pot_energy)
                
                