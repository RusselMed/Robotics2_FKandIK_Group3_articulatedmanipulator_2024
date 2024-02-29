# Inverse Kinematics of Articulated

# Import Libraries
import numpy as np

# Link Lengths in mm
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))

# Position Vector in mm
x0_3 =  float(input("x0_3 = "))
y0_3 =  float(input("y0_3 = "))
z0_3 =  float(input("z0_3 = "))

# Inverse Kinematics using Graphical Method

# Solution 1
theta1 = np.arctan(x0_3/y0_3) * 180/np.pi

# Solution 2
r1 = np.sqrt(y0_3**2 + x0_3**2)

# Solution 3
r2 = z0_3-a1

# Solution 4
phi1 = np.arctan(r2/r1) * 180/np.pi

# Solution 5
r3 = np.sqrt(r2**2 + r1**2) 

# Solution 6
phi2 = np.arccos((a3**2-a2**2-r3**2)/(-2*a2*r3)) * 180/np.pi

# Solution 7
theta2 = (phi1 + phi2)

# Solution 8
phi3 = np.arccos((r3**2-a2**2-a3**2)/(-2*a2*a3)) * 180/np.pi

# Solution 9
theta3 = phi3 - 180

# Displaying the JOint Variables
print("theta1 =", np.around(theta1,0))
print("theta2 =", np.around(theta2,0))
print("theta3 =", np.around(theta3,0))
