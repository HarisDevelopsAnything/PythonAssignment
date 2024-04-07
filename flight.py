# Define a dictionary to store flight details
flights = {
    "FL001": {"flight_number": "FL001", "departure_city": "New York", "arrival_city": "Los Angeles", "departure_time": "10:00 AM", "availableSeats": 100},
    "FL002": {"flight_number": "FL002", "departure_city": "Los Angeles", "arrival_city": "Chicago", "departure_time": "12:00 PM", "availableSeats": 150},
    "FL003": {"flight_number": "FL003", "departure_city": "Chicago", "arrival_city": "Houston", "departure_time": "2:00 PM", "availableSeats": 120},
    "FL004": {"flight_number": "FL004", "departure_city": "Houston", "arrival_city": "New York", "departure_time": "4:00 PM", "availableSeats": 200},
}

# Define a dictionary to store booking details
bookings = {}

# Function to display menu and get user choice
def displayMenu():
    print("\nMenu:")
    print("a. View Available Flights")
    print("b. Search for Flights")
    print("c. Book a Flight")
    print("d. Cancel a Reservation")
    print("e. View Booked Flights")
    print("x. Exit")
    choice = input("Enter your choice (a, b, c, d, e, x): ")
    return choice.lower()

# Function to view available flights
def viewAvailableFlights():
    print("\nAvailable Flights:")
    print("Flight No. | Departure City | Arrival City | Departure Time | Available Seats")
    for flightId, flightInfo in flights.items():
        print(f"{flightInfo['flight_number']} | {flightInfo['departure_city']} | {flightInfo['arrival_city']} | {flightInfo['departure_time']} | {flightInfo['availableSeats']}")

# Function to search for flights
def searchFlights():
    searchKey = "_".join(input("Enter search criteria (departure city, arrival city, departure time): ").lower().split(sep=" "))
    searchValue = input("Enter search value: ")
    foundFlights = []
    for flightId, flightInfo in flights.items():
        if flightInfo[searchKey] == searchValue:
            foundFlights.append(flightInfo)
    if foundFlights:
        print("\nSearch Results:")
        print("Flight No. | Departure City | Arrival City | Departure Time | Available Seats")
        for flight in foundFlights:
            print(f"{flight['flight_number']} | {flight['departure_city']} | {flight['arrival_city']} | {flight['departure_time']} | {flight['availableSeats']}")
    else:
        print("No flights found.")

# Function to book a flight
def bookFlight():
    print("\nAvailable Flights:")
    print("Flight No. | Departure City | Arrival City | Departure Time | Available Seats")
    for flightId, flightInfo in flights.items():
        print(f"{flightInfo['flight_number']} | {flightInfo['departure_city']} | {flightInfo['arrival_city']} | {flightInfo['departure_time']} | {flightInfo['availableSeats']}")

    flight_number = input("Enter the flight number you want to book: ")
    numSeats = int(input("Enter the number of seats you want to book: "))
    if flight_number in flights:
        if flights[flight_number]["availableSeats"] >= numSeats:
            passengerName = input("Enter passenger name: ")
            bookingId = len(bookings) + 1
            bookings[bookingId] = {
                "passengerName": passengerName,
                "flight_number": flight_number,
                "departure_city": flights[flight_number]["departure_city"],
                "arrival_city": flights[flight_number]["arrival_city"],
                "departure_time": flights[flight_number]["departure_time"],
                "numSeats": numSeats,
            }
            flights[flight_number]["availableSeats"] -= numSeats
            print(f"Booking successful for {numSeats} seats on flight {flight_number}.")
            print(f"Booking ID: {bookingId}")
        else:
            print("Insufficient seats available.")
    else:
        print("Flight not found.")

# Function to cancel a reservation
def cancelReservation():
    bookingId = int(input("Enter the booking ID you want to cancel: "))
    if bookingId in bookings:
        flight_number = bookings[bookingId]["flight_number"]
        numSeats = bookings[bookingId]["numSeats"]
        flights[flight_number]["availableSeats"] += numSeats
        print(f"Reservation cancelled for booking ID {bookingId}.")
        del bookings[bookingId]
    else:
        print("Booking ID not found.")

# Function to view booked flights
def viewBookedFlights():
    print("\nBooked Flights:")
    print("Booking ID | Passenger Name | Flight No. | Departure City | Arrival City | Departure Time | Num Seats")
    for bookingId, bookingInfo in bookings.items():
        print(f"{bookingId} | {bookingInfo['passengerName']} | {bookingInfo['flight_number']} | {bookingInfo['departure_city']} | {bookingInfo['arrival_city']} | {bookingInfo['departure_time']} | {bookingInfo['numSeats']}")

# Main program loop
while True:
    choice = displayMenu()
    if choice == 'a':
        viewAvailableFlights()
    elif choice == 'b':
        searchFlights()
    elif choice == 'c':
        bookFlight()
    elif choice == 'd':
        cancelReservation()
    elif choice == 'e':
        viewBookedFlights()
    elif choice == 'x':
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
