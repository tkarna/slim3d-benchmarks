# SLIM - Copyright (C) <2010-2018>
# <Universite catholique de Louvain (UCL), Belgique>
# 	
# List of the contributors to the development of SLIM: see AUTHORS file.
# Description and complete License: see LICENSE file.
# 	
# This program (SLIM) is free software: 
# you can redistribute it and/or modify it under the terms of the GNU General 
# Public License as published by the Free Software Foundation, either version
# 3 of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program (see COPYING file).  If not, 
# see <http://www.gnu.org/licenses/>.

import slimPre, dgpy
import numpy as np

data_dir_base = 'data'+slimPre.partition_nb()+'/'
data_dir = data_dir_base+slimPre.partition_id()+'/'
slimPre.make_directory(data_dir)

from dgpy.scripts import Common
if (slimPre.partition_id()==0):
    Common.genMesh("haidvogel.geo", 2)
dgpy.Msg.Barrier()
mesh_file = 'haidvogel.msh'

slimPre.partition_mesh(mesh_file, 'mesh_part.msh')
mesh_file = 'mesh_part.msh'

print('Extruding mesh')
def shiftOperation(node, iPerBound) :
  n = [node[0], node[1] - 1000, node[2]]
  return n
cutTags = ["sideR"]
pasteTags = ["sideL"]
mapFilename = data_dir_base+"periodicMesh.txt"
periodicity = (shiftOperation, cutTags, pasteTags, mapFilename)

mesh2d = slimPre.Mesh(mesh_file)
slimPre.write_file(data_dir+'bath_2d.nc', region=None, time=None, data=[('bath',20)])
slimPre.extrude(mesh_file, (data_dir+'bath_2d.nc','bath'), nb_layers=int(20), mesh_file_name_out=data_dir_base+'mesh3d.msh', factor_show=200, periodicity=periodicity)

print('Loading 3D mesh')
mesh_file = data_dir_base + "mesh3d.msh"
mesh = slimPre.Mesh(mesh_file)

def initS(cm) : 
    xyz = cm.get(mesh._groups.getFunctionCoordinates())
    return (5.5*np.minimum(np.maximum(-xyz[:,0]/50, 0.0), 1.0))[:,None]
  
cm = dgpy.functorCache(dgpy.functorCache.INTEGRATION_GROUP_MODE, mesh._groups)  
cm.setGroup(mesh._groups.getElementGroup(0))

f = dgpy.functorNumpy(initS)
val = cm.get(f)

dof = dgpy.dgDofContainer(mesh._groups,1)
dof.L2Projection(f)
#idx = dgpy.dgIdxExporter(dof,data_dir_base+"initS")
#idx.exportIdx()
dof.exportMsh(data_dir_base+"Sinit")

print('preprocessing done')
slimPre.exit(0)