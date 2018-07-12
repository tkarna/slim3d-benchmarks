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


cd output

gmsh mesh3d.msh uv/uv_COMP_0.idx w/w.idx salinity/salinity.idx z/z.idx ../opt.opt
