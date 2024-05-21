#modules, constants, functions:-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
K=8.9975*(10**9)
G=6.67430*(10**(-11))

def force_plot(net_force,t2,n,dt,t):
    max=0
    min=0
    for i in range(0,t2+1):
        for j in range(0,n):
            if max<net_force[i][j]: max=net_force[i][j]
            if min>net_force[i][j]: min=net_force[i][j]
    alpha=((max-min)*5)/(t2+1)
    Color=["blue","red","green","black","magenta"]
    forceY=np.transpose(net_force)
    timeX=np.zeros(t2+1)
    for i in range(0,t2+1): timeX[i]=i*dt
    plt.xlabel("Time (s)")
    plt.ylabel("Force (N)")
    plt.title("Function line plot of each particle.")
    plt.xlim(0,t)
    plt.ylim(min-alpha,max+alpha)
    for i in range(0,n):
        plt.plot(timeX,forceY[i],label=f"particle {i}",color=Color[i])
    plt.legend()
    plt.show()

def coordinates_plot(parameters3d,t2,n,t):
    xmax=0
    xmin=0
    ymax=0
    ymin=0
    for i in range(0,t2+1):
        for j in range(0,n):
            if xmax<parameters3d[i][j][0]: xmax=parameters3d[i][j][0]
            if xmin>parameters3d[i][j][0]: xmin=parameters3d[i][j][0]
            if ymax<parameters3d[i][j][1]: ymax=parameters3d[i][j][1]
            if ymin>parameters3d[i][j][1]: ymin=parameters3d[i][j][1]          
    xalpha=((xmax-xmin)*5)/(t2+1)
    yalpha=((ymax-ymin)*5)/(t2+1)
    Color=["blue","red","green","black","magenta"]
    plt.xlabel("X coordinate")
    plt.ylabel("Y coordinate")
    plt.title("coordinates of each particle")
    plt.xlim(xmin-xalpha,xmax+xalpha)
    plt.ylim(ymin-yalpha,ymax+yalpha)
    X=np.zeros((n,t2+1))
    Y=np.zeros((n,t2+1))
    for i in range(0,t2+1):
        for j in range(0,n):
                X[j][i]=parameters3d[i][j][0]
                Y[j][i]=parameters3d[i][j][1]
    for j in range(0,n):
        plt.plot(X[j],Y[j],label=f"particle {j+1}",color=Color[j])
    plt.legend()
    plt.show()

def speed_plot(speed,dt,n,t2,t):
    max=0
    min=0
    for i in range(0,t2+1):
        for j in range(0,n):
            if max<speed[i][j]: max=speed[i][j]
            if min>speed[i][j]: min=speed[i][j]
    alpha=((max-min)*5)/(t2+1)
    Color=["blue","red","green","black","magenta"]
    speedY=np.transpose(speed)
    timeX=np.zeros(t2+1)
    for i in range(0,t2+1): timeX[i]=i*dt
    plt.xlabel("Time (s)")
    plt.ylabel("speed (N)")
    plt.title("speed line plot of each particle.")
    plt.xlim(0,t)
    plt.ylim(min-alpha,max+alpha)
    for i in range(0,n):
        plt.plot(timeX,speedY[i],label=f"particle {i+1}",color=Color[i])
    plt.legend()
    plt.show()

def TPE_plot(dt,n,t,TPE_2d,t2):
    max=0
    min=0
    for i in range(0,t2+1):
        for j in range(0,n):
            if max<TPE_2d[i][j]: max=TPE_2d[i][j]
            if min>TPE_2d[i][j]: min=TPE_2d[i][j]
    alpha=((max-min)*5)/(t2+1)
    Color=["blue","red","green","black","magenta"]
    TPE_2dY=np.transpose(TPE_2d)
    timeX=np.zeros(t2+1)
    for i in range(0,t2+1): timeX[i]=i*dt
    plt.xlabel("Time (s)")
    plt.ylabel("TPE (Joules)")
    plt.title("TPE line plot of each particle.")
    plt.xlim(0,t)
    plt.ylim(min-alpha,max+alpha)
    for i in range(0,n):
        plt.plot(timeX,TPE_2dY[i],label=f"particle {i+1}",color=Color[i])
    plt.legend()
    plt.show()

