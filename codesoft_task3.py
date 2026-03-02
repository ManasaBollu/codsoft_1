import random
import string
def generate_password(length, use_uppercase = True, use_number = True, use_special_chars = True):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ""
    number = string.digits if use_number else ""
    special_chars = string.punctuation if use_special_chars else ""
    all_chars = lowercase_letters + uppercase_letters + number + special_chars
    if not all_chars:
        raise ValueError("at least one charactor set must be enabled")
    password = "".join(random.choice(all_chars)for _ in range(length))
    return password
def main():
    length = int(input("enter the desired length of the pasword : "))
    use_uppercase = input("use uppercase letter? (y/n): ").lower() == "y"
    use_numbers = input("use numbers? (y/n): ").lower() == "y"
    use_special_chars = input("use special characters? (y/n):").lower() == "y"
    try:
        password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
        print(f"generated password: {password}")
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()
