# coding=utf-8

#
# A Last.fm API interface.
# Copyright (C) 2013  Nikola "hauzer" Vukosavljević
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


from lfm        import VERSION
from setuptools import setup, find_packages


readme_lines = open("README.rst", "r").read().splitlines()

description = readme_lines[0]
long_description = "\n".join(readme_lines[2:])

setup(name              = "lfmh",
      version           = VERSION,
      packages          = find_packages(),
      install_requires  = ["requests"],

      author            = "Nikola \"hauzer\" Vukosavljević",
      author_email      = "hauzer@gmx.com",
      description       = description,
      long_description  = long_description,
      license           = "GPLv3",
      url               = "https://bitbucket.org/hauzer/lfm/",
      download_url      = "https://bitbucket.org/hauzer/lfm/downloads",
      
      classifiers = [
                     "Development Status :: 3 - Alpha",
                     "Intended Audience :: Developers",
                     "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                     "Operating System :: OS Independent",
                     "Programming Language :: Python :: 3",
                     "Topic :: Software Development :: Libraries",
                    ]
      )
