import pandas as pd
import statsmodels.formula.api as smf

# 1. Load your data
df = pd.read_csv('cleaned_data2020.csv')

# 2. (Optional) Inspect
print(df[['MONEYPY','HOUSEHOLDER_RACE','SCALEE']].head())

# 3. Specify the model using a formula:
#    - Treat MONEYPY as a continuous (ordinal) variable
#    - Treat HOUSEHOLDER_RACE as categorical via C()
#    - Include the interaction term with *
formula = 'SCALEE ~ MONEYPY * C(HOUSEHOLDER_RACE)'

# 4. Fit OLS
model = smf.ols(formula, data=df).fit()

# 5. View results
print(model.summary())
