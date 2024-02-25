#mass, charge, coordinates, velocity 
# module and imports
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import numpy as np
print("hello")
#change particle


#popup function
def show_popup():
    messagebox.showwarning("Input Value Error", "You have inserted wrong Value for either of number of particles, total time or dt time !!!")

#getting values of coordiates, velocity, mass, charge
def coordinates_velocity_mass_charge(n,i,mass_entry,charge_entry,x_coordinates_entry,y_coordinates_entry,z_coordinates_entry,x_velocity_entry,y_velocity_entry,z_velocity_entry):
    m=int(mass_entry.get())
    c=int(charge_entry.get())
    x_c=int(x_coordinates_entry.get())
    y_c=int(y_coordinates_entry.get())
    z_c=int(z_coordinates_entry.get())
    x_v=int(x_velocity_entry.get())
    y_v=int(y_velocity_entry.get())
    z_v=int(z_velocity_entry.get())
    
    
    #making appropriates arrays to store coordinates, velocity and mass, charge
    coordinates=np.zeros((n,3))
    velocities=np.zeros((n,3))
    parameter_=np.zeros((n,2))
    
    #feeding each of the abovwe value into suitable list
    coordinates[i][0],coordinates[i][1],coordinates[i][2]=x_c,y_c,z_c
    velocities[i][0],velocities[i][1],velocities[i][2]=x_v,y_v,z_v
    parameter_[i][0],parameter_[i][1]=m,c

    #opening file and checking how much content is written in it
    with open ("input_initial_values.txt",'r') as file:
            file_content=file.readlines()
            if len(file_content)==8:None
            else: file_content=file_content+["","\n","\n","\n"]
    
    #updating file_content_new so that later it could be inserted into file
    if i<n-1:
        file_content[4]=file_content[4]+str(parameter_[i][0])+','
        file_content[5]=file_content[5]+str(parameter_[i][1])+','
        file_content[6]=file_content[6]+str(coordinates[i][0])+','+str(coordinates[i][1])+','+str(coordinates[i][2])+';'
        file_content[7]=file_content[7]+str(velocities[i][0])+','+str(velocities[i][1])+','+str(velocities[i][2])+';'
    else: 
        file_content[4]=file_content[4]+str(parameter_[i][0])
        file_content[5]=file_content[5]+str(parameter_[i][1])
        file_content[6]=file_content[6]+str(coordinates[i][0])+','+str(coordinates[i][1])+','+str(coordinates[i][2])
        file_content[7]=file_content[7]+str(velocities[i][0])+','+str(velocities[i][1])+','+str(velocities[i][2])
    
    #uploading file content into actual file
    with open("input_initial_values.txt",'w') as file:
        file.writelines(file_content)

