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

