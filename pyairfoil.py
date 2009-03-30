#!/usr/bin/python

#    Program for for modeling the geometry of wind turbine blades

#    Copyright 2009 Brandon Stafford
#
#    This file is part of Pywind.
#
#    Pywind is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    Pywind is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with Pywind. If not, see <http://www.gnu.org/licenses/>.

import csv
from math import *
from enthought.mayavi import mlab
import numpy as np

def getCoordinates(coordString):
    pair = coordString.strip().split()
    return (float(pair[0]), float(pair[1]))

def buildAirfoil(airfoil, station):
    scale = float(station["chord"])
    tranx = float(station["tranx"])
    trany = float(station["trany"])
    theta = radians(float(station["pitch"]))
    z = float(station["z"])

    # apply translations and scaling
    scaled_and_translated = [((x - tranx) * scale, (y + trany) * scale) for (x, y) in airfoil]

    # apply rotation and insert z position
    return [(x * cos(theta) - y * sin(theta), x * sin(theta) + y * cos(theta), z) for (x, y) in scaled_and_translated]

# read in a blade profile
blade = list(csv.DictReader(open("testfoil.csv", "rb")))[1:]

# read in an airfoil data file in Selig's format
pairs = [getCoordinates(point) for point in open("sd6060.dat", "rb").readlines()[1:]]

# assemble list of stations, each station being a list of 3-tuple coordinates, (x, y, z)
profile = [buildAirfoil(pairs, station) for station in blade]

# make list of stations into one long list of [x, y, z] elements
pts = np.vstack(np.array(profile))

# grab x-position for colormap
colors = pts[:,0]

# plot the points
s = mlab.points3d(pts[:,0], pts[:,1], pts[:,2], colors, scale_mode = 'none', colormap='Spectral', scale_factor = 0.0015)

