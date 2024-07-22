# ========================================== Modules ==========================================

import tensorflow as tf
import numpy as np
import time

# ========================================== Global Constants ==========================================

# Electrostatic Constant  /   Coulomb's Constant
K = 8.9975 * (10 ** 9)

# Gravitational Constant
G = 6.67430 * (10 ** (-11))

# ========================================== Accessing File Content for Parameters ==========================================

n = 2
t1 = 4
t = 3
dt = 10 ** (-t1)
t2 = int(t / dt)

parameter = np.array([
    [0.0, 0.0, 0.0, -1e-05, 1.0],
    [1.0, 0.0, 0.0, 1e-05, 1.0]
], dtype=np.float32)

velocity = np.array([
    [0.0, -6.7, 10.0],
    [0.0, 6.7, 10.0]
], dtype=np.float32)


# ========================================== All Tensors ==========================================

Parameter = tf.Variable(tf.convert_to_tensor([parameter], dtype=tf.float32), trainable=False)
Velocity = tf.Variable(tf.convert_to_tensor([velocity], dtype=tf.float32), trainable=False)
start = time.time()
for it in range(t2):
    # Calculate pairwise distances
    dist_diff = tf.expand_dims(Parameter[it, :, :3], 1) - tf.expand_dims(Parameter[it, :, :3], 0)
    Distance = tf.norm(dist_diff, axis=-1)

    # Calculate electrostatic and gravitational forces
    force_magnitude = K * tf.expand_dims(Parameter[it, :, 3], 1) * tf.expand_dims(Parameter[it, :, 3], 0) / Distance ** 3
    force_magnitude += G * tf.expand_dims(Parameter[it, :, 4], 1) * tf.expand_dims(Parameter[it, :, 4], 0) / Distance ** 3
    force_vector = force_magnitude[:, :, tf.newaxis] * dist_diff

    # Summing forces
    Force_Vector = tf.reduce_sum(force_vector, axis=1)

    # Calculate velocities
    Velocity_next = Velocity[it] + Force_Vector * dt / tf.expand_dims(Parameter[it, :, 4], -1)
    Velocity = tf.concat([Velocity, [Velocity_next]], axis=0)

    # Calculate displacements
    Displacement = Velocity[it] * dt + 0.5 * Force_Vector * dt / tf.expand_dims(Parameter[it, :, 4], -1)

    # Update parameters
    new_parameter = Parameter[it, :, :3] + Displacement
    new_parameter = tf.concat([new_parameter, Parameter[it, :, 3:]], axis=-1)
    Parameter = tf.concat([Parameter, [new_parameter]], axis=0)

    # print(f"Iteration {it}")

end = time.time()
print(end-start)