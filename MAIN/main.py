# ========================================== Modules ==========================================

import tensorflow as tf
import math

# ========================================== Global Constants ==========================================

# Electrostatic Constant  /   Coulomb's Constant
K=8.9975*(10**9)

# Gravitational Constant
G=6.67430*(10**(-11))

# ========================================== Accessing File Content for Parameters ==========================================

with open("input.txt")as file:
    file_content=file.readlines()
n=int(file_content[0])
t=float(file_content[1])
t1=float(file_content[2])
parameter=[]
velocity123=[]
for i in range(0,n):
    para=list(map(float,file_content[4+i*3].strip().split(",")))
    velo=list(map(float,file_content[5+i*3].strip().split(",")))
    parameter.append(para)
    velocity123.append(velo)

# time intervals
dt = 10 ** (-1 * t1)
t2 = int (t / dt)

