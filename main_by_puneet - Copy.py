#modules, constants, functions:-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import functions
from functions import *
import time
import math
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
K=8.9975*(10**9)
G=6.67430*(10**(-11))


# #popup function
# def show_popup():
#     messagebox.showwarning("Input Value Error", "You have inserted wrong Value for either of number of particles, total time or dt time !!!")

# #getting values of coordiates, velocity, mass, charge
# def coordinates_velocity_mass_charge(n,i,mass_entry,charge_entry,x_coordinates_entry,y_coordinates_entry,z_coordinates_entry,x_velocity_entry,y_velocity_entry,z_velocity_entry):
#     m=float(mass_entry.get())
#     c=float(charge_entry.get())
#     x_c=float(x_coordinates_entry.get())
#     y_c=float(y_coordinates_entry.get())
#     z_c=float(z_coordinates_entry.get())
#     x_v=float(x_velocity_entry.get())
#     y_v=float(y_velocity_entry.get())
#     z_v=float(z_velocity_entry.get())

#     #opening file and checking how much content is written in it
#     with open ("input_initial_values.txt",'r') as file:file_content=file.readlines()
    
#     #updating file_content_new so that later it could be inserted into file
#     file_content.append("\n"+str(x_c)+","+str(y_c)+","+str(z_c)+","+str(c)+","+str(m))
#     file_content.append("\n"+str(x_v)+","+str(y_v)+","+str(z_v))

#     #uploading file content into actual file
#     with open("input_initial_values.txt",'w') as file:
#         file.writelines(file_content)

# #get calues of n, t, dt function 
# def get_values_and_insert_coordinates():
#     try:
        
#         #making variables for stroring n, t, dt
#         n=int(number_of_particle_entry.get())
#         t=int(total_time_entry.get())
#         dt=int(dt_entry.get())
        
#         #writting the content in file
#         with open("input_initial_values.txt",'w') as file:
#             file.write(str(n)+'\n'+str(t)+'\n'+str(dt))
        
#         # for i in range(0,n):
#         i=0    
#         while i<n:
#             #space label
#             space_label3=Label(root,text="-"*137)
#             space_label3.grid(row=5,column=0,columnspan=9)
#             space_label4=Label(root,text=" "*137)
#             space_label4.grid(row=7,column=0,columnspan=9)
#             space_label5=Label(root,text="-"*137)
#             space_label5.grid(row=11,column=0,columnspan=9)
            
#             #mass
#             mass_label=Label(root,text=f"Mass {i+1}")
#             mass_label.grid(column=1,row=6)
#             mass_entry=Entry(root,width=10)
#             mass_entry.grid(row=6,column=2)

#             #charge
#             charge_label=Label(root,text=f"Charge {i+1}")
#             charge_label.grid(row=6,column=3)
#             charge_entry=Entry(root,width=10)
#             charge_entry.grid(row=6,column=4)

#             #coordinates label
#             coordinates_label=Label(root,text=f"Coordinates {i+1}")
#             coordinates_label.grid(row=9,column=0)

#             #velocity label
#             velocity_label=Label(root,text=f"Velocity {i+1}")  
#             velocity_label.grid(row=9,column=3)

#             #  x,y,z for coordinates 
#             x_coordinates_label=Label(root,text="X- coord")
#             y_coordinates_label=Label(root,text="Y- coord")
#             z_coordinates_label=Label(root,text="Z- coord")
#             x_coordinates_label.grid(row=8,column=1)
#             y_coordinates_label.grid(row=9,column=1)
#             z_coordinates_label.grid(row=10,column=1)

#             # x,y,z for coordinates velocity
#             x_velocity_label=Label(root,text="X- coord")
#             y_velocity_label=Label(root,text="Y- coord")
#             z_velocity_label=Label(root,text="Z- coord")
#             x_velocity_label.grid(row=8,column=4)
#             y_velocity_label.grid(row=9,column=4)
#             z_velocity_label.grid(row=10,column=4)

#             #entry panel for coordinates
#             x_coordinates_entry=Entry(root,width=10)
#             y_coordinates_entry=Entry(root,width=10)
#             z_coordinates_entry=Entry(root,width=10)
#             x_coordinates_entry.grid(row=8,column=2)
#             y_coordinates_entry.grid(row=9,column=2)
#             z_coordinates_entry.grid(row=10,column=2)

