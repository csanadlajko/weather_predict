from meteostat import Point, Daily
from utils.DateFunctions import DateFunctions
from utils.LocationFunctions import LocationFunctions
import pandas as pd


interval: DateFunctions = DateFunctions()
target_city_model: LocationFunctions = LocationFunctions()
target_city_point: Point = Point(target_city_model.latitude, target_city_model.longitude)

data: Daily = Daily(target_city_point, interval.start_date, interval.end_date)
df_data: pd.DataFrame = data.fetch()