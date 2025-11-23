# collect user preference
# length
# should contain uppercase
# should contain digits
# should have special characters

# get all available characters
# randomly pic charact upto length
# ensure we have atleast one of each character
# ensure length is valid

import random
import string

def generate_password():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Include uppercase letters? Yes/No: ").strip().lower()
    include_digits = input("Include digits? Yes/No: ").strip().lower()
    include_special_characters = input("Include special characters? Yes/No: ").strip().lower()

    if length < 4:
        print("Password length must be at least 4 characters.")
        return

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    special = string.punctuation if include_special_characters == "yes" else ""

    all_characters = lower + upper + digits + special

    # In case user selects nothing except lowercase
    if not all_characters:
        all_characters = lower

    required_characters = []

    if include_uppercase == "yes":
        required_characters.append(random.choice(upper))

    if include_digits == "yes":
        required_characters.append(random.choice(digits))

    if include_special_characters == "yes":
        required_characters.append(random.choice(special))

    # Remaining characters
    remaining_length = length - len(required_characters)

    password = required_characters.copy()

    for _ in range(remaining_length):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    final_password = "".join(password)
    print("Generated Password:", final_password)
    return final_password


# Call function
generate_password()
