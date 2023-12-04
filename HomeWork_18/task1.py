import re

class UserEmail:
    def __init__(self, email):
        self.validate_email(email)
        self.email = email

    @classmethod
    def validate_email(cls, email):
        if not re.match(r"^[a-zA-Z0-9](?:[a-zA-Z0-9._-]*[a-zA-Z0-9])?@[a-zA-Z](?:[a-zA-Z.-]*[a-zA-Z])*\.[a-zA-Z]{2,}$", email):
            raise ValueError("Invalid email address")
        else:
            print('Good email')

UserEmail.validate_email("abc@mail.com")