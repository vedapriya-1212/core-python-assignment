def fare(distance):
    base = 50
    distance_fare = 10 * distance
    return base + distance_fare
trips = []
n = int(input("Enter number of trips: "))

for i in range(n):
    d = int(input(f"Enter distance (in km) for trip {i+1}: "))
    trips.append(d)
total_fare = 0
for i, d in enumerate(trips, start=1):
    f = fare(d)
    total_fare += f
    print(f"Trip {i}: ${f}")

print(f"Total Fare: ${total_fare}")