#plotstarspolar.py

import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np;

dfraw = pd.read_csv("qiutable2merged.csv");
df = dfraw[dfraw['PreAge'] < 1.5]; #filter old stars out

messraw = pd.read_csv("messier.csv");
mess = messraw[messraw['distpc'] < 500.0];

l = df['l'];
b = df['b'];
plx = df['plx'];
tau = df['PreAge'];

d = 1/plx;

lm = mess['l'].astype(float);
bm = mess['b'];
dm = mess['distpc'] / 1000.0;
namem = mess['messiernum'].astype(str);
mm = ['$\mathrm{' + x + '}$' for x in namem];

#convert to polar projection (galactic, top-down)

r = d * np.cos(np.radians(b));
rm = dm * np.cos(np.radians(bm));

fig = plt.figure();
ax = fig.add_subplot(projection='polar');
ax.set_rmax(0.3);
p = ax.scatter(np.radians(l), r, c=tau, cmap= 'viridis', s=1);
m7 = ax.scatter(np.radians(lm.data[0]), rm.data[0], marker='$M7$', s=500, c='black');
m27 = ax.scatter(np.radians(lm.data[1]), rm.data[1], marker='$M27$', s=500, c='black');
m34 = ax.scatter(np.radians(lm.data[2]), rm.data[2], marker='$M34$', s=500, c='black');
m39 = ax.scatter(np.radians(lm.data[3]), rm.data[3], marker='$M39$', s=500, c='black');
m40 = ax.scatter(np.radians(lm.data[4]), rm.data[4], marker='$M40$', s=500, c='black');
m42 = ax.scatter(np.radians(lm.data[5]), rm.data[5], marker='$M42$', s=500, c='black');
m43 = ax.scatter(np.radians(lm.data[6]), rm.data[6], marker='$M43$', s=500, c='black');
m44 = ax.scatter(np.radians(lm.data[7]), rm.data[7], marker='$M44$', s=500, c='black');
m45 = ax.scatter(np.radians(lm.data[8]), rm.data[8], marker='$M45$', s=500, c='black');
m47 = ax.scatter(np.radians(lm.data[9]), rm.data[9], marker='$M47$', s=500, c='black');
m48 = ax.scatter(np.radians(lm.data[10]), rm.data[10], marker='$M48$', s=500, c='black');
m78 = ax.scatter(np.radians(lm.data[11]), rm.data[11], marker='$M78$', s=500, c='black');
ax.set_theta_zero_location("N")
fig.colorbar(p, label='PreAge (Gyr)');
ax.set_title("r * cos(b) vs l -- kpc vs degrees.");
plt.show();