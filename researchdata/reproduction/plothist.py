#plothist.py

#plots a histogram of ages (Gyr)

import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

dfraw = pd.read_csv("phillipstable2.csv");
df = dfraw[dfraw['PreAge'] < 1.0]; #filter old stars out

tau = df['PreAge'];

plt.hist(tau, bins=100);
plt.show();