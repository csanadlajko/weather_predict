import datetime

class DateFunctions():
    COMMON_DATE_FORMAT: str = "%Y.%m.%d"
    
    def parseStringDate(string_date: str) -> datetime.datetime:
        """
        Parses date if its format matches %Y.%m.%d.
        """
        try:
            parsed_date: datetime.datetime = datetime.datetime.strptime(string_date, DateFunctions.COMMON_DATE_FORMAT)
            return parsed_date
        except Exception as e:
            print(f"Couldn't parse date, an error has occured: {e}")