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


class AllineaReports(Package):
    """Allinea Performance Reports are the most effective way to characterize
    and understand the performance of HPC application runs. One single-page
    HTML report elegantly answers a range of vital questions for any HPC site
    """

    homepage = "http://www.allinea.com/products/allinea-performance-reports"

    version('7.0.5', '555d0d7d1b904a57d87352b5f5e1415b')
    #version('6.0.4', '3f13b08a32682737bc05246fbb2fcc77')

    # Licensing
    license_required = True
    license_comment = '#'
    license_files = ['licences/Licence']
    license_vars = ['ALLINEA_LICENCE_FILE', 'ALLINEA_LICENSE_FILE']
    license_url = 'http://www.allinea.com/user-guide/reports/Installation.html'

    def url_for_version(self, version):
        # TODO: add support for other architectures/distributions
        url = "http://content.allinea.com/downloads/"
        #return url + "allinea-reports-%s-Redhat-6.0-x86_64.tar" % version
        return url + "allinea-reports-%s-Suse-12-x86_64.tar" % version

    def install(self, spec, prefix):
        textinstall = Executable('./textinstall.sh')
        textinstall('--accept-licence', prefix)
