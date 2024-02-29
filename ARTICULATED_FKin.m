disp('ARTICULATED MANIPULATOR')
syms a1 a2 a3 t1 t2 t3

%% Link Lengths
a1 = 20;
a2 = 30;
a3 = 10;


%% D-H Parameters [Theta, d, r, alpha, offset]
% if prismatic joint; theta = theta, d = 0, offset = 1, after offset put the value of d
% if revolute joint; theta = 0, offset = 0, after offset put the value of theta

H0_1 = Link ([0, a1, 0, pi/2, 0]);
H0_1.qlim = [-pi/2 pi/2];

H1_2 = Link ([0, 0, a2, 0 , 0]);
H1_2.qlim = [-pi/6 pi/2];

H2_3 = Link([0, 0, a3, 0, 0]);
H2_3.qlim = [-pi/2 pi/2];


Articulated = SerialLink ([H0_1 H1_2 H2_3], 'name', 'Articulated')
Articulated.plot ([0 0 0],'workspace',[-50 50 -50 50 0 50]) 
Articulated.teach

    