#get calues of n, t, dt function 
def get_values_and_insert_coordinates():
    try:
        
        #making variables for stroring n, t, dt
        n=int(number_of_particle_entry.get())
        t=int(total_time_entry.get())
        dt=int(dt_entry.get())
        
        #writting the content in file
        with open("input_initial_values.txt",'w') as file:
            file.write("1"+"\n"+str(n)+'\n'+str(t)+'\n'+str(dt)+"\n")
        
        # for i in range(0,n):
        i=0    
        while i<n:
            #space label
            space_label3=Label(root,text="-"*137)
            space_label3.grid(row=5,column=0,columnspan=9)
            space_label4=Label(root,text=" "*137)
            space_label4.grid(row=7,column=0,columnspan=9)
            space_label5=Label(root,text="-"*137)
            space_label5.grid(row=11,column=0,columnspan=9)
            
            #mass
            mass_label=Label(root,text=f"Mass {i+1}")
            mass_label.grid(column=1,row=6)
            mass_entry=Entry(root,width=10)
            mass_entry.grid(row=6,column=2)

            #charge
            charge_label=Label(root,text=f"Charge {i+1}")
            charge_label.grid(row=6,column=3)
            charge_entry=Entry(root,width=10)
            charge_entry.grid(row=6,column=4)

            #coordinates label
            coordinates_label=Label(root,text=f"Coordinates {i+1}")
            coordinates_label.grid(row=9,column=0)

            #velocity label
            velocity_label=Label(root,text=f"Velocity {i+1}")  
            velocity_label.grid(row=9,column=3)

            #  x,y,z for coordinates 
            x_coordinates_label=Label(root,text="X- coord")
            y_coordinates_label=Label(root,text="Y- coord")
            z_coordinates_label=Label(root,text="Z- coord")
            x_coordinates_label.grid(row=8,column=1)
            y_coordinates_label.grid(row=9,column=1)
            z_coordinates_label.grid(row=10,column=1)

            # x,y,z for coordinates velocity
            x_velocity_label=Label(root,text="X- coord")
            y_velocity_label=Label(root,text="Y- coord")
            z_velocity_label=Label(root,text="Z- coord")
            x_velocity_label.grid(row=8,column=4)
            y_velocity_label.grid(row=9,column=4)
            z_velocity_label.grid(row=10,column=4)

            #entry panel for coordinates
            x_coordinates_entry=Entry(root,width=10)
            y_coordinates_entry=Entry(root,width=10)
            z_coordinates_entry=Entry(root,width=10)
            x_coordinates_entry.grid(row=8,column=2)
            y_coordinates_entry.grid(row=9,column=2)
            z_coordinates_entry.grid(row=10,column=2)

            #entry panel for velocity
            x_velocity_entry=Entry(root,width=10)
            y_velocity_entry=Entry(root,width=10)
            z_velocity_entry=Entry(root,width=10)
            x_velocity_entry.grid(row=8,column=5)
            y_velocity_entry.grid(row=9,column=5)
            z_velocity_entry.grid(row=10,column=5)

            #button to except values of coordinates, mass, charge, velocity
            coordinates_velocity_button=Button(root,text=f"Except the Values \n for particle {i+1}",command= lambda: coordinates_velocity_mass_charge(n,i,mass_entry,charge_entry,x_coordinates_entry,y_coordinates_entry,z_coordinates_entry,x_velocity_entry,y_velocity_entry,z_velocity_entry))
            coordinates_velocity_button.grid(row=12,column=2,columnspan=2)
            
            h=input()
            #input panel to stop 
            i=i+1
            
            
    except ValueError:
        show_popup()

#get values of n, t, dt        
def get_values_and_get_random_coordinates():
    try:    
        
        #making variables for stroring n, t, dt
        n=int(number_of_particle_entry.get())
        t=int(total_time_entry.get())
        dt=int(dt_entry.get())
        
        #writting the content in file
        with open("input_initial_values.txt",'w') as file:
            file.write("2"+"\n"+str(n)+'\n'+str(t)+'\n'+str(dt)+'\n')
        
        #finding random coordinates, mass, charge, and velocity
        coordinates=np.zeros((n,3))
        velocities=np.zeros((n,3))
        parameter_=np.zeros((n,2))
        for i in range(0,n):
            for j in range(0,3):
                coordinates[i][j]=random.uniform(-100,100)
                velocities[i][j]=random.uniform(-100,100)
            parameter_[i][0]=random.uniform(0,10)
            parameter_[i][1]=random.uniform(-1,1)
        
        #opening file and checking how much content is written in it
        with open ("input_initial_values.txt",'r') as file:
                file_content=file.readlines()
                if len(file_content)==8:None
                else: file_content=file_content+["","\n","\n","\n"]

        #appending file content
        for i in range(0,n):
            if i<n-1:
                file_content[4]=file_content[4]+str(parameter_[i][0])+','
                file_content[5]=file_content[5]+str(parameter_[i][1])+','
                file_content[6]=file_content[6]+str(coordinates[i][0])+','+str(coordinates[i][1])+','+str(coordinates[i][2])+';'
                file_content[7]=file_content[7]+str(velocities[i][0])+','+str(velocities[i][1])+','+str(velocities[i][2])+';'
            else: 
                file_content[4]=file_content[4]+str(parameter_[i][0])
                file_content[5]=file_content[5]+str(parameter_[i][1])
                file_content[6]=file_content[6]+str(coordinates[i][0])+','+str(coordinates[i][1])+','+str(coordinates[i][2])
                file_content[7]=file_content[7]+str(velocities[i][0])+','+str(velocities[i][1])+','+str(velocities[i][2])
            
        #uploading file content into actual file
        with open("input_initial_values.txt",'w') as file:
            file.writelines(file_content)

    except ValueError:
        show_popup()

