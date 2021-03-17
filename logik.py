from datetime import date


class Checker:
    """
        Класс для валидация различных данных
        Паспортов, иннов и т.п.
        # TODO
    """
    def check_date(self, year, month, day):
        try:
            birth_date = date(year=year, month=month, day=day)
        except:
            return False
        return True
