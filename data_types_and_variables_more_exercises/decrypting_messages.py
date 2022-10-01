from base64 import encode

key = int(input())
number_of_lines = int(input())

for current_number in range(number_of_lines):
    character = input()
    results = {}
    results.update({key:character})
    encoded = encode(results, "password")
    print(encoded)