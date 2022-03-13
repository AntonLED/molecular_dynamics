class Particle: 
    def __init__(self, m, x_0, y_0, vx_0, vy_0):
        self.m = m 
        self.x = x_0
        self.y = y_0 
        self.vx = vx_0
        self.vy = vy_0
        self.fx = 0
        self.fy = 0 
        self.xs = [x_0]
        self.ys = [y_0]
        self.vxs = [vx_0]
        self.vys = [vy_0]
        self.fxs = [0]
        self.fys = [0]
    def x_update(self, new_x, active=False):
        self.xs.append(new_x)
    def y_update(self, new_y, active=False):
        self.ys.append(new_y)
    def vx_update(self, new_vx):
        self.vxs.append(new_vx)
    def vy_update(self, new_vy):
        self.vys.append(new_vy)