#             #entry panel for velocity
#             x_velocity_entry=Entry(root,width=10)
#             y_velocity_entry=Entry(root,width=10)
#             z_velocity_entry=Entry(root,width=10)
#             x_velocity_entry.grid(row=8,column=5)
#             y_velocity_entry.grid(row=9,column=5)
#             z_velocity_entry.grid(row=10,column=5)

#             #button to except values of coordinates, mass, charge, velocity
#             coordinates_velocity_button=Button(root,text=f"Except the Values \n for particle {i+1}",command= lambda: coordinates_velocity_mass_charge(n,i,mass_entry,charge_entry,x_coordinates_entry,y_coordinates_entry,z_coordinates_entry,x_velocity_entry,y_velocity_entry,z_velocity_entry))
#             coordinates_velocity_button.grid(row=12,column=2,columnspan=2)
            
#             h=input()
#             #input panel to stop 
#             i=i+1
            
#     except ValueError:
#         show_popup()

# # main widget
# root=Tk()

# # icon widget
# root.iconbitmap("project icon.ico")

# # title widget
# root.title ("3-D Physics Simulator")

# # geometry of main widget
# root.geometry("700x300") 

# # image 
# image_path="project image.png"
# img=Image.open(image_path)
# img=img.resize((100,100))
# img=ImageTk.PhotoImage(img)
# image=Label(root,width=100,height=100,image=img)
# image.grid(row=0,column=2,columnspan=1)

# # Main Title
# Title=Label(root,text="    3-D  PHYSICS  SIMULATOR",font=("Times New Roman",16,"bold"))
# Title.grid(row=0,column=3,columnspan=4)

# #space label
# space_label1=Label(root,text="-"*137)
# space_label1.grid(row=1,column=0,columnspan=9)

# #number of particles and time.
# number_of_particle_label=Label(root,text="Number of Particles  ")
# number_of_particle_label.grid(row=2,column=0)
# total_time_label=Label(root,text="Total Time  ")
# total_time_label.grid(row=2,column=2)
# dt_label=Label(root,text="Fraction of 1s  ")
# dt_label.grid(row=2,column=4)

# #input panel for number of particles and time
# number_of_particle_entry=Entry(root, width=10)
# number_of_particle_entry.grid(row=2,column=1)
# total_time_entry=Entry(root,width=10)
# total_time_entry.grid(row=2,column=3)
# dt_entry=Entry(root,width=10)
# dt_entry.grid(row=2,column=5)

# #space label
# space_label2=Label(root,text="                                          ")
# space_label2.grid(row=3,column=0,columnspan=7)

# #buttton, getting number of particles, time, dt
# user_defined_coordinates=Button(root,text="Get Value and \nInsert Coordinates",command=get_values_and_insert_coordinates)
# user_defined_coordinates.grid(row=4,column=2)


# #root widget mainloop end
# root.mainloop()


with open("input_initial_values.txt")as file:
    file_content=file.readlines()
n=int(file_content[0])
t=float(file_content[1])
t1=float(file_content[2])
parameter=[]
velocity123=[]
for i in range(0,n):
    para=list(map(float,file_content[3+i*2].strip().split(",")))
    velo=list(map(float,file_content[4+i*2].strip().split(",")))
    parameter.append(para)
    velocity123.append(velo)


#time intervals
dt=(10**t1)**(-1)
t2=int(t/dt)

#array for parameters of n particles
parameters3d=np.zeros((t2+2,n,5))
velocity=np.zeros((t2+2,n,3)) 

#inputing initial dimension of n particles and initial velocity
parameters3d[0]=parameter
velocity[0]=velocity123

# introducing all arrays before initiating loop.
#distance
distance_array_3d=np.zeros((t2+1,n,n))
distance_cube_array_3d=np.zeros((t2+1,n,n))

#forces
electrostatic_force_4d=np.zeros((t2+1,3,n,n))
gravitational_force_4d=np.zeros((t2+1,3,n,n))
force_4d=np.zeros((t2+1,3,n,n))

