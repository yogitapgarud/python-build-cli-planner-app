from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable
from dateutil.parser import parse
from datetime import datetime

class DeadlinedReminder(ABC, Iterable):
    @abstractmethod
    def is_due(self):
        pass

class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):
    @abstractmethod
    def is_due(self):
        pass

class DateReminder(DeadlinedReminder):
    def __init__(self, text, date) -> None:
        self.date = parse(date, dayfirst=True)
        self.text = text

    def __iter__(self):
        return iter([self.text, self.date.isoformat()])

    def is_due(self):
        return self.date < datetime.now()