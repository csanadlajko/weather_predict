from meteostat import Point, Daily
from utils.DateFunctions import DateFunctions
from utils.LocationFunctions import LocationFunctions
import pandas as pd
from models.weather_model import WeatherData, WindData, SunData


interval: DateFunctions = DateFunctions()
target_city_model: LocationFunctions = LocationFunctions()
target_city_point: Point = Point(target_city_model.latitude, target_city_model.longitude)

data: Daily = Daily(target_city_point, interval.start_date, interval.end_date)
df_data: pd.DataFrame = data.fetch()

df_data = df_data.reset_index() # <-- set time as first column

weather_data: WeatherData = WeatherData(
    date=df_data['time'],
    avg_temperature=df_data['tavg'],
    min_temperature=df_data['tmin'],
    max_temperature=df_data['tmax'],
    snow=df_data['snow']
)

wind_data: WindData = WindData(
    wind_speed=df_data['wspd'],
    wind_peak_gust=df_data['wpgt'],
    wind_direction=df_data['wdir']
)

sun_data: SunData = SunData(
    sunny_hours=df_data['tsun']
)
