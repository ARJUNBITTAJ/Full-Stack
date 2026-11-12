'''TASK3: Create a class Validator with a static method to validate user input, such as an email
address or phone number.
 Use @staticmethod to define the validation logic since it does not depend on
instance or class variables.'''

import re


class Validator:
    @staticmethod
    def is_valid_email(email):
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
        return re.match(email_pattern, email.strip())

    @staticmethod
    def is_valid_phone(phone):
        cleaned = re.sub(r"[\s\-\(\)]", "", phone)
        # Check if it consists of exactly 10 digits
        return re.fullmatch(r"\d{10}", cleaned)


test_emails = ["alex@example.com", "bad_email@", "user.name@sub.domain.co"]
for email in test_emails:
    result = Validator.is_valid_email(email)
    print(f"'{email}' is valid? {result}")

print()

test_phones = ["9876543210", "123-456-7890", "12345", "(555) 123-4567"]
for phone in test_phones:
    result = Validator.is_valid_phone(phone)
    print(f"'{phone}' is valid? {result}")