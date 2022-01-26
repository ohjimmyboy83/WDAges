#plotquivercolor.py

import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np;
from mpl_toolkits import mplot3d;

dfraw = pd.read_csv("qiutable2merged.csv");
df = dfraw[dfraw['PreAge'] < 0.5]; #filter old stars out


def findvector(mydf, myra, mypmra, mydec, mypmdec, myplx):
    r = 1 / myplx;
    t = 20.0;
    
    theta1 = ((np.pi/2) - mydec);
    vdec = t * mypmdec;
    vra = t * mypmra;

    ra2 = myra + vra;
    dec2 = mydec + vdec;
    theta2 = ((np.pi/2) - dec2);x1 = r * np.cos(ra1) * np.sin(theta1);
    
    x1 = r * np.cos(ra1) * np.sin(theta1);
    y1 = r * np.sin(ra1) * np.sin(theta1);
    z1 = r * np.cos(theta1);

    x2 = r * np.cos(ra2) * np.sin(theta2);
    y2 = r * np.sin(ra2) * np.sin(theta2);
    z2 = r * np.cos(theta2);

    dx = x2 - x1;
    dy = y2 - y1;
    dz = z2 - z1;
    return x1, y1, z1, dx, dy, dz;

