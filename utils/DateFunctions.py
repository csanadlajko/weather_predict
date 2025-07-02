import datetime
from utils.CommonConstants import CommonConstants

class DateFunctions():
    COMMON_DATE_FORMAT: str = "%Y.%m.%d"
    TODAY: int = datetime.datetime.today().day
    CURRENT_MONTH: int = datetime.datetime.today().month
    
    def __init__(self, start_date: str = CommonConstants.START_DATE, end_date: str = CommonConstants.END_DATE):
        self.start_date = self.parseStringDate(start_date)
        self.end_date = self.parseStringDate(end_date)
    
    def parseStringDate(self, string_date: str) -> datetime:
        """
        Parses date if its format matches %Y.%m.%d.
        """
        try:
            parsed_date: datetime = datetime.datetime.strptime(string_date, DateFunctions.COMMON_DATE_FORMAT)
            return parsed_date
        except Exception as e:
            print(f"Couldn't parse date, an error has occured: {e}")