__author__ = "Marin Lauber"
__copyright__ = "Copyright 2020, Marin Lauber"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "M.Lauber@soton.ac.uk"

import numpy as np, pandas as pd, datashader as ds
from datashader import transfer_functions as tf
from datashader.colors import inferno, viridis, Greys9
from numba import jit
from math import sin, cos, sqrt, fabs


@jit(nopython=True)
def Clifford(x, y, a, b, c, d):
    return sin(a * y) + c * cos(a * x), \
           sin(b * x) + d * cos(b * y)


@jit(nopython=True)
def PeterdeJong(x, y, a, b, c, d):
    return sin(a * y) - cos(b * x), \
           sin(c * x) - cos(d * y)


@jit(nopython=True)
def _trajectory_coords(fn, x0, y0, a, b, c, d, n):
    x, y = np.zeros(n), np.zeros(n)
    x[0], y[0] = x0, y0
    for i in np.arange(n-1):
        x[i+1], y[i+1] = fn(x[i], y[i], a, b, c, d)
    return x,y


def ComputeTrajectory(Attractor, x0, y0, a, b, c, d, n=200000000):
    """
    Computes n trajectories around a given Attractor from initial position (x0, y0)
    with parameteres (a, b, c, d).

    Parameters :

    Returns :
        Pands DataFrame containing the (x, y) coordinates of the trajectories

    Some examples:
        ComputeTrajectory(Clifford, 0, 0, -1.4, 1.6, 1., 0.7)
        ComputeTrajectory(Clifford, 0, 0, -1.8, -2.0, -0.5, -0.9)
        ComputeTrajectory(Clifford, 0, 0, 1.7, 1.7, 0.6, 1.2)
        ComputeTrajectory(Clifford, 0, 0, 1.5, -1.8, 1.6, 0.9)
        ComputeTrajectory(Clifford, 0, 0,-1.7, 1.8, -1.9, -0.4) 
        ComputeTrajectory(PeterdeJong, 0, 0, 1.4, -2.3, 2.4, -2.1)
        ComputeTrajectory(PeterdeJong, 0, 0, 2.01, -2.53, 1.61, -0.33)
    """
    x, y = _trajectory_coords(Attractor, x0, y0, a, b, c, d, n)
    return pd.DataFrame(dict(x=x,y=y))


def MakeImage(trajectory, cm=['#114d7d', '#000000'], size=(1080, 1080)):
    width, height = size
    cvs = ds.Canvas(plot_width=width, plot_height=height)
    pts = cvs.points(trajectory, 'x', 'y')
    ds.transfer_functions.Image.border=0
    img = tf.shade(pts, cmap=cm)
    img
    return img


def SaveImage(img, fname='image'):
    ds.utils.export_image(img=img,filename=fname,fmt=".png",background='white')
