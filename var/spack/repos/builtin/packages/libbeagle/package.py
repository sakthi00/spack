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


class Libbeagle(AutotoolsPackage):
    """Beagle performs genotype calling, genotype phasing, imputation of
       ungenotyped markers, and identity-by-descent segment detection."""

    homepage = "https://github.com/beagle-dev/beagle-lib"
    url      = "https://github.com/beagle-dev/beagle-lib/archive/beagle_release_2_1_2.tar.gz"

    version('2.1.2', '1107614e86f652f8ee45c1c92f2af3d4')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('subversion', type='build')
    depends_on('pkg-config', type='build')

    def url_for_version(self, version):
        url = "https://github.com/beagle-dev/beagle-lib/archive/beagle_release_{0}.tar.gz"
        return url.format(version.underscored)
