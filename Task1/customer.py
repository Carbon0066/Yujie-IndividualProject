from datetime import datetime


class Person:
    def __init__(self, name, phone):
        self._name = name
        self._phone = phone

    #Encapsulation
    @property
    def name(self):
        return self._name

    @property
    def phone(self):
        return self._phone

    def __str__(self):
        return f"Name: {self._name}, Phone: {self._phone}"


class Customer(Person):
    def __init__(self, customerid, name, phone):
        super().__init__(name, phone)
        self._customerid = customerid
        self._booking_history = []   # use list store booking Info

    @property
    def customerid(self):
        return self._customerid

    def add_booking_record(self, reservation): #record and use in menu 5 search
        self._booking_history.append(reservation)

    def get_booking_history(self, include_cancelled=True):        
        if include_cancelled:
            history = list(self._booking_history)
        else:
            history = [r for r in self._booking_history if r.status != "Cancelled"]

        #Use lambda , sort in start_time , first booking show first
        history.sort(key=lambda r: r.start_time)
        return history


    def __str__(self):
        return f"Customer ID: {self._customerid}, {super().__str__()}"
