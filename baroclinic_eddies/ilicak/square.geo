L = 1.6e5;
l = 5e5;

Point(1) = {0, 0, 0};
Point(2) = {L, 0, 0};
Point(3) = {L, l, 0};
Point(4) = {0, l, 0};
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};
Line Loop(1) = {3, 4, 1, 2};
Plane Surface(1) = {1};

Transfinite Line{1} = 41;
Transfinite Line{2} = 126;
Transfinite Line{3} = 41;
Transfinite Line{4} = 126;
Transfinite Surface{1} = {1,2,3,4};

Recombine Surface{1};

Physical Surface("Surface")={1};
Physical Line("Wall") = {1,3};
Physical Line("cut") = {2};
Physical Line("paste") = {4};

