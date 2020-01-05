def number_of_available_passwords(range_start, range_end):
    return [validate_password(str(password)) for password in range(range_start, range_end + 1)].count(True)


def validate_password(password):
    return all([has_double_digits(password), has_only_increasing_digits(password)])


def has_only_increasing_digits(password):
    last_digit = '0'
    for digit in password:
        if int(digit) < int(last_digit):
            return False
        last_digit = digit
    return True


def has_double_digits(password):
    return any([validate_double(password, str(digit)) for digit in range(0, 10)])


def validate_double(string_password, string_digit):
    return string_digit + string_digit in string_password and string_password.count(string_digit) == 2


print(number_of_available_passwords(136760, 595730))