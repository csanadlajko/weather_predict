from geopy.geocoders import Nominatim
from utils.CommonConstants import CommonConstants

class LocationFunctions:
    GEOLOCATOR: Nominatim = Nominatim(user_agent="USER_AGENT")
    
    def __init__(self, city_name: str = CommonConstants.CITY_NAME):
        self.city_name = city_name
        location_details = LocationFunctions.GEOLOCATOR.geocode(self.city_name)
        self.latitude = location_details.latitude
        self.longitude = location_details.longitude