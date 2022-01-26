#plotstarspm.py

#plots ra, dec, parallax distance and nonradial velocity vectors in a 3d plot

import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np;
from mpl_toolkits import mplot3d;

dfraw = pd.read_csv("qiutable2merged.csv");
df = dfraw[dfraw['PreAge'] < 0.5]; #filter old stars out

ra1 = np.radians(df['RAdeg']);
pmra = np.radians(df['pmRA']/360.0); #in radians per 1,000 years
dec1 = np.radians(df['DEdeg']);
pmdec = np.radians(df['pmDE']/360.0);
plx = df['plx'];
tau = df['PreAge'];

r = 1/plx;
t = 20.0; #time step in thousands of years

#convert to spherical coordinates and find spherical displacement vectors

theta1 = ((np.pi/2) - dec1);
vdec = t * pmdec;
vra = t * pmra

ra2 = ra1 + vra;
dec2 = dec1 + vdec;
theta2 = ((np.pi/2) - dec2);
    
#convert to cartesian coordinates
x1 = r * np.cos(ra1) * np.sin(theta1);
y1 = r * np.sin(ra1) * np.sin(theta1);
z1 = r * np.cos(theta1);

x2 = r * np.cos(ra2) * np.sin(theta2);
y2 = r * np.sin(ra2) * np.sin(theta2);
z2 = r * np.cos(theta2);

dx = x2 - x1;
dy = y2 - y1;
dz = z2 - z1;

fig = plt.figure();
ax = plt.axes(projection='3d',title='Positive x is Aries Point, Positive z is Polaris');
p = ax.quiver(x1, y1, z1, dx, dy, dz,
            length=1.0, normalize=False);
#p = ax.scatter3D(x, y ,z,c=tau,cmap="viridis", s=1);
#fig.colorbar(p, label='PreAge (Gyr)');
ax.set_xlabel('kpc');
plt.show();s