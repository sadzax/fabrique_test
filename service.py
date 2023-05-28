import datetime

#  Создаём класс рассылки
class Mailing:
    def __init__(self, id, date_start, message, filters, date_stop):
        #  Устанавливаем базовые параметры
        self.id = id
        self._date_start = None
        self.date_start = date_start
        self.message: str = message
        self.filters = filters
        self._date_stop = date_stop
        self.date_stop = date_stop

    @property
    def date_start(self):
        return self._date_start

    @property
    def date_stop(self):
        return self._date_stop

    @date_start.setter
    def date_start(self, value):
        value = datetime.datetime.strptime(value, '%Y/%m/%d %H:%M:%S')
        self._date_start = value

    @date_stop.setter
    def date_stop(self, value):
        value = datetime.datetime.strptime(value, '%Y/%m/%d %H:%M:%S')
        self._date_stop = value