# main widget
root=Tk()

# icon widget
root.iconbitmap("project icon.ico")

# title widget
root.title ("3-D Physics Simulator")

# geometry of main widget
root.geometry("700x300") 

# image 
image_path="project image.png"
img=Image.open(image_path)
img=img.resize((100,100))
img=ImageTk.PhotoImage(img)
image=Label(root,width=100,height=100,image=img)
image.grid(row=0,column=2,columnspan=1)

# Main Title
Title=Label(root,text="    3-D  PHYSICS  SIMULATOR",font=("Times New Roman",16,"bold"))
Title.grid(row=0,column=3,columnspan=4)

#space label
space_label1=Label(root,text="-"*137)
space_label1.grid(row=1,column=0,columnspan=9)

#number of particles and time.
number_of_particle_label=Label(root,text="Number of Particles  ")
number_of_particle_label.grid(row=2,column=0)
total_time_label=Label(root,text="Total Time  ")
total_time_label.grid(row=2,column=2)
dt_label=Label(root,text="Fraction of 1s  ")
dt_label.grid(row=2,column=4)

#input panel for number of particles and time
number_of_particle_entry=Entry(root, width=10)
number_of_particle_entry.grid(row=2,column=1)
total_time_entry=Entry(root,width=10)
total_time_entry.grid(row=2,column=3)
dt_entry=Entry(root,width=10)
dt_entry.grid(row=2,column=5)

#space label
space_label2=Label(root,text="                                          ")
space_label2.grid(row=3,column=0,columnspan=7)

#buttton, getting number of particles, time, dt
user_defined_coordinates=Button(root,text="Get Value and \nInsert Coordinates",command=get_values_and_insert_coordinates)
user_defined_coordinates.grid(row=4,column=2)
random_coordinates=Button(root,text="Get Values and Insert \nRandom Coordinates",command=get_values_and_get_random_coordinates)
random_coordinates.grid(row=4,column=3)

#root widget mainloop end
root.mainloop()

#writting file content back into new arrays.
with open("input_initial_values.txt","r") as file:
    file_lines=file.readlines()
mass=file_lines[4].split(',')
charge=file_lines[5].split(',')
xyz_coordinates_together=file_lines[6].split(';')
xyz_velocities_together=file_lines[7].split(';')
for i in range(0,len(mass)):
    xyz_coordinates=np.zeros((len(mass)))
    xyz_velocities=np.zeros((len(mass)))
    xyz_velocities[i]=xyz_velocities_together[i].split(',')
    xyz_coordinates[i]=xyz_coordinates_together[i].split(',')
for i in range (0,len(mass)):
    for j in range(0,3):
        xyz_coordinates[i][j]=int(xyz_coordinates[i][j])
        xyz_velocities[i][j]=int(xyz_velocities[i][j])
for i in range (0,len(mass)):
    mass[i]=int(mass[i])
    charge[i]=int(charge[i])
n=int(file_lines[1])
t=int(file_lines[2])
dt=int(file_lines[3])
parameter_3d=np.zeros((n,5))
velocity_3d=np.zeros((n,5))
for i in range (0,n):
    for j in range(0,5):
        parameter_3d[i][j]=xyz_coordinates[i][j]
        velocity_3d=[i][j]=xyz_velocities[i][j]
print(parameter_3d)
print(velocity_3d)