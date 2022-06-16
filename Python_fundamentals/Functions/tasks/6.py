def pass_validator(password):
    is_valid = True

    if not (6 <= len(password) <= 10):
        is_valid = False
        print("Password must be between 6 and 10 characters")

    if not password.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")

    counter_digits = 0

    for el in pass_input:
        if el.isdigit():
            counter_digits += 1

    if counter_digits < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    return is_valid


pass_input = input()
is_valid = pass_validator(pass_input)

if is_valid:
    print("Password is valid")
