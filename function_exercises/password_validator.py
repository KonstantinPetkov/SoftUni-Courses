def validate_pass(current_pass):
    password_valid = True
    if len(password) < 6 or len(password) > 10:
        password_valid = False
        print("Password must be between 6 and 10 characters")
    elif not current_pass.isalnum():
        password_valid = False
        print("Password must consist only of letters and digits")
    digit_counter = 0
    for element in current_pass:
        if element.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        password_valid = False
        print("Password must have at least 2 digits")

    return password_valid



password = input()
pass_is_valid = validate_pass(password)
if pass_is_valid:
    print("Password is valid")