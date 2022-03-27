from functions import init_particles, integrate, get_energy, special_init
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import numpy as np 

PART_NUM = 150
X_LIM = 50
Y_LIM = 50
START = 0
STOP = 10
STEP = 0.01

# =============================================================================
# params1 = [1, 1.5, 5, -1, 0]
# params2 = [1, 9.5, 5, 0, 0]
# particles = special_init(params1, params2)
# =============================================================================


particles = init_particles(PART_NUM, X_LIM, Y_LIM)

integrate(particles, START, STOP, STEP, X_LIM, Y_LIM)

k_e, p_e, t_e = get_energy(particles, X_LIM, Y_LIM)
    

plt.plot(np.linspace(START, STOP, int(STOP - START) / STEP), k_e, color="red")
plt.plot(np.linspace(START, STOP, int(STOP - START) / STEP), p_e, color="green")
plt.plot(np.linspace(START, STOP, int(STOP - START) / STEP), t_e, color="black")


# animation
fig, ax = plt.subplots()
ax = plt.axes(xlim=(0, X_LIM), ylim=(0, Y_LIM))
plt.grid(True)
lines=[]

for i in range(len(particles)):
    line, = ax.plot([], [], '.')
    lines.append(line,)
    
def animation_frame(n):
    for i in range(len(particles)):
        lines[i].set_xdata(particles[i].xs[n])
        lines[i].set_ydata(particles[i].ys[n])
    
animate = animation.FuncAnimation(fig, animation_frame, frames=10000, interval=1, repeat=True)    









