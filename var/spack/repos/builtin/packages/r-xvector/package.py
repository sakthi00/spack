##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RXvector(RPackage):
    """Memory efficient S4 classes for storing sequences "externally" (behind
       an R external pointer, or on disk)."""

    homepage = "https://bioconductor.org/packages/XVector/"
    url      = "https://git.bioconductor.org/packages/XVector"
    list_url = homepage

    version('0.16.0', git='https://git.bioconductor.org/packages/XVector', commit='54615888e1a559da4a81de33e934fc0f1c3ad99f')

    depends_on('r-biocgenerics', type=('build', 'run'))
    depends_on('r-s4vectors', type=('build', 'run'))
    depends_on('r-iranges', type=('build', 'run'))
    depends_on('r-zlibbioc', type=('build', 'run'))
    depends_on('r@3.4.0:3.4.9', when='@0.16.0')
