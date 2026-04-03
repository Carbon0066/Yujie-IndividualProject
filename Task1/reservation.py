class Reservation:
    def __init__(self, reservationid, customer, table, start_time, end_time, guests):
        self._reservationid = reservationid
        self._customer = customer
        self._table = table
        self._start_time = start_time
        self._end_time = end_time
        self._guests = guests
        self._status = "Active"   # Active / Cancelled

    #Encapsulation
    @property
    def reservationid(self):
        return self._reservationid

    @property
    def customer(self):
        return self._customer

    @property
    def table(self):
        return self._table

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def guests(self):
        return self._guests

    @property
    def status(self):
        return self._status

    def overlaps(self, other_start, other_end):
        # Overlap if start < other_end and other_start < end
        return self._start_time < other_end and other_start < self._end_time

    def cancel(self): #menu 4
        self._status = "Cancelled"

    def __str__(self):
        return (
            f"[{self._reservationid}] Customer: {self._customer.name}, "
            f"Table: {self._table.tableid}, Guests: {self._guests}, "
            f"Start: {self._start_time.strftime('%Y-%m-%d %H:%M')}, "
            f"End: {self._end_time.strftime('%Y-%m-%d %H:%M')}, "
            f"Status: {self._status}"
        )
