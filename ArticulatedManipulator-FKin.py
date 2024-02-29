## Articulated

# import libraries
import numpy as np

# link lengths in mm
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))

#joint variables: mm if d and degrees if theta
T1 = float(input("T1 = "))
T2 = float(input("T2 = "))
T3 = float(input("T3 = "))

#Convert Rotation angles
#deg to radian
T1 = (T1/180)*np.pi
T2 = (T2/180)*np.pi
T3 = (T3/180)*np.pi

#Parametric Table: (Theta, alpha, r, d)

PT = [[T1,(90/180)*np.pi,0,a1],
     [T2,(0/180)*np.pi,a2,0],
     [T3,(0/180)*np.pi,a3,0]]

#Homogeneous Transformation Matrix Formula
i = 0
H0_1 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

i = 1
H1_2 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

i = 2
H2_3 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

H0_1 = np.matrix(H0_1)
print("H0_1= ")
print(H0_1)

H1_2 = np.matrix(H1_2)
print("H1_2= ")
print(H1_2)

H2_3 = np.matrix(H2_3)
print("H2_3= ")
print(H2_3)

H0_2 = np.dot(H0_1,H1_2)
H0_3 = np.dot(H0_2,H2_3)
print("H0_3= ")
print(np.matrix(np.around(H0_3,3)))
