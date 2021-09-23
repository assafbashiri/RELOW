from datetime import datetime

class Utils:
    def string_to_datetime_with_hour(self, str_date):
        return datetime.strptime(str_date, '%d/%m/%y %H:%M:%S')
    def string_to_datetime_without_hour(self, str_date):
        return datetime.strptime(str_date, "%Y-%m-%d")
