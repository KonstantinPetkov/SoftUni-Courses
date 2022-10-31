list_vehicals = input().split(">>")
total_tax = 0
for vehical in list_vehicals:
    element = vehical.split()
    car_type = element[0]
    years = int(element[1])
    kilometers = int(element[2])
    if car_type == "family":
        initial_tax = 12 * (kilometers // 3000) + (50 - years * 5)
        total_tax += initial_tax
        print(f"A {car_type} car will pay {initial_tax:.2f} euros in taxes.")
    elif car_type == "heavyDuty":
        initial_tax = 14 * (kilometers // 9000) + (80 - years * 8)
        total_tax += initial_tax
        print(f"A {car_type} car will pay {initial_tax:.2f} euros in taxes.")
    elif car_type == "sports":
        initial_tax = 18 * (kilometers // 2000) + (100 - years * 9)
        total_tax += initial_tax
        print(f"A {car_type} car will pay {initial_tax:.2f} euros in taxes.")
    else:
        print("Invalid car type.")


print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")

