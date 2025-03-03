def validate_password(some_text: str) -> str:
    validation_output = []

    # check string length
    if not 6 <= len(some_text) <= 10:
        validation_output.append("Password must be between 6 and 10 characters")

    # check if 2 digits are present
    counter = 0
    for i in some_text:
        if i.isdigit():
            counter += 1
    if counter < 2:
        validation_output.append("Password must have at least 2 digits")

    # check if string is alphanumeric
    if not some_text.isalnum():
        validation_output.append("Password must consist only of letters and digits")

    if validation_output:
        return "\n".join(validation_output)
    else:
        return "Password is valid"


password = input()

result = validate_password(password)
print(result)
