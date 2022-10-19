def check_availability(rooms):
    total_free_chairs = 0
    total_needed_chairs = 0
    for room in range(1, number_of_rooms + 1):
        chairs, visitors = input().split()
        diff = len(chairs) - int(visitors)
        if diff >= 0:
            total_free_chairs += diff
        else:
            total_needed_chairs += abs(diff)
            print(f"{abs(diff)} more chairs needed in room {room}")
    return total_free_chairs, total_needed_chairs


number_of_rooms = int(input())
free_chairs, needed_chairs = check_availability(number_of_rooms)
if free_chairs >= needed_chairs:
    print(f"Game On, {free_chairs} free chairs left")