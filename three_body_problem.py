import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation
from math import sqrt

step = 40000
t = np.linspace(0, 5000, step)

m1 = 5
m2 = 5
m3 = 5
G = 10

initial_position_1 = np.array([-5., -4., 4.])
initial_position_2 = np.array([0., -3., 5.5])
initial_position_3 = np.array([3, 5., 2.5])

velocity_array_1 = []
velocity_array_2 = []
velocity_array_3 = []

initial_velocity_1 = np.array([.3, 0, 0])
initial_velocity_2 = np.array([0, .2, 0])
initial_velocity_3 = np.array([0, 0, -.1])

velocity_array_1.append(initial_velocity_1)
velocity_array_2.append(initial_velocity_2)
velocity_array_3.append(initial_velocity_3)

position_array_1 = []
position_array_2 = []
position_array_3 = []
position_array_1.append(initial_position_1)
position_array_2.append(initial_position_2)
position_array_3.append(initial_position_3)



for i in range(step):
    
    # WRONG NORMALIZATION;
    
    threshold = 0.2
    
    r_1_2_diff = (position_array_1[i] - position_array_2[i])
    r_1_2 = pow(sqrt(pow(r_1_2_diff[0], 2) + pow(r_1_2_diff[1], 2) + pow(r_1_2_diff[2], 2)), 3)
    r_1_3_diff = (position_array_1[i] - position_array_3[i])
    r_1_3 = pow(sqrt(pow(r_1_3_diff[0], 2) + pow(r_1_3_diff[1], 2) + pow(r_1_3_diff[2], 2)), 3)
    
    
    r12 = np.power(abs(position_array_1[i] - position_array_2[i]), 3)
    r13 = np.power(abs(position_array_1[i] - position_array_3[i]), 3)
    


    a1 = (-G * m2) * (position_array_1[i] - position_array_2[i]) / r_1_2 - (G * m3) * (position_array_1[i] - position_array_3[i]) / r_1_3
    # edge case;    
    if (r_1_2 <= threshold or r_1_3 <= threshold):
        a1 = 0
    #if (r12[0] < threshold or r12[1] < threshold or r12[2] < threshold or r13[0] < threshold or r13[1] < threshold or r13[2] < threshold):
    #    a1 = 0
    
    
    
    r_2_1_diff = (position_array_2[i] - position_array_1[i])
    r_2_1 = pow(sqrt(pow(r_2_1_diff[0], 2) + pow(r_2_1_diff[1], 2) + pow(r_2_1_diff[2], 2)), 3)
    r_2_3_diff = (position_array_2[i] - position_array_3[i])
    r_2_3 = pow(sqrt(pow(r_2_3_diff[0], 2) + pow(r_2_3_diff[1], 2) + pow(r_2_3_diff[2], 2)), 3)
    
    
    r21 = np.power(abs(position_array_2[i] - position_array_1[i]), 3)
    r23 = np.power(abs(position_array_2[i] - position_array_3[i]), 3)


    
    a2 = (-G * m1) * (position_array_2[i] - position_array_1[i]) / r_2_1 - (G * m3) * (position_array_2[i] - position_array_3[i]) / r_2_3
    # edge case;
    if (r_2_1 <= threshold or r_2_3 <= threshold):
        a2 = 0
    #if (r21[0] < threshold or r21[1] < threshold or r21[2] < threshold or r23[0] < threshold or r23[1] < threshold or r23[2] < threshold):
    #    a2 = 0
    
        
        
    r_3_1_diff = (position_array_3[i] - position_array_1[i])
    r_3_1 = pow(sqrt(pow(r_3_1_diff[0], 2) + pow(r_3_1_diff[1], 2) + pow(r_3_1_diff[2], 2)), 3)
    r_3_2_diff = (position_array_3[i] - position_array_2[i])
    r_3_2 = pow(sqrt(pow(r_3_2_diff[0], 2) + pow(r_3_2_diff[1], 2) + pow(r_3_2_diff[2], 2)), 3)
    
    
    r31 = np.power(abs(position_array_3[i] - position_array_1[i]), 3)
    r32 = np.power(abs(position_array_3[i] - position_array_2[i]), 3)
    
        
    a3 = (-G * m3) * (position_array_3[i] - position_array_1[i]) / r_3_1 - (G * m2) * (position_array_3[i] - position_array_2[i]) / r_3_2   
    
    # edge case;
    if (r_3_1 <= threshold or r_3_2 <= threshold):
        #a3 = (-G * m1) * (position_array_3[i] - position_array_1[i]) / 1 - (G * m2) * (position_array_3[i] - position_array_2[i]) / 1  
        a3 = 0
    #if (r31[0] < threshold or r31[1] < threshold or r31[2] < threshold or r32[0] < threshold or r32[1] < threshold or r32[2] < threshold):
    #    a3 = 0
    
        
        
        
    time = 1. / 500
    
    v1_new = velocity_array_1[i] + a1 * time
    v2_new = velocity_array_2[i] + a2 * time
    v3_new = velocity_array_3[i] + a3 * time
    
    #print(v1_new)
    
    
    velocity_array_1.append(v1_new)
    velocity_array_2.append(v2_new)
    velocity_array_3.append(v3_new)
    
    x1_new = position_array_1[i] + velocity_array_1[i] * time + 1./2 * a1 * time * time
    x2_new = position_array_2[i] + velocity_array_2[i] * time + 1./2 * a2 * time * time
    x3_new = position_array_3[i] + velocity_array_3[i] * time + 1./2 * a3 * time * time

    
    
    
    position_array_1.append(x1_new)
    position_array_2.append(x2_new)
    position_array_3.append(x3_new)
    
positions = np.asarray([position_array_1, position_array_2, position_array_3])
    
    
#print(velocity_array_1)
print(positions)


                  

# Set up figure & 3D axis for animation
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1], projection='3d')
ax.axis('off')

# choose a different color for each trajectory
colors = plt.cm.jet(np.linspace(0, 1, 3))

# set up lines and points
lines = sum([ax.plot([], [], [], '-', c=c)
             for c in colors], [])
pts = sum([ax.plot([], [], [], 'o', c=c)
           for c in colors], [])

# prepare the axes limits
ax.set_xlim((-15, 15))
ax.set_ylim((-15, 15))
ax.set_zlim((-15, 15))

# set point-of-view: specified by (altitude degrees, azimuth degrees)
ax.view_init(30, 0)

# initialization function: plot the background of each frame
def init():
    for line, pt in zip(lines, pts):
        line.set_data([], [])
        line.set_3d_properties([])

        pt.set_data([], [])
        pt.set_3d_properties([])
    return lines + pts

# animation function.  This will be called sequentially with the frame number
def animate(i):
    
    # we'll step two time-steps per frame.  This leads to nice results.
    i = (i * 25) % step

    for line, pt, xi in zip(lines, pts, positions):
        x, y, z = xi[:i].T
        line.set_data(x, y)
        line.set_3d_properties(z)

        pt.set_data(x[-1:], y[-1:])
        pt.set_3d_properties(z[-1:])

    #ax.view_init(20, 0.05 * i)
    fig.canvas.draw()
    return lines + pts

# instantiate the animator.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1000, interval=30, blit=False)
plt.show()