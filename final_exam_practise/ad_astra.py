import re

text = input()

pattern = r'([\|\#])([A-za-z\s]+)\1([\d]{2}[\/][\d]{2}[\/][\d]{2})\1([\d]+)\1'
matched = re.findall(pattern, text)
kcal_need_per_day = 2000
total_calories = 0
count_day = 0

if matched:
    for match, item in enumerate(matched):
        calories = int(item[3])
        total_calories += calories

    while total_calories >= kcal_need_per_day:
        total_calories -= kcal_need_per_day
        count_day += 1

print(f"You have food to last you for: {count_day} days!")
if matched:
    for match, item in enumerate(matched):
        print(f"Item: {item[1]}, Best before: {item[2]}, Nutrition: {item[3]}")
