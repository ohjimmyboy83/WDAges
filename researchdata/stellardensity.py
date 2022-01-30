#stellardensity.py

import pandas as pd;
import matplotlib.pyplot as plt;
import matplotlib.colors as colors;
import numpy as np;
from physt import polar;

dfraw = pd.read_csv("qiutable2merged.csv");
df = dfraw[dfraw['PreAge'] < 2.0]; #filter old stars out

l = df['l'];
b = df['b'];
plx = df['plx'];
tau = df['PreAge'];

d = 1/plx;

#convert to polar projection (galactic, top-down)

r = d * np.cos(np.radians(b));

#define bins
lmax = np.radians(l.max());
rmax = r.max();
rbins = np.linspace(0.0, rmax, 50);
lbins = np.linspace(0.0, lmax, 60);

#make histogram data
h, _, _ = np.histogram2d(l, r, bins=(lbins,rbins));
L, R = np.meshgrid(lbins, rbins);
hmax = np.amax(h);
hmin = 0.001;
#plot it
fig, ax = plt.subplots(subplot_kw=dict(projection="polar"));

pc = ax.pcolormesh(L, R, h.T, cmap="viridis", shading='auto', norm=colors.Normalize(vmin=hmin, vmax=hmax));
ax.set_theta_zero_location("N");
fig.colorbar(pc);

plt.show()


#fig = plt.figure();
#ax = fig.add_subplot(projection='polar');
#ax.set_rmax(0.3);
#p = ax.scatter(np.radians(l), r, c=tau, cmap= 'viridis', s=1);
#ax.set_theta_zero_location("N")
#fig.colorbar(p, label='PreAge (Gyr)');
#ax.set_title("r * cos(b) vs l -- kpc vs degrees.");
#plt.show();