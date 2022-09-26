a_string = input()
lower_message = a_string.lower()
print(sum(lower_message.count(x) for x in ("sand", "water", "fish", "sun")))








