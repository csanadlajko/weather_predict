from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from process.features import final_df

X: pd.DataFrame = final_df.drop(columns=["tavg"])
Y: pd.DataFrame = final_df["tavg"]

lin_reg_model: LinearRegression = LinearRegression()

lin_reg_model.fit(X, Y)
y_pred = lin_reg_model.predict(X)

## TODO: SPLIT DATA, USE OTHER MODELS AS WELL