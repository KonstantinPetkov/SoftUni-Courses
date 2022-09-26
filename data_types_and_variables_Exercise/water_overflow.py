number_of_lines = int(input())
water_tank = 255
capacity = 0
for current_line in range(number_of_lines):
    current_litters = int(input())
    if water_tank - current_litters < 0:
        print("Insufficient capacity!")
        continue
    water_tank -= current_litters
    capacity += current_litters

print(capacity)