number_of_cars = int(input())
cars = {}

for num in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    cars[car] = cars.get(car, {})
    cars[car]["Mileage"] = int(mileage)
    cars[car]["Fuel"] = int(fuel)


def drive(car_name, distance, car_fuel):
    if cars[car_name]["Fuel"] < int(car_fuel):
        print("Not enough fuel to make that ride")
    else:
        cars[car_name]["Mileage"] += int(distance)
        cars[car_name]["Fuel"] -= int(car_fuel)
        print(f"{car_name} driven for {distance} kilometers. {car_fuel} liters of fuel consumed.")
        if cars[car_name]["Mileage"] >= 100000:
            del cars[car_name]
            print(f"Time to sell the {car_name}!")


def refuel(name_of_car, fuel_of_car):
    if cars[name_of_car]["Fuel"] + int(fuel_of_car) > 75:
        fuel_of_car = 75 - cars[name_of_car]["Fuel"]
        cars[name_of_car]["Fuel"] = 75
    else:
        cars[name_of_car]["Fuel"] += int(fuel_of_car)
    print(f"{name_of_car} refueled with {fuel_of_car} liters")


def revert(name_of_car, kilometers):
    if cars[name_of_car]["Mileage"] - int(kilometers) < 10000:
        cars[name_of_car]["Mileage"] = 10000
    else:
        cars[name_of_car]["Mileage"] -= int(kilometers)
        print(f"{name_of_car} mileage decreased by {kilometers} kilometers")


while True:
    command = input()
    if command == "Stop":
        break
    splited_command = command.split(" : ")
    action = splited_command[0]
    if action == "Drive":
        car_d = splited_command[1]
        distance_d = splited_command[2]
        fuel_d = splited_command[3]
        drive(car_d, distance_d, fuel_d)
    elif action == "Refuel":
        car_rf = splited_command[1]
        fuel_rf = splited_command[2]
        refuel(car_rf, fuel_rf)
    elif action == "Revert":
        car_rv = splited_command[1]
        fuel_rv = splited_command[2]
        revert(car_rv, fuel_rv)

for car in cars.keys():
    print(f"{car} -> Mileage: {cars[car]['Mileage']} kms, Fuel in the tank: {cars[car]['Fuel']} lt.")