electrostatic_force=np.zeros((t2+1,n,3))
gravitational_force=np.zeros((t2+1,n,3))
force=np.zeros((t2+1,n,3))

net_electrostatic_force=np.zeros((t2+1,n))
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
KE=np.zeros((t2+1,n))
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

start=time.time()

for a in range(0,t2+1):
   
    #distances
    #array storing distances of any particle with each particle
    vary_distance_array_3d=np.zeros((n,n))
    for i in range(0,n):
        for j in range(0,n):
            if i==j: 
                distance_array_3d[a][i][j]=0
            else:
                x=parameters3d[a][i][0]-parameters3d[a][j][0]
                y=parameters3d[a][i][1]-parameters3d[a][j][1]
                z=parameters3d[a][i][2]-parameters3d[a][j][2]
                d=((x**2)+(y**2)+(z**2))**(1/2)
                vary_distance_array_3d[i][j]=vary_distance_array_3d[j][i]=d
                distance_array_3d[a][i][j]=np.array(vary_distance_array_3d[i][j])
    #array storing cube of distances of any particle with each particle
    vary_distance_cube_array_3d=np.zeros((n,n))
    for i in range(0,n):
        for j in range(0,n):
            vary_distance_cube_array_3d[i][j]=(vary_distance_array_3d[i][j])**3
            distance_cube_array_3d[a][i][j]=vary_distance_cube_array_3d[i][j]

    #calculating force
    # arrays of electrostatic, gravitational, total force at each particle by each one of particle.
    vary_electrostatic_force_4d=np.zeros((3,n,n))
    vary_gravitational_force_4d=np.zeros((3,n,n))
    vary_force_4d=np.zeros((3,n,n))
    for j in range(0,3):
        for k in range(0,n):
            for l in range(0,n):
                if (distance_cube_array_3d[a][k][l])!=0:
                    vary_electrostatic_force_4d[j][k][l]=(K*parameters3d[a][k][3]*parameters3d[a][l][3]*(parameters3d[a][l][j]-parameters3d[a][k][j]))/(distance_cube_array_3d[a][k][l])
                    vary_gravitational_force_4d[j][k][l]=(G*parameters3d[a][k][4]*parameters3d[a][l][4]*(parameters3d[a][l][j]-parameters3d[a][k][j]))/(distance_cube_array_3d[a][k][l])
                    vary_force_4d[j][k][l]=vary_electrostatic_force_4d[j][k][l]+vary_gravitational_force_4d[j][k][l]
                else: 
                    vary_electrostatic_force_4d[j][k][l]=0
                    vary_gravitational_force_4d[j][k][l]=0
                    vary_force_4d[j][k][l]=0
    electrostatic_force_4d[a]=np.array(vary_electrostatic_force_4d)
    gravitational_force_4d[a]=np.array(vary_gravitational_force_4d)
    force_4d[a]=np.array(vary_force_4d)
    # making arrays of electrostatic, gravitational, total force at each particle by all particles agrigatedly.
    vary_electrostatic_force=np.zeros((3,n))
    vary_gravitational_force=np.zeros((3,n))
    vary_force=np.zeros((3,n))
    for i in range(0,3):
        vary_electrostatic_force[i]=np.sum(electrostatic_force_4d[a][i],axis=0)
        vary_gravitational_force[i]=np.sum(gravitational_force_4d[a][i],axis=0)
        vary_force[i]=np.sum(force_4d[a][i],axis=0)


    vary_electrostatic_force=np.transpose(vary_electrostatic_force)
    vary_gravitational_force=np.transpose(vary_gravitational_force)
    vary_force=np.transpose(vary_force)
    electrostatic_force[a]=vary_electrostatic_force
    gravitational_force[a]=vary_gravitational_force
    force[a]=vary_force
    #net electrostatic, graitational, total force on any particle.
    for j in range(0,n):
        net_e=0
        net_g=0
        net_t=0
        for k in range(0,3):
            net_e=net_e+((electrostatic_force[a][j][k])**2)
            net_g=net_g+((gravitational_force[a][j][k])**2)
            net_t=net_t+((force[a][j][k])**2)
        net_electrostatic_force[a][j]=(net_e)**(1/2)
        net_gravtational_force[a][j]=(net_g)**(1/2)
        net_force[a][j]=(net_t)**(1/2)

    #calculating velocities
    #creating array for holding velocities
    vary_velocity=np.zeros((n,3))

    #new velocity after force is applied for 10^(-t) seconds.
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

    #speed
    if (a<t2):
        #initial speed
        for i in range(0,n):
            s=0
            for j in range(0,3):
                s=s+(velocity[0][i][j]**2)
            speed[0][i]=s
        #finding speed of each particle
        vary_speed=np.zeros((n))
        for j in range(0,n):
            net_v=0
            for k in range(0,3):
                net_v=net_v+((velocity[a][j][k])**2)
            vary_speed[j]=(net_v)**(1/2)
        speed[a+1]=vary_speed
    else: break
    
    #linear momentum
    vary_linear_momentum=np.zeros((n))
    if (a<t2):
        for i in range(0,n):linear_momentum[0]=parameters3d[0][i][4]*speed[0][i]
        for j in range(0,n): vary_linear_momentum[j]=parameters3d[a][j][4]*speed[a][j]
        linear_momentum[a+1]=vary_linear_momentum
    else: break
    
    #KE
    if (a<t2):
        for j in range(0,n):KE[0][j]=((parameters3d[0][j][4]*(speed[0][j]**2))/2)
        for j in range(0,n):KE[a+1][j]=((parameters3d[a+1][j][4]*(speed[a+1][j]**2))/2)
    else: break

    #EPE
    #EPE of each particle at any instant duw to any other particle
    for j in range(0,n):
        for k in range(0,n):
            if (distance_array_3d[a][j][k]!=0):
                EPE_3d[a][j][k]=((K*parameters3d[a][j][3]*parameters3d[a][k][3])/distance_array_3d[a][j][k])
            else: 
                EPE_3d[a][j][k]=0
    #EPE of each particle due to all particles agrigately
    EPE_2d[a]=np.sum(EPE_3d[a],axis=0)


    #GPE
    #GPE of each particle at any istant due to any other particle
    for j in range(0,n):
        for k in range(0,n):
            if (distance_array_3d[a][j][k]!=0):
                GPE_3d[a][j][k]=((G*parameters3d[a][j][4]*parameters3d[a][k][4])/distance_array_3d[a][j][k])
            else: GPE_3d[a][j][k]=0
    #GPE of each particle due to all particles agrigately
    GPE_2d[a]=np.sum(GPE_3d[a],axis=0)

    print(f"hello{a}")

