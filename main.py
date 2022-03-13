from functions import init_particles, integrate, get_energy
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 


PART_NUM = 10
X_LIM = 10
Y_LIM = 10
START = 0
STOP = 10
STEP = 0.01

# =============================================================================
# params1 = [1, 1.5, 5, -0, 0]
# params2 = [1, 9.5, 5, 0, 0]
# particles = special_init(params1, params2)
# =============================================================================

particles = init_particles(PART_NUM, X_LIM, Y_LIM)

integrate(particles, START, STOP, STEP, X_LIM, Y_LIM)

k_e, p_e, t_e = get_energy(particles)

plt.plot(t_e)

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









