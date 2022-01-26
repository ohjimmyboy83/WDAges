#plotstars.py

#plots ra, dec, and parallax in a 3d plot

import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np;
from mpl_toolkits import mplot3d;

dfraw = pd.read_csv("qiutable2merged.csv");
df = dfraw[dfraw['PreAge'] < 0.5]; #filter old stars out

ra = np.radians(df['RAdeg']);
dec = np.radians(df['DEdeg']);
plx = df['plx'];
tau = df['PreAge'];

r = 1/plx;

#convert to spherical coordinates
    
theta = (np.pi/2) - dec;
    
#convert to cartesian coordinates
x = r * np.cos(ra) * np.sin(theta);
y = r * np.sin(ra) * np.sin(theta);
z = r * np.cos(theta);

fig = plt.figure();
ax = plt.axes(projection='3d',title='Positive x is Aries Point, Positive z is Polaris');
p = ax.scatter3D(x, y ,z,c=tau,cmap="viridis", s=1.5);
fig.colorbar(p, label='PreAge (Gyr)');
ax.set_xlabel('kpc');
plt.show();