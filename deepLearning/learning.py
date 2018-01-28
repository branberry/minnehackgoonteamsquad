import numpy as np
import pandas as pd
import statsmodels.api as sm


#load all data from our injuries file
data = pd.read_csv("ConcussionOnly3.csv")
# set X and Y where X is our data classifiers (age, weight and height) and Y (return time) is the predition
X = data.iloc[:, 2:5].values
Y = data.iloc[:,37]
df = pd.DataFrame(X,columns=['Age','Height', 'Weight'])
df['Recovery'] = pd.Series(Y)
#print(df)
# X_1=sm.add_constant(X)
# results=sm.OLS(Y,X_1).fit()
# results.params
# print(results.params)

from mpl_toolkits.mplot3d import Axes3D
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
model = smf.ols(formula='Recovery ~ Age + Height + Weight', data=df)
results_formula = model.fit()
results_formula.params
print(results_formula.params)
x_surf, y_surf = np.meshgrid(np.linspace(df2.Age.min(), df2.Age.max(), 100),np.linspace(df2.Height.min(), df2.Height.max(), 100),np.linspace(df2.Weight.min(), df2.Weight.max(), 100))
onlyX = pd.DataFrame({'Age': x_surf.ravel(), 'Height': y_surf.ravel(), 'Weight': y_surf.ravel
fittedY=results_formula.predict(exog=onlyX)
