disp('ARTICULATED MANIPULATOR')
syms a1 a2 a3 t1 t2 t3

%% Link Lengths
a1 = 30;
a2 = 20;
a3 = 10;


%% D-H Parameters [Theta, d, r, alpha, offset]
% if prismatic joint; theta = theta, d = 0, offset = 1, after offset put the value of d
% if revolute joint; theta = 0, offset = 0, after offset put the value of theta

H0_1 = Link ([0, a1, 0, pi/2, 0]);
H0_1.qlim = [-85 70] * pi/180;

H1_2 = Link ([0, 0, a2, 0 , 0]);
H1_2.qlim = [-25 85] * pi/180;

H2_3 = Link([0, 0, a3, 0, 0]);
H2_3.qlim = [-70 90] * pi/180;


Articulated = SerialLink ([H0_1 H1_2 H2_3], 'name', 'Articulated')
Articulated.plot ([0 0 0],'workspace',[-50 50 -50 50 0 80]) 
Articulated.teach
