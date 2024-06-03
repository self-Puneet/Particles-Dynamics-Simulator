# ========================================== Modules ==========================================

import tensorflow as tf
import math

# ========================================== Global Constants ==========================================

# Electrostatic Constant  /   Coulomb's Constant
K=8.9975*(10**9)

# Gravitational Constant
G=6.67430*(10**(-11))

# ========================================== Accessing File Content for Parameters ==========================================

with open("MAIN\input.txt")as file:
    file_content=file.readlines()
n = int(file_content[0])
t = float(file_content[1])
t1 = float(file_content[2])
parameter = []
velocity = []
for i in range(0,n):
    para = list(map(float, file_content[4 + i*3].strip().split(",")))
    velo = list(map(float, file_content[5 + i*3].strip().split(",")))
    parameter.append(para)
    velocity.append(velo)

# time intervals
dt = 10 ** (-1 * t1)
t2 = int (t / dt)

# ========================================== All Tensors ==========================================

Parameter = tf.Variable(tf.zeros([t2 + 1, n, 5]))
Velocity = tf.Variable(tf.zeros([t2 + 1, n, 3]))
Distance = tf.Variable(tf.zeros([t2, n, n]))

Electrostatic_Force_Vector_4D = tf.Variable(tf.zeros([t2, 3, n, n]))
Gravitational_Force_vector_4D = tf.Variable(tf.zeros([t2, 3, n, n]))
Force_Vector_4D = tf.Variable(tf.zeros([t2, 3, n, n]))

Electrostatic_Force_Vector = tf.Variable(tf.zeros([t2, n, 3]))
Gravitational_Force_Vector = tf.Variable(tf.zeros([t2, n, 3]))
Force_Vector = tf.Variable(tf.zeros([t2, n, 3]))

Electrostatic_Force_Resultant = tf.Variable(tf.zeros([t2, n]))
Gravitational_Force_Resultant = tf.Variable(tf.zeros([t2, n]))
Force_Resultant = tf.Variable(tf.zeros([t2, n]))

Displacement = tf.Variable(tf.zeros([t2 + 1, n, 3]))


Parameter[0].assign(tf.convert_to_tensor(parameter, dtype=tf.float32))
Velocity[0].assign(tf.convert_to_tensor(velocity, dtype=tf.float32))

# ========================================== Main Loop ==========================================

for it in range(0, t2):

    # Distance
    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                x = Parameter[it, i, 0] - Parameter[it, j, 0]
                y = Parameter[it, i, 1] - Parameter[it, j, 1]
                z = Parameter[it, i, 2] - Parameter[it, j, 2]
                dist = tf.sqrt((x ** 2) + (y ** 2) + (z ** 2))
                Distance[it, i, j].assign(dist)

    # Force
    for i in range(0, 3):
        for j in range(0, n):
            for k in range(0, n):
                if Distance[it, j, k] != 0:
                    elec = K * Parameter[it, j, 3] * Parameter[it, k, 3] * (Parameter[it, k, i] - Parameter[it, j, i]) / (Distance[it, j, k] ** 3)
                    grav = G * Parameter[it, j, 4] * Parameter[it, k, 4] * (Parameter[it, k, i] - Parameter[it, j, i]) / (Distance[it, j, k] ** 3)
                    Electrostatic_Force_Vector_4D[it, i, j, k].assign(elec)
                    Gravitational_Force_vector_4D[it, i, j, k].assign(grav)

    for i in range(0, 3):
        for j in range(0, n):
            sum1 = 0
            sum2 = 0
            for k in range(0, n):
                sum1 += Electrostatic_Force_Vector_4D[it, i, j, k]
                sum2 += Gravitational_Force_vector_4D[it, i, j, k]
            Electrostatic_Force_Vector[it, j, i].assign(sum1)
            Gravitational_Force_Vector[it, j, i].assign(sum2)
    

    for i in range(0, n):
        val1 = math.sqrt((Electrostatic_Force_Vector[it, i, 0] ** 2) + (Electrostatic_Force_Vector[it, i, 1] ** 2) + (Electrostatic_Force_Vector[it, i, 2] ** 2))
        val2 = math.sqrt((Gravitational_Force_Vector[it, i, 0] ** 2) + (Gravitational_Force_Vector[it, i, 1] ** 2) + (Gravitational_Force_Vector[it, i, 2] ** 2))
        Electrostatic_Force_Resultant[it, i].assign(val1)
        Gravitational_Force_Resultant[it, i].assign(val2)
    Force_Resultant = Electrostatic_Force_Resultant + Gravitational_Force_Resultant

    # Velocity
    for i in range(0, n):
        for j in range(0, 3):
            vel = Velocity[it, i, j] + (Force_Vector[it, i, j] * dt / Parameter[it, i, 4])
            Velocity[it + 1, i, j].assign(vel)

    # Displacement
    for i in range(0, n):
        for j in range(0, 3):
            if Parameter[it, i, 4] != 0:
                dis = (Velocity[it, i, j] * dt) + (0.5 * Force_Vector[it, i, j] * dt / Parameter[it, i, 4])
                Displacement[it + 1, i, j].assign(dis)

    # Editing Dimensions
    for i in range(0,n):
        for j in range(0,3):
            new_parameter = Parameter[it, i, j] + Displacement[it + 1, i, j]
            Parameter[it + 1, i, j].assign(new_parameter)
        Parameter[it + 1, i, 3].assign(Parameter[it, i, 3])
        Parameter[it + 1, i, 4].assign(Parameter[it, i, 4])
    print(f"hello{it}")