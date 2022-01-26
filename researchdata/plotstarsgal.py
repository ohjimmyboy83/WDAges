#plotstarsgal.py

#plots ra, dec, and parallax in a 3d plot

import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np;
from mpl_toolkits import mplot3d;

dfraw = pd.read_csv("qiutable2merged.csv");
df = dfraw[dfraw['PreAge'] < 2.0]; #filter old stars out

#ra = np.radians(df['RAdeg']);
#dec = np.radians(df['DEdeg']);
l = df['l'];
b = df['b'];
plx = df['plx'];
tau = df['PreAge'];

r = 1/plx;

#convert to spherical coordinates
    
theta = (np.pi/2) - np.radians(b);
    
#convert to cartesian coordinates
x = r * np.cos(np.radians(l)) * np.sin(theta);
y = r * np.sin(np.radians(l)) * np.sin(theta);
z = r * np.cos(theta);

fig = plt.figure();
ax = plt.axes(projection='3d',title='Positive x is Galactic Center, Positive z is GNP');
p = ax.scatter3D(x, y ,z,c=tau,cmap="viridis", s=1);
fig.colorbar(p, label='PreAge (Gyr)');
ax.set_xlabel('kpc');
plt.show();