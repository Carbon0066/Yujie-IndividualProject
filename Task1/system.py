from datetime import datetime, timedelta
from customer import Customer
from table import Table
from reservation import Reservation


class ReservationSystem:
    DINING_TIME = 90  #Set default dining time is 90 mins

    # use dict to store the data
    def __init__(self):
        self._customers = {}
        self._tables = {}
        self._reservations = {}
        self._reservation_counter = 1


    # Add_table Management  ----table.py
    def add_table(self, tableid, capacity): #menu 2
        if tableid in self._tables:
            raise ValueError("Table ID already exists.")
        self._tables[tableid] = Table(tableid, capacity)

    def get_table(self, tableid):
        return self._tables.get(tableid)

    def get_all_tables(self):       #menu 7
        return list(self._tables.values())


    # Add_customer Management  ----customer.py
    def add_customer(self, customerid, name, phone): #menu1
        if customerid in self._customers:
            raise ValueError("Customer ID already exists.")
        self._customers[customerid] = Customer(customerid, name, phone)

    def get_customer(self, customerid):
        return self._customers.get(customerid)

    def get_all_customers(self):      #menu6
        return list(self._customers.values())


    # Define reservation function Core
    def generate_reservationid(self): #Reservation ID auto accumulate
        reservationid = f"R{self._reservation_counter:03d}"
        self._reservation_counter += 1
        return reservationid

    def parse_datetime(self, dt_str): #Transfer string to datatime
        return datetime.strptime(dt_str, "%Y-%m-%d %H:%M")

    def find_table(self, guests, start_time, end_time): #core function find table
        suitable_tables = []

        for table in self._tables.values(): #time is not occupied
            if table.capacity >= guests and table.is_available(start_time, end_time):
                suitable_tables.append(table)

        if not suitable_tables:
            return None

        # use lambda choose the smallest suitable table
        suitable_tables.sort(key=lambda t: t.capacity)
        return suitable_tables[0]
    

    # Make_reservation Management  ----reservation.py
    def make_reservation(self, customerid, guests, start_str):
        customer = self.get_customer(customerid)
        if not customer:
            raise ValueError("Customer not found.")

        start_time = self.parse_datetime(start_str)
        end_time = start_time + timedelta(minutes=self.DINING_TIME)

        table = self.find_table(guests, start_time, end_time)
        if not table:
            raise ValueError("No available table in the requested time and guests.")

        reservationid = self.generate_reservationid()
        reservation = Reservation(reservationid, customer, table, start_time, end_time, guests) #save format

        self._reservations[reservationid] = reservation #save in dict
        table.add_reservation(reservation)              #save in table list
        customer.add_booking_record(reservation)        #save in customer list

        return reservation

    #Cancel_reservation Management
    def cancel_reservation(self, reservationid):
        reservation = self._reservations.get(reservationid)
        if not reservation:
            raise ValueError("Reservation not found.")

        if reservation.status == "Cancelled":
            raise ValueError("Reservation is already cancelled.")

        reservation.cancel()
        return reservation
    
    
    #Search_customer_booking_history
    def get_customer_booking_history(self, customerid, include_cancelled=True):
        customer = self.get_customer(customerid)
        if not customer:
            raise ValueError("Customer not found.")
        return customer.get_booking_history(include_cancelled=include_cancelled)