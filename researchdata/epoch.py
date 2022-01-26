#epoch.py

import numpy as np;

t = 2015.5;
T = (t - 2000.0)/100;

alpha = np.deg2rad(192.8595);
delta = np.deg2rad(27.1284);

print("alpha = ");
print(np.rad2deg(alpha));
print("\n");
print("delta = ");
print(np.rad2deg(delta));
print("\n");

M = (1.2812323 * T) + (0.0003879 * T**2) + (0.0000101 * T**3);
N = (0.5567530 * T) + (0.0001185 * T**2) + (0.0000116 * T**3);

dalpha = (M + N) * np.sin(alpha) * np.tan(delta);
ddelta = N * np.cos(alpha);

alpha = alpha + dalpha;
delta = delta + ddelta;

print("dalpha = "); 
print(np.rad2deg(dalpha));
print("\n");
print("ddelta = ");
print(np.rad2deg(ddelta));
print("\n");
print("alpha = ");
print(np.rad2deg(alpha));
print("\n");
print("delta = ");
print(np.rad2deg(delta));
print("\n");