#plotstarsgal.py

#plots ra, dec, and parallax in a 3d plot

import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np;
from mpl_toolkits import mplot3d;
from sklearn.preprocessing import PolynomialFeatures;
from sklearn.pipeline import Pipeline;
from sklearn import linear_model as lm; 
from sklearn import metrics as mt;

dfraw = pd.read_csv("qiutable2merged.csv");
df = dfraw[dfraw['PreAge'] < 2.0]; #filter old stars out

#ra = np.radians(df['RAdeg']);
#dec = np.radians(df['DEdeg']);
l = df['l'];
b = df['b'];
plx = df['plx'];
tau = df['PreAge'];

r = 1/plx;
ltau = np.log10(1000000000*tau);
#convert to spherical coordinates
    
theta = (np.pi/2) - np.radians(b);
    
#convert to cartesian coordinates
x = r * np.cos(np.radians(l)) * np.sin(theta);
y = r * np.sin(np.radians(l)) * np.sin(theta);
z = r * np.cos(theta);

coords = list(zip(x, y, z));

#poly = PolynomialFeatures(degree=3);
#trfm = poly.fit_transform(coords);

regr = lm.LinearRegression();
regr.fit(coords, ltau);
#Input = [('polynomial',PolynomialFeatures(degree=2)),('modal',lm.LinearRegression())];
#regr = Pipeline(Input);
#regr.fit(coords, ltau);
pred = regr.predict(coords);
r2 = mt.r2_score(pred, ltau);
mse = mt.mean_squared_error(pred, ltau);

#coef = regr.coef_;
#intr = regr.intercept_;

#print(coef);
#print(intr);

print("tau(x, y, z) = ",
      regr.intercept_,
      " + ",
      regr.coef_[0],
      "x + ",
      regr.coef_[1],
      "y + ",
      regr.coef_[2],
      "z",
      sep='');
print("MSE = ",mse);
print("r2 = ",r2);