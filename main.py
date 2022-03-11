from functions import init_particles, integrate, get_energy 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import numpy as np 

PART_NUM = 5
X_LIM = 10
Y_LIM = 10
START = 0
STOP = 10
STEP = 0.01

particles = init_particles(PART_NUM, X_LIM, Y_LIM)

integrate(particles, START, STOP, STEP, X_LIM, Y_LIM)

k_e, p_e, t_e = get_energy(particles)

plt.plot(np.linspace(START, STOP, int((STOP-START)/STEP)), t_e)


# animation
fig, ax = plt.subplots()
ax = plt.axes(xlim=(0, X_LIM), ylim=(0, Y_LIM))
plt.grid(True)
lines=[]

for i in range(len(particles)):
    line, = ax.plot([], [], 'o')
    lines.append(line,)
    
def animation_frame(n):
    for i in range(len(particles)):
        lines[i].set_xdata(particles[i].xs[n])
        lines[i].set_ydata(particles[i].ys[n])
    
animate = animation.FuncAnimation(fig, animation_frame, frames=10000, interval=1, repeat=True)    









