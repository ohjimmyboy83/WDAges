#plotstarspm.py

#plots ra, dec, parallax distance and nonradial velocity vectors in a 3d plot

import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np;
from mpl_toolkits import mplot3d;

dfraw = pd.read_csv("qiutable2merged.csv");
df = dfraw[dfraw['PreAge'] < 2.0]; #filter old stars out

ra = np.radians(df['RAdeg']);
pmra = np.radians(df['pmRA'] / 3600000.0);
dec = np.radians(df['DEdeg']);
pmdec = np.radians(df['pmDE'] / 3600000.0);
plx = df['plx'];
tau = df['PreAge'];

r = 1/plx;

#convert to spherical coordinates
vra = r * np.sin(pmra);
vdec = r * np.sin(pmdec);
v = np.sqrt(vra**2 + vdec**2);
    
theta = (np.pi/2) - dec;
    
#convert to cartesian coordinates
x = r * np.cos(ra) * np.sin(theta);
dx = v * np.cos(vra) * np.sin(vdec);
y = r * np.sin(ra) * np.sin(theta);
dy = v * np.sin(vra) * np.sin(vdec);
z = r * np.cos(theta);
dz = v * np.cos(vdec);

fig = plt.figure();
ax = plt.axes(projection='3d',title='Positive x is Aries Point, Positive z is Polaris');
p = ax.quiver(x, y, z, dx, dy, dz,
            length=0.05, normalize=True);
#p = ax.scatter3D(x, y ,z,c=tau,cmap="viridis", s=1);
#fig.colorbar(p, label='PreAge (Gyr)');
ax.set_xlabel('kpc');
plt.show();