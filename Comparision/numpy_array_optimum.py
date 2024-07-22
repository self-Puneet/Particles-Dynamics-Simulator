import numpy as np
import time

# Electrostatic Constant  /   Coulomb's Constant
K = 8.9975 * (10 ** 9)

# Gravitational Constant
G = 6.67430 * (10 ** (-11))

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

# Initialize arrays to store parameters and velocities at each step
parameters = [parameter]
velocities = [velocity]

start = time.time()

for it in range(t2):
    # Current parameter and velocity
    curr_param = parameters[-1]
    curr_velocity = velocities[-1]
    
    # Calculate pairwise distances
    dist_diff = curr_param[:, np.newaxis, :3] - curr_param[np.newaxis, :, :3]
    Distance = np.linalg.norm(dist_diff, axis=-1)
    
    # Avoid division by zero in distances
    Distance[Distance == 0] = 1e-10
    
    # Calculate electrostatic and gravitational forces
    force_magnitude = K * np.outer(curr_param[:, 3], curr_param[:, 3]) / Distance ** 3
    force_magnitude += G * np.outer(curr_param[:, 4], curr_param[:, 4]) / Distance ** 3
    force_vector = force_magnitude[:, :, np.newaxis] * dist_diff

    # Summing forces
    Force_Vector = np.sum(force_vector, axis=1)

    # Calculate velocities
    Velocity_next = curr_velocity + Force_Vector * dt / curr_param[:, 4][:, np.newaxis]
    velocities.append(Velocity_next)

    # Calculate displacements
    Displacement = curr_velocity * dt + 0.5 * Force_Vector * dt ** 2 / curr_param[:, 4][:, np.newaxis]

    # Update parameters
    new_param = np.copy(curr_param)
    new_param[:, :3] += Displacement
    parameters.append(new_param)
    
end = time.time()

print(f"time for 1 interval = {(end-start)}")
print(131.70439743995667 / 1.5274360179901123)