import re

valid_emails = []
pattern = r'(w{3}\.[a-zA-Z0-9]+(\-[a-zA-Z0-9]+)*(\.[a-z]+)+)'
text = input()
while text:
    matches = re.search(pattern, text)
    if matches:
        valid_emails.append(matches.group(0))
    text = input()

for email in valid_emails:
    print(email)
