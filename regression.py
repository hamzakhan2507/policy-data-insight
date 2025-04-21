import pandas as pd
import statsmodels.api as sm
from statsmodels.miscmodels.ordinal_model import OrderedModel

# Load
df = pd.read_csv('cleaned_data2020.csv')
# Prepare
df['race_cat'] = df['HOUSEHOLDER_RACE'].astype('category')
df['income_cat'] = df['MONEYPY'].astype('category')

# Exogenous: get dummies for income & race
exog = pd.get_dummies(df[['income_cat','race_cat']], drop_first=True)
# Fit
ordmod = OrderedModel(df['SCALEE'], exog, distr='logit')
ordres = ordmod.fit(method='bfgs')
print(ordres.summary())
