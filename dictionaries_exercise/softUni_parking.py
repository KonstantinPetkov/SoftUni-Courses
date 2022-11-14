def register_car(username, license):
    if username in parking.keys():
        print(f"ERROR: already registered with plate number {parking[username]}")
    else:
        parking[username] = license
        print(f"{username} registered {parking[username]} successfully")

def unregister_car(username):
    if username not in parking.keys():
        print(f"ERROR: user {username} not found")
    else:
        del parking[username]
        print(f"{username} unregistered successfully")

car_numbers = int(input())
parking = {}

for num in range(car_numbers):
    cars = input().split()
    command = cars[0]
    name = cars[1]
    if command == "register":
        number = cars[2]
        register_car(name, number)
    else:
        unregister_car(name)

for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")