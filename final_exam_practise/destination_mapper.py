import re

some_places = input()

pattern = r'([\=\/])([A-Z][a-zA-Z]{2,})\1'
matched_locations = re.findall(pattern, some_places)
travel_points = 0
valid_destinations = ()
for match, item in enumerate(matched_locations):
    travel_points += len(item[1])
    valid_destinations += (item[1],)

print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {travel_points}")


# ---Do with list()---
# valid_destinations = list()
# for match in matched_locations:
#     travel_points += len(match[1])
#     valid_destinations.append(match[1])