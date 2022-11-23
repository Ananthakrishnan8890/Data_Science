import pandas as pd
import statsmodels.api as sm

 
dataset = pd.read_csv('Salary_Data.csv')
print("First five lines",dataset.head())
X = dataset.iloc[:,:-1].values  #independent variable array
y = dataset.iloc[:,1].values  #dependent variable vector

lmregmodel = sm.OLS(y,X)
result = lmregmodel.fit()
print(result.summary())