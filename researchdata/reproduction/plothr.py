#plothr.py

#plots an Hertzsprung-Russel diagram

import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

dfraw = pd.read_csv("colortable3.csv");
df = dfraw[dfraw['PreAge'] < 2.0]; #filter old stars out

x = df['bp_rp'];
y = df['Gmag'];
tau = df['PreAge'];

fig = plt.figure();
ax = plt.axes(title='G vs bp-rp');
p = ax.scatter(x, y, c=tau,cmap="viridis", s=1);
fig.colorbar(p, label='PreAge (Gyr)');
ax.set_xlabel('bp-rp');
ax.set_ylabel('G (mag)');
plt.show();