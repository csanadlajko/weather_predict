from dataclasses import dataclass
from datetime import date
from pandas import Float64Dtype

@dataclass(slots=True)
class WeatherData:
    date: date
    avg_temperature: Float64Dtype
    min_temperature: Float64Dtype
    max_temperature: Float64Dtype
    snow: Float64Dtype

@dataclass(slots=True)
class WindData:
    wind_speed: Float64Dtype
    wind_peak_gust: Float64Dtype
    wind_direction: Float64Dtype
    
@dataclass(slots=True)
class SunData:
    sunny_hours: Float64Dtype