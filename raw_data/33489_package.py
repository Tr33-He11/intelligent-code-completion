##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
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


class RMemoise(RPackage):
    """Cache the results of a function so that when you call it again with the
    same arguments it returns the pre-computed value."""

    homepage = "https://github.com/hadley/memoise"
    url      = "https://cran.rstudio.com/src/contrib/memoise_1.1.0.tar.gz"
    list_url = homepage
    version('1.1.0', '493209ee04673f0fcab473c3dd80fb8c')
    version('1.0.0', 'd31145292e2a88ae9a504cab1602e4ac')

    depends_on('r-digest', type=('build', 'run'))