#extras
total_linear_momuntum=np.sum(linear_momentum,axis=1)
total_KE=np.sum(KE,axis=1)
EPE=np.sum(EPE_2d,axis=1)
GPE=np.sum(GPE_2d,axis=1)
TPE_2d=GPE_2d+EPE_2d
TPE=GPE+EPE
energy=TPE_2d+KE
total_energy=np.sum(energy,axis=1)

# time
end=time.time()
print("total time = ",end-start)
print("time for 1 iteration = ",(end-start)/(t2+1))

print("------------------------------------------------")

#calling graph drawing functions
# timeX=np.zeros(t2+1)   
# for i in range(0,t2+1): timeX[i]=i*dt
# force_plot(timeX, net_force,n)
# print(net_force)
# hello(n,parameters3d,t2)
# speed_plot(speed,dt,n,t2,t)
# linear_momentum_plot(linear_momentum,t2,dt,n,t)
# total_linear_momentum_plot(total_linear_momuntum,dt,t,t2)
# KE_plot(KE,t2,dt,t,n)
# total_KE_plot(total_KE,t2,dt,t)
# EPE_plot(t2,n,EPE_2d,dt,t)
# GPE_plot(t2,t,n,dt,GPE_2d)
# TPE_plot(dt,n,t,TPE_2d,t2)
# total_EPE_plot(EPE,t2,dt,t)
# total_GPE_plot(GPE,t2,dt,t)
# total_TPE_plot(TPE,t2,dt,t)
# energy_plot(energy,t2,n,t,dt)
# total_energy_plot(total_energy,t2,t,dt)
coordinates_plot(parameters3d,t2,n,t)
