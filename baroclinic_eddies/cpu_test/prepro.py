import slimPre
import numpy as np

run_dir = 'data/'
slimPre.make_directory(run_dir)

slimPre.write_file(run_dir+'bath.nc',None,None,[('bath',1000)])

mesh_file = 'square.msh'

print('Extruding mesh')
def shiftOperation(node, iPerBound) :
  n = [node[0] - 1.6e5, node[1], node[2]]
  return n
cutTags = ["cut"]
pasteTags = ["paste"]
mapFilename = "periodicMesh.txt"
periodicity = (shiftOperation, cutTags, pasteTags, mapFilename)

nPart = 2
slimPre.dgpy.dgMeshPartition(mesh_file, nPart)
mesh_file = mesh_file[:-4] + '_' + str(nPart)+'.msh'

slimPre.extrude(mesh_file, (run_dir+'bath.nc','bath'), nb_layers=40, mesh_file_name_out=run_dir+'mesh3d.msh', periodicity=periodicity)

print('Loading 3D mesh')
mesh_file = run_dir + "mesh3d.msh"

mesh = slimPre.Mesh(mesh_file)
region_global = slimPre.Region(mesh)

print('Preprocessing coriolis')
xyz = region_global.coordinates
coriolis = -1.2e-4
slimPre.write_file(run_dir+'coriolis.nc', region=None, time=None, data=[('coriolis', coriolis)])
slimPre.netcdf_to_msh(mesh_file, run_dir+'coriolis.nc', 'coriolis', 'coriolis')

print('Preprocessing initial temperature')
xyz = region_global.coordinates
theta0 = 10.1 + 3*(-975.-xyz[:,2])/(-975.)
yw = 2.5e5-4e4*np.sin(2*np.pi*3*xyz[:,0]/1.6e5)
fact = 1. - (xyz[:,1]-yw[:])/4.e4
indx = fact < 0.
fact[indx] = 0.
indx = fact > 1.
fact[indx] = 1.
theta = theta0[:]-1.2*fact[:]

yw_t = 2.5e5-2.0e4*np.sin(np.pi*(xyz[:,0]-1.1e5)/2.0e4)
theta_t = 0.3*(1.0 - (xyz[:,1] - yw_t)/2.0e4)
indx = (xyz[:,0] > 1.1e5) * (xyz[:,0] < 1.3e5) * (xyz[:,1] > yw_t[:] - 2.0e4) * (xyz[:,1] < yw_t[:] + 2.0e4)
theta[indx] += theta_t[indx]

slimPre.write_file(run_dir+'initialTemp.nc', region=region_global, time=None, data=[('temp', theta)])
slimPre.netcdf_to_msh(mesh_file, run_dir+'initialTemp.nc', 'temp', 'temp')

print('preprocessing done')
slimPre.exit(0)
