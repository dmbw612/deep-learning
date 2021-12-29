"""
https://www.daleseo.com/python-property/
"""
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.set_age(age)

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self._age = age


bwmin = Person('Byungwook', 'Min', 32)


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.set_age(age)

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self._age = age


bwmin = Person('Byungwook', 'Min', 32)


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self._age = age

    age = property(get_age, set_age)


bwmin = Person('Byungwook', 'Min', 32)
