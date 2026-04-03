from system import ReservationSystem


#System menu
def print_menu():
    print("\n" + "=" * 60)
    print("        RESTAURANT SEAT RESERVATION SYSTEM")
    print("=" * 60)
    print("1. Add Customer")
    print("2. Add Table")
    print("3. Make Reservation")
    print("4. Cancel Reservation")
    print("5. Search Customer Booking History")
    print("6. List All Customers")
    print("7. List All Tables")
    print("8. Exit")
    print("=" * 60)


#Define testing data #Done
def pre_define_data(system): 
    try:
        system.add_table("T01", 2)
        system.add_table("T02", 4)
        system.add_table("T03", 10)

        system.add_customer("C001", "Zhang", "11111111")
        system.add_customer("C002", "Li", "22222222")
        system.add_customer("C003", "Wang", "33333333")
    except ValueError:
        pass


#menu1 add_customer #Done
def add_customer(system):
    print("\n--- Add Customer ---")
    customer_id = input("Enter customer ID (e.g. C005): ").strip()
    name = input("Enter customer name: ").strip()

    attempt = 0
    phone = None
    #Phone number validation 8 integer numbers, allow attempt 5 times
    while attempt < 5:
        phone_input = input("Enter Hong Kong phone number: ").strip()

        if phone_input.isdigit() and len(phone_input) == 8:
            phone = phone_input
            break
        else:
            attempt += 1
            print(f"Error: Need to use Hong Kong phone number, please try again.")

    if phone is None:
        return

    try:
        system.add_customer(customer_id, name, phone)
        print("Customer added successfully.")
    except ValueError as e:
        print(f"Error: {e}")


#menu2 add_table #Done
def add_table(system):
    print("\n--- Add Table ---")
    tableid = input("Enter table ID (e.g. T05): ").strip()

    max_attempts = 5 #Try max 5 times if enter the wrong capacity
    for attempt in range(1, max_attempts + 1):
        try:
            capacity = int(input("Enter table capacity: ").strip())
            break
        except ValueError:
            print(f"Error: Capacity must be an integer.")
            if attempt == max_attempts:
                return

    try:
        system.add_table(tableid, capacity)
        table = system.get_table(tableid)
        print("Table added successfully.")
        print(f"Location: {table.location}")
    except ValueError as e:
        print(f"Error: {e}")


#menu3 make_reservation #Done
def make_reservation(system):
    print("\n--- Make Reservation ---")
    customerid = input("Enter customer ID: ").strip()

    max_attempts = 5 #Try max 5 times if enter the wrong capacity
    for attempt in range(1, max_attempts + 1):
        try:
            guests = int(input("Enter number of guests: ").strip())
            break
        except ValueError:
            print("Error: Number of guests must be an integer.")
            if attempt == max_attempts:
                return

    print("Enter start time in format: YYYY-MM-DD HH:MM")
    start_str = input("Enter start time: ").strip()

    try:
        reservation = system.make_reservation(
            customerid=customerid,
            guests=guests,
            start_str=start_str
        )
        print("\nReservation created successfully.")
        print("Dining duration is 90 minutes.")
        print(reservation)
    except ValueError as e:
        print(f"Error: {e}")


#menu4 cancel_reservation #Done
def cancel_reservation(system):
    print("\n--- Cancel Reservation ---")
    reservationid = input("Enter reservation ID (e.g. R001): ").strip()

    try:
        reservation = system.cancel_reservation(reservationid)
        print("Reservation cancelled successfully.")
        print(reservation)
    except ValueError as e:
        print(f"Error: {e}")

#menu5 search_customer_booking_history #Done
def search_customer_booking_history(system):
    print("\n--- Search Customer Booking History ---")
    customer_id = input("Enter customer ID: ").strip()

    try:
        history = system.get_customer_booking_history(
            customer_id,
            include_cancelled=True
        )

        if not history:
            print("No booking history found.")
            return

        print(f"\nBooking History for Customer {customer_id}")
        print("-" * 60)

        for reservation in history:
            print(reservation)

    except ValueError as e:
        print(f"Error: {e}")

#menu6 list_all_customers #Done
def list_all_customers(system):
    print("\n--- All Customers ---")
    customers = system.get_all_customers()

    if not customers:
        print("No customers found.")
        return

    for customer in customers: #show all the customers record
        print(customer)

#menu7 list_all_tables #Done
def list_all_tables(system):
    print("\n--- All Tables ---")
    tables = system.get_all_tables()

    if not tables:
        print("No tables found.")
        return

    for table in tables:    #show all the tables record
        print(table)


def main():
    system = ReservationSystem()
    pre_define_data(system)     #load pre define data

    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_customer(system)
        elif choice == "2":
            add_table(system)
        elif choice == "3":
            make_reservation(system)
        elif choice == "4":
            cancel_reservation(system)
        elif choice == "5":
            search_customer_booking_history(system)
        elif choice == "6":
            list_all_customers(system)
        elif choice == "7":
            list_all_tables(system)
        elif choice == "8":
            print("Thank you for using this system!")
            break
        else:
            print("Invalid choice. Please enter a number from 1-8.")


if __name__ == "__main__":
    main()