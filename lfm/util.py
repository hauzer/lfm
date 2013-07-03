# A Last.fm API interface.
# Copyright (C) 2013  Никола Вукосављевић
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

import inspect

def to_array(xs, key):
    array = {}

    for i, x in enumerate(xs):
        array[key + "[" + str(i) + "]"] = x

    return array


def to_arrays(xs, keys):
    arrays = {}

    for x, key in zip(list(zip(*xs)), keys):
        arrays.update(to_array(x, key))

    return arrays


def class_to_arrays(klas, i = 0):
    attrs = [(key, value) for key, value in inspect.getmembers(klas)
                    if not callable(value) and not(key.startswith("__") and key.endswith("__"))]
    
    arrays = {}
    for key, value in attrs:
        arrays[key + "[" + str(i) + "]"] = value

    return arrays

def classes_to_arrays(klasses):
    arrays = {}
    for i, klas in enumerate(klasses):
        arrays.update(class_to_arrays(klas, i))

    return arrays