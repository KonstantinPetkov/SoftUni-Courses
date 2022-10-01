prime_number = int(input())
is_number_prime = False
if prime_number > 1:
    for current_number in range(2, prime_number):
        if (prime_number % current_number) == 0:
            is_number_prime = True
            break
if not is_number_prime:
    print("True")
else:
    print("False")







