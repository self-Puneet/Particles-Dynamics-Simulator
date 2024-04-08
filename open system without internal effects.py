#modules, constants, functions:-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
from functions import *
import time
K=8.9975*(10**9)
G=6.67430*(10**(-11))
from math import *

# testing my model
# F=[4*sin(5*x)+6,5*sin(6*y)+7,6*sin(7*z)+8]

#number of particles
n=int(input("numbers of particles= "))

#radius of particles
r=0.001

#wall equation
area_vector=input("enter area vector of wall: ")
area_vector=eval(area_vector)
point_on_plane=input("enter point on plane: ")
point_on_plane=eval(point_on_plane)
magnitude_of_area_vector=((area_vector[0]**2)+(area_vector[1]**2)+(area_vector[2]**2))**(1/2)

#time intervals
t=float(input("desired time= "))
t1=int(input("enter t for 10^t wehre 10^t is division of 1 sec= "))
dt=(10**t1)**(-1)
t2=int(t/dt)

#array for parameters of n particles
parameters3d=np.zeros((t2+2,n,5))
velocity=np.zeros((t2+2,n,3))

#inputing initial dimension of n particles
parameters=[]
for ab in range(0,n):
    str = input(f"\t\tEnter dimensionas of particle {ab+1}: ")
    list1=eval(str)
    parameters.append(list1)
parameters3d[0]=parameters

#inputing velocities of particles
velocity2d=[]
for ab in range(0,n):
    str=input(f"\t\t\tvelocity of particle {ab+1}:")
    list2=eval(str)
    velocity2d.append(list2)
velocity[0]=velocity2d

#inputing coordinates of random point
str=input("\t\t\tcoordinate of random point: ")
random_point=eval(str)

#introduction of all array before initiating loop.

#force- 3D
electromagnetic_force=np.zeros((t2+1,n,3))
gravitational_force=np.zeros((t2+1,n,3))
force=np.zeros((t2+1,n,3))

#force- 2D
net_electromagnetic_force=np.zeros((t2+1,n))
net_gravtational_force=np.zeros((t2+1,n))
net_force=np.zeros((t2+1,n))

#speed and linear momentum
speed=np.zeros((t2+1,n))
linear_momentum=np.zeros((t2+1,n))
total_linear_momuntum=np.zeros((t2+1))

#displacement
displacement_3d=np.zeros((t2+1,n,3))
displacement=np.zeros((n,3))

#energy
KE = np.zeros((t2+1,n))
total_KE=np.zeros(t2+1)
EPE_3d=np.zeros((t2+1,n,n))
EPE_2d=np.zeros((t2+1,n))
EPE=np.zeros((t2+1))
GPE_3d=np.zeros((t2+1,n,n))
GPE_2d=np.zeros((t2+1,n))
GPE=np.zeros((t2+1))
TPE_2d=np.zeros((t2+1,n))
TPE=np.zeros((t2+1))
energy=np.zeros((t2+1,n))
total_energy=np.zeros((t2+1))

#angular momentum
angular_momentum_3d=np.zeros((t2+1,n,3))
angular_momentum_2d=np.zeros((t2+1,n))
vector_angular_momentum_1d=np.zeros((t2+1,3))
angular_momentum_1d=np.zeros((t2+1))
distance_vector_random=np.zeros((t2+1,n,3))

#torque
torque=np.zeros((t2+1,n,3))
net_torque=np.zeros((t2+1,n))
torque_2d=np.zeros((t2+1,3))
torque_1d=np.zeros((t2+1))

start=time.time()

for a in range(0,t2+1):

    #calculating distance of each particle at each instant from choosen line
    for i in range(0,n):
        if (condition_for_approching_particle(n,a,velocity,area_vector) is True):
            wer=distance_of_particle_from_wall(area_vector,parameters3d,point_on_plane,magnitude_of_area_vector,a,n)
            if (wer<0.00001):
                qwe=new_velocity_after_collision_fo_wall(a,n,velocity,area_vector,e)
                for j in range(0,3):
                    velocity[t][n][j]=qwe[j]

    #calculating force
    #force-3D
    for i in range(0,n):
        force[a][i][0]=1*sin(2*parameters3d[a][i][0])+2
        force[a][i][1]=2*sin(3*parameters3d[a][i][1])+3
        force[a][i][2]=3*sin(4*parameters3d[a][i][2])+4
    #force- 2D
    for i in range(0,n):
        s1=0
        for j in range(0,3):
            s1=s1+force[a][i][j]**2
        net_force[a][i]=s1**(1/2)
    
    #calculating velocities
    #creating array for holding velocities
    vary_velocity=np.zeros((n,3))

    #new velociyty after force is applied for 10^(-t) seconds.
    if (a<t2):
        for j in range(0,n):
            for k in range (0,3):
                vary_velocity[j][k]=velocity[a][j][k]+((force[a][j][k]*dt)/parameters3d[a][j][4])
        velocity[a+1]=vary_velocity
    else: break

    #displacement determination
    #making an array for storing displacement
    vary_displacement_3d=np.zeros((n,3))
    if (a<t2):
        #evaluating displacement
        for j in range(0,n):
            for k in range(0,3):
                if (parameters3d[a][j][4]!=0): vary_displacement_3d[j][k]=(velocity[a][j][k]*dt)+((force[a][j][k]*dt*dt)/(2*parameters3d[a][j][4]))
                else: vary_displacement_3d[j][k]=0
        #storing evaluated displacement
        displacement_3d[a+1]=vary_displacement_3d
    else: break

    #editing dimensions:-
    if (a<t2):
        for i in range(0,n):
            for j in range(0,3):
                parameters3d[a+1][i][j]=parameters3d[a][i][j]+displacement_3d[a+1][i][j]
    else: break

    #keeping mass and charge constant
    if (a<t2):
        for i in range(0,n):
            parameters3d[a+1][i][3]=parameters3d[a][i][3]
            parameters3d[a+1][i][4]=parameters3d[a][i][4]
    else: break

    print(f"hello{a}")

mid=time.time()
print("total time in loop = ",mid-start)
print("time for 1 iteration = ",(mid-start)/(n*(t2+1)))

# force_plot(net_force,t2,n,dt,t)
# coordinates_plot(parameters3d,t2,n,t)