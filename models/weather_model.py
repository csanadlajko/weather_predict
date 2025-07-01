from dataclasses import dataclass
from datetime import date

@dataclass(slots=True)
class Weather:
    date: date
    temperature: float
    humidity: float
    