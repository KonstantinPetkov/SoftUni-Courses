import re

some_text = input()
first_pattern = r'(?:<title>)([\w\s].+)(?:<\/title>).*(?:<body>)([\w\s].+)(?:<\/body>)'
result_first_pattern = re.search(first_pattern, some_text)

pattern_spaces = r'[ ]+'
sub_pattern_spaces = re.sub(pattern_spaces, " ", result_first_pattern)

pattern_tabs = r'\\n'
sub_pattern_tabs = re.sub(pattern_tabs, "", sub_pattern_spaces)

pattern_all_tags = r'<[^>]*>'
sub_pattern_tags = re.sub(pattern_all_tags, "", sub_pattern_tabs)

print(result_first_pattern)
print(sub_pattern_spaces)
print(sub_pattern_tabs)
print(sub_pattern_tags)



# print(f'Title: {extracted title}')
# print(f'Content: {extracted content}')







# for email in valid_emails:
#     print(email)
