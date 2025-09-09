def book(booked, seat, total):
    if seat < 1 or seat > total:
        print(f"Seat {seat} is invalid.")
    elif seat in booked:
        print(f"Seat {seat} is already booked.")
    else:
        booked.append(seat)
        print(f"Seat {seat} booked successfully.")
    return booked
def cancel(booked, seat):
    if seat in booked:
        booked.remove(seat)
        print(f"Seat {seat} canceled successfully.")
    else:
        print(f"Seat {seat} is not booked yet.")
    return booked
def available(total, booked):
    return [s for s in range(1, total + 1) if s not in booked]

total_seats = int(input("Enter total number of seats in the cinema hall: "))
booked_seats = []

while True:
    print("1. Book a seat")
    print("2. Cancel a seat")
    print("3. View available seats")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        seat = int(input("Enter seat number to book: "))
        booked_seats = book(booked_seats, seat, total_seats)
    elif choice == 2:
        seat = int(input("Enter seat number to cancel: "))
        booked_seats = cancel(booked_seats, seat)
    elif choice == 3:
        print("Available seats:", available(total_seats, booked_seats))
    elif choice == 4:
        print("Exiting booking system. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")