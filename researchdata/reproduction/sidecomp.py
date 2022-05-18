#sidecomp.py

#compares the age distributions on two ends of the sky

import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

dfraw = pd.read_csv("phillipstable2.csv");
df = dfraw[dfraw['PreAge'] < 2.0]; #filter old stars out
df1 = df.query('l <= 45.0 or l > 225.0'); 
df2 = df.query('l > 45.0 and l <= 225.0');

tau1 = df1['PreAge'];
tau2 = df2['PreAge'];

mean1 = np.mean(tau1);
mean2 = np.mean(tau2);

sig1 = np.var(tau1);
sig2 = np.var(tau2);

lgd1 = "mean = " + str(mean1) + "\nvar = " + str(sig1);
lgd2 = "mean = " + str(mean2) + "\nvar = " + str(sig2);


fig, (ax1, ax2) = plt.subplots(1, 2);
ax1.hist(tau1, 100, label=lgd1);
ax2.hist(tau2, 100, label=lgd2);
ax1.set_title('l = 225 to 45 degrees');
ax2.set_title('l = 45 to 225 degrees');
ax1.legend();
ax2.legend();
plt.show();