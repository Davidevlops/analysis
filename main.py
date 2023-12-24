import pandas as pd
import statsmodels.api as sm
import patsy
import matplotlib.pyplot as plt

# Load data from Excel files
df_y = pd.read_csv('./sect3_health.csv',low_memory=False)
df_X = pd.read_csv('./sect13_income.csv')


combined_data = pd.concat([df_y,df_X], ignore_index=True )


missing_values = combined_data.isnull().sum()
print("missing_values",missing_values)
if missing_values.any():
    combined_data.fillna(combined_data.mean(), inplace=True)
    combined_data.dropna(inplace=True)