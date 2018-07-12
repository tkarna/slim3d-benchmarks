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

import slim3d
import slimPre
import shutil

output_dir = './output/'
data_dir_base = 'data'+slimPre.partition_nb()+'/'
data_dir = data_dir_base+slimPre.partition_id()+'/'
slimPre.make_directory(output_dir)
shutil.copyfile(data_dir_base+'mesh3d.msh', output_dir+'mesh3d.msh')

domain = slim3d.Domain(data_dir_base+'mesh3d.msh', data_dir_base+'periodicMesh.txt', reference_density=1001.85)

equations = slim3d.Slim3d_equations(domain, salinity=True)
equations.set_implicit_vertical(True)
#equations.set_horizontal_viscosity('smagorinsky')
equations.set_horizontal_viscosity('constant', 250.)
equations.set_vertical_viscosity('constant', 1e-4)
equations.set_lax_friedrichs_factor(1)
equations.set_bottom_friction(False)
equations.set_limiter(True)
equations.set_initial_salinity('netcdf', data_dir_base+"Sinit_COMP_0.msh")
#equations.set_initial_salinity('netcdf', data_dir+"initS/initS.idx")
equations.set_initial_temperature('vertical_gradient', None, 10, 0.)
equations.set_boundary_coast(['river','sea'])
#equations.set_vertical_adaptation(tau=100, uv_factor=0, rho_factor=1, minimum_height=.5, maximum_height=1500, resize_factor=1.5, background_error=0.00001, vertical_gradient_factor=.5)

time_loop = slim3d.Loop(equations, 
        time_step=10,
        export_time_step=900, 
        final_time = 9000,
        output_directory=output_dir)
time_loop.export_elevation()
time_loop.export_salinity()
time_loop.export_uv(False)
time_loop.export_uv2d(False)
time_loop.export_w()
time_loop.export_rho()
time_loop.loop()
