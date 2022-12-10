
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/Users/sudachk/Packt/churn-bigml-80.csv',na_values=-999)

print(df.columns)

print(df.types)