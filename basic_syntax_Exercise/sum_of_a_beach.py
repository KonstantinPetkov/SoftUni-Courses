string = input()
lower_message = string.lower()
print(sum(lower_message.count(x) for x in ("sand", "water", "fish", "sun")))





