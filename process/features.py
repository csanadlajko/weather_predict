import pandas as pd
import numpy as np
from data.weather_data import df_data
from utils.DateFunctions import DateFunctions

same_day_data: pd.DataFrame = df_data[(df_data['time'].dt.day == DateFunctions.TODAY) & (df_data['time'].dt.month == DateFunctions.CURRENT_MONTH)]

filtered_df: pd.DataFrame = same_day_data.drop(columns=["time", "wdir", "pres", "tsun", "snow"])

filtered_df = filtered_df.fillna(filtered_df.mean(numeric_only=True))

final_df = filtered_df.dropna(how='any')

## TODO: ADD MORE FEATURES FOR MORE ACCURATE RESULTS