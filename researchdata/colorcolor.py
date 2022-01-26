#colorcolor.py

#plots a color-color diagram (bp-g vs g-rp)

import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

dfraw = pd.read_csv("qiutable2merged.csv");
df = dfraw[dfraw['PreAge'] < 1.0]; #filter old stars out

x = df['bp_g'];
y = df['g_rp'];
tau = df['PreAge'];

fig = plt.figure();
ax = plt.axes(title='bp-g vs g-rp');
p = ax.scatter(x, y, c=tau,cmap="viridis", s=1);
fig.colorbar(p, label='PreAge (Gyr)');
ax.set_xlabel('bp-g');
ax.set_ylabel('g-rp');
plt.show();