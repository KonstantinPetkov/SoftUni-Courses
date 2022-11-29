import re

number_of_message = int(input())
pattern_decrypted_message = r'@([A-Za-z]+)([^\@\-\!\:\>]*):([\d]+)([^\@\-\!\:\>]*)!([A-Z])!([^\@\-\!\:\>]*)->([\d]+)'
attacked_planets = 0
destroyed_planets = 0
attacked_planets_list = []
destryed_planets_list = []

for num in range(number_of_message):
    message = input()
    pattern_count = r'[star]'
    decrypt_mesage = len(re.findall(pattern_count, message.lower()))
    decode_decrypt_mesage = ''.join(chr(ord(char) - decrypt_mesage) for char in message)
    matched = re.search(pattern_decrypted_message, decode_decrypt_mesage)
    if matched:
        if matched.group(5) == "A":
            attacked_planets += 1
            attacked_planets_list.append(matched.group(1))
        elif matched.group(5) == "D":
            destroyed_planets += 1
            destryed_planets_list.append(matched.group(1))

sorted_attacked_planets_list = sorted(attacked_planets_list)
sorted_destryed_planets_list = sorted(destryed_planets_list)

print(f"Attacked planets: {attacked_planets}")
if attacked_planets > 0:
    for planet in sorted_attacked_planets_list:
        print(f"-> {planet}")

print(f"Destroyed planets: {destroyed_planets}")
if destroyed_planets > 0:
    for planet in sorted_destryed_planets_list:
        print(f"-> {planet}")



