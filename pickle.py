import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df=pd.read_csv(r"C:\Users\aadil khan\OneDrive\Desktop\Data Science\heart_failure_clinical_records_dataset.csv")
df.drop

x = df[['time']][0:100]
y = df[['smoking']][0:100]

model = LinearRegression()
model.fit(x, y)