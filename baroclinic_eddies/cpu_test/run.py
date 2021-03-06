import slim3d

runFile = 'data/'
meshFile = runFile+'mesh3d.msh'
sim_Ti = "2012-03-24 00:00:00"
sim_Tf = "2012-03-24 01:34:40"
dt = 142
sim_export = 40*dt
sim_exportFullRatio = -1
output_directory = "./output"

domain = slim3d.Domain(meshFile, "periodicMesh.txt", reference_density=1000)

equations = slim3d.Slim3d_equations(domain,temperature=True)
equations.set_coriolis((runFile+'coriolis.nc', 'coriolis'))
equations.set_horizontal_viscosity('constant', 20.0)
equations.set_vertical_viscosity("constant", 1.0e-4)
equations.set_implicit_vertical(True)
equations.set_lax_friedrichs_factor(1.0)
equations.set_linear_density(mode="temperature", constant_coefficient=5., linear_coefficient=-0.2)
equations.set_initial_temperature('netcdf', temperature=(runFile+'initialTemp.nc','temp'))
equations.set_boundary_coast(["Wall"])

time_loop = slim3d.Loop(
    equations,
    time_step=dt,
    export_time_step=sim_export,
    ratio_full_export=sim_exportFullRatio,
    initial_time=sim_Ti,
    final_time=sim_Tf,
    output_directory=output_directory)
# time_loop.export_elevation()
# time_loop.export_temperature()
# time_loop.export_uv()
# time_loop.export_uv2d()
# time_loop.export_rho()
time_loop._slimSolver.functions.bottomFrictionDragCoeff2d = slim3d.dgpy.functionConstant(0.01)
time_loop.loop()
