# A Last.fm API interface.
# Copyright (C) 2013  Nikola Vukosavljević
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

from distutils.core import setup

setup(name="lfm",
      version="1.0",
      description="A Last.fm API interface.",
      long_description="", # FIX
      author="hauzer",
      author_email="hauzer@gmx.com",
      url="https://bitbucket.org/hauzer/lfm/",
      download_url="https://bitbucket.org/hauzer/lfm/downloads",
      license="GPLv3",
      packages=["lfm", "lfm.api"])
