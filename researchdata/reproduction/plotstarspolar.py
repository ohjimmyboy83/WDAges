#plotstarspolar.py

import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np;

dfraw = pd.read_csv("phillipstable2.csv");
df = dfraw[dfraw['PreAge'] < 2.0]; #filter old stars out

l = df['l'];
b = df['b'];
plx = df['plx'];
tau = df['PreAge'];

d = 1/plx;

#convert to polar projection (galactic, top-down)

r = d * np.cos(np.radians(b));

fig = plt.figure();
ax = fig.add_subplot(projection='polar');
ax.set_rmax(0.3);
p = ax.scatter(np.radians(l), r, c=tau, cmap= 'viridis', s=1);
ax.set_theta_zero_location("N")
fig.colorbar(p, label='PreAge (Gyr)');
ax.set_title("r * cos(b) vs l -- kpc vs degrees.");
plt.show();