# lock exchange benchmark test

Based on the slim3d lock exchange example found at
https://git.immc.ucl.ac.be/slim/slim/tree/master/benchmarks/lock-exchange

branch master
commit 5595cbb

Changes:
- triangular mesh, same 1000 m resolution, same 20 layers
- set end time to 9000 s
- set export time to 900 s
- use same time step 10 s
- use implicit vertical diffusion (and advection)
- set horizontal diffusivity to 250
- set vertical diffusivity to 1e-4

