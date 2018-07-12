Cx = 32000;
Cy = 500; 
lc = 1000;

Point(1) = {-Cx, -Cy, 0, lc};
Point(2) = {Cx , -Cy, 0, lc};
Point(3) = {Cx , Cy , 0, lc};
Point(4) = {-Cx, Cy , 0, lc};

Line(1) = {1,2};
Line(2) = {2,3};
Line(3) = {3,4};
Line(4) = {4,1};

Line Loop(5) = {1,2,3,4};
Plane Surface(6) = {5};


Transfinite Line{2} = 2; 
Transfinite Line{4} = 2; 
 

Transfinite Line{1} = 65; 
Transfinite Line{3} = 65; 
 
Mesh.Algorithm=8; 
  
// Recombine Surface{6}; 

Physical Line("sideL") = {1};
Physical Line("river") = {2};
Physical Line("sideR") = {3};
Physical Line("sea") = {4};

Physical Surface("domain") = {6};