def total_TPE_plot(TPE,t2,dt,t):
    max=0
    min=0
    for i in range(0,t2+1):
        if max<TPE[i]: max=TPE[i]
        if min>TPE[i]: min=TPE[i]
    alpha=((max-min)*5)/(t2+1)
    Color=["blue","red","green","black","magenta"]
    timeX=np.zeros(t2+1)
    for i in range(0,t2+1): timeX[i]=i*dt
    plt.xlabel("Time (s)")
    plt.ylabel("Total KE ")
    plt.title("Total KE line plot")
    plt.xlim(0,t)
    plt.ylim(min-alpha,max+alpha)
    plt.plot(timeX,TPE,color="black")
    plt.legend()
    plt.show()

def energy_plot(energy,t2,n,t,dt):
    max=0
    min=0
    for i in range(0,t2+1):
        for j in range(0,n):
            if max<energy[i][j]: max=energy[i][j]
            if min>energy[i][j]: min=energy[i][j]
    alpha=((max-min)*5)/(t2+1)
    Color=["blue","red","green","black","magenta"]
    energyY=np.transpose(energy)
    timeX=np.zeros(t2+1)
    for i in range(0,t2+1): timeX[i]=i*dt
    plt.xlabel("Time (s)")
    plt.ylabel(" (Joules)")
    plt.title("Energy line plot of each particle.")
    plt.xlim(0,t)
    plt.ylim(min-alpha,max+alpha)
    for i in range(0,n):
        plt.plot(timeX,energyY[i],label=f"particle {i+1}",color=Color[i])
    plt.legend()
    plt.show()

def total_energy_plot(total_energy,t2,t,dt):
    max=0
    min=0
    for i in range(0,t2+1):
        if max<total_energy[i]: max=total_energy[i]
        if min>total_energy[i]: min=total_energy[i]
    alpha=((max-min)*5)/(t2+1)
    Color=["blue","red","green","black","magenta"]
    timeX=np.zeros(t2+1)
    for i in range(0,t2+1): timeX[i]=i*dt
    plt.xlabel("Time (s)")
    plt.ylabel("Total Energy (Joules) ")
    plt.title("Total energy line plot")
    plt.xlim(0,t)
    plt.ylim(min-alpha,max+alpha)
    plt.plot(timeX,total_energy,color="black")
    plt.legend()
    plt.show()

def cros_product(a,b):
        c=np.zeros(3)
        c[0]=((a[1]*b[2])-(a[2]*b[1]))
        c[1]=((a[2]*b[0])-(a[0]*b[2]))
        c[2]=((a[0]*b[1])-(a[1]*b[0]))
        return c

def KE_plot(KE,t2,dt,t,n):
    max=0
    min=0
    for i in range(0,t2+1):
        for j in range(0,n):
            if max<KE[i][j]: max=KE[i][j]
            if min>KE[i][j]: min=KE[i][j]
    alpha=((max-min)*5)/(t2+1)
    Color=["blue","red","green","black","magenta"]
    KEY=np.transpose(KE)
    timeX=np.zeros(t2+1)
    for i in range(0,t2+1): timeX[i]=i*dt
    plt.xlabel("Time (s)")
    plt.ylabel("KE (Joules)")
    plt.title("KE line plot of each particle.")
    plt.xlim(0,t)
    plt.ylim(min-alpha,max+alpha)
    for i in range(0,n):
        plt.plot(timeX,KEY[i],label=f"particle {i+1}",color=Color[i])
    plt.legend()
    plt.show()

def total_KE_plot(total_KE,t2,dt,t):
    max=0
    min=0
    for i in range(0,t2+1):
        if max<total_KE[i]: max=total_KE[i]
        if min>total_KE[i]: min=total_KE[i]
    alpha=((max-min)*5)/(t2+1)
    Color=["blue","red","green","black","magenta"]
    timeX=np.zeros(t2+1)
    for i in range(0,t2+1): timeX[i]=i*dt
    plt.xlabel("Time (s)")
    plt.ylabel("Total KE ")
    plt.title("Total KE line plot")
    plt.xlim(0,t)
    plt.ylim(min-alpha,max+alpha)
    plt.plot(timeX,total_KE,color="black")
    plt.legend()
    plt.show()