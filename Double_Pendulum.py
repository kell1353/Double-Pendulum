import sys
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

G = 9.807  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of the first pendulum in m
L2 = 1.0  # length of the second pendulum in m
M1 = .05  # mass of the first pendulum in kg
M2 = .05  # mass of the second pendulum in kg


def derivs(state, t):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    del_ = state[2] - state[0]
    den1 = (M1 + M2)*L1 - M2*L1*cos(del_)*cos(del_)
    dydx[1] = (M2*L1*state[1]*state[1]*sin(del_)*cos(del_) +
               M2*G*sin(state[2])*cos(del_) +
               M2*L2*state[3]*state[3]*sin(del_) -
               (M1 + M2)*G*sin(state[0]))/den1

    dydx[2] = state[3]

    den2 = (L2/L1)*den1
    dydx[3] = (-M2*L2*state[3]*state[3]*sin(del_)*cos(del_) +
               (M1 + M2)*G*sin(state[0])*cos(del_) -
               (M1 + M2)*L1*state[1]*state[1]*sin(del_) -
               (M1 + M2)*G*sin(state[2]))/den2

    return dydx

# create a time array from 0..100 sampled at 0.05 second steps
dt = 0.05
t = np.arange(0.0, 60, dt)

# th1 and th2 are the initial angles (degrees)
# w1 and w2 are the initial angular velocities (degrees per second)
th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0

# initial state
state = np.radians([th1, w1, th2, w2])

#initial total energy
def calc_E(y):
        """Calculate the total energy of the system"""
        U = -((M1 + M2)*G*L1*cos(th1) - M2*G*cos(th2))
        K = .5*M1*((L1)**2)*((th1)**2) + (.5*M2*((L1)**2)*((th1)**2) + ((L2)**2)*((th2)**2) + 2*L1*L2*th1*th2*cos(th1 - th2))
        return U + K

# integrate your ODE using scipy.integrate.
y = integrate.odeint(derivs, state, t)

x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1



"""Start plotting graph"""

fig = plt.figure()
limit = 3
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-limit, limit), ylim=(-limit, limit))
ax.set_aspect('equal')

fig.set_facecolor('black')
ax.set_facecolor('black')

ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')
ax.tick_params(axis = 'both', color='white', labelcolor = 'white')
#ax.grid()


""" Plot the center point"""
c0 = plt.Circle((0,0), .035, fc = 'k', zorder = 10)
ax.add_patch(c0)


line, = ax.plot([], [], 'b-', lw=1.25)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', bbox = {'facecolor' : 'white'}, transform=ax.transAxes)


""" Check that the calculation conserves total energy to within some tolerance """
EDRIFT = .05
E = calc_E(state)
if np.max(np.sum(np.abs(calc_E(y) - E))) > EDRIFT:
    sys.exit('Maximum energy drift of {} exceeded.'.format(EDRIFT))
print(E)


#This is here to create the trace line location for the middle and bottom point on the pendulum
trace_line_p1, = ax.plot([], [], 'r-', lw=.75)
trace_line_p1_x = []
trace_line_p1_y = []

trace_line_p2, = ax.plot([], [], 'w-', lw=.75)
trace_line_p2_x = []
trace_line_p2_y = []


def init():
    line.set_data([], [])
    trace_line_p1.set_data([], [])
    trace_line_p2.set_data([], [])
    time_text.set_text('')
    return line, time_text, trace_line_p1, trace_line_p2


def animate(i):
    #plot the adjusting corresponding points position through the animation
    #size of the point corresponds to the mass of the weights scaled to fit graphs
    c1 = plt.Circle((x1[i], y1[i]), M1/2, fc = 'b', zorder = 10)
    c2 = plt.Circle((x2[i], y2[i]), M2/2, fc = 'r', zorder = 10)
    patch_c1 = ax.add_patch(c1)
    patch_c2 = ax.add_patch(c2)

    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    trace_line_p1_x.append(x1[i])
    trace_line_p1_y.append(y1[i])

    trace_line_p2_x.append(x2[i])
    trace_line_p2_y.append(y2[i])

    line.set_data(thisx, thisy)
    trace_line_p1.set_data(trace_line_p1_x, trace_line_p1_y)
    trace_line_p2.set_data(trace_line_p2_x, trace_line_p2_y)
    
    time_text.set_text(time_template % (i*dt))
    return line, time_text, trace_line_p1, trace_line_p2, patch_c1, patch_c2

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
                              interval=25, blit=True, init_func=init)

# ani.save('double_pendulum.mp4', fps=15)
plt.show()
