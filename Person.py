import datetime


class Person:

    def __init__(self, name, surname, birthdate, address, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.email = email

        self._age = None
        self._age_last_recalculated = None

        self._recalculate_age()

    def _recalculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        self._age = age
        self._age_last_recalculated = today

    def age(self):
        if datetime.date.today() > self._age_last_recalculated:
            self._recalculate_age()

#

person = Person("Jane",
                "Doe",
                datetime.date(1992, 3, 12),
                "adrrrrr",
                "rubub@bubub.pl")

print(person.__dict__)
