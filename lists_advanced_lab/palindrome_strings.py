def check_palindrom(word):
    if word == word[::-1]:
        return word


words = input().split(' ')
palindrome = input()
list_of_palindroms = [word for word in words if check_palindrom(word)]
count_palindrom = list_of_palindroms.count(palindrome)

print(list_of_palindroms)
print(f'Found palindrome {count_palindrom} times')







