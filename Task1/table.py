class Table:
    def __init__(self, tableid, capacity):
        self._tableid = tableid
        self._capacity = capacity
        self._location = self._location(capacity)
        self._reservations = []  #use list store reservation data

    #People >=8 assign to VIP Room, otherwise assign to Hall
    def _location(self, capacity):
        if capacity >= 8:
            return "VIP Room"
        return "Hall"

    #Encapsulation
    @property
    def tableid(self):
        return self._tableid

    @property
    def capacity(self):
        return self._capacity

    @property
    def location(self):
        return self._location

    def add_reservation(self, reservation):
        self._reservations.append(reservation)

    #Check if the booking times is overlap
    def is_available(self, start_time, end_time):
        for reservation in self._reservations:
            if reservation.status == "Active" and reservation.overlaps(start_time, end_time):
                return False
        return True

    def __str__(self): 
        return f"Table ID: {self._tableid}, Capacity: {self._capacity}, Location: {self._location}"