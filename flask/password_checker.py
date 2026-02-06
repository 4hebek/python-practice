# class

# obj built with password param
 
# 1 method returns a string. 

# check against a know list of exposed passwords.
#     - if match auto return very weak. 

# very strong
# strong 
# medium
# weak
# very weak

class PasswordChecker:
    def __init__(self, password):
        self.password = password

    def check_strength(self):
        exposed_passwords = ["password", "123456", "qwerty", "abc123", "letmein"]

        if self.password.lower() in exposed_passwords:
            return "Very Weak"

        if (
            len(self.password) >= 12
            and any(c.isupper() for c in self.password)
            and any(c.islower() for c in self.password)
            and any(c.isdigit() for c in self.password)
            and any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in self.password)
        ):
            return "Very Strong"

        if (
            len(self.password) >= 8
            and any(c.isupper() for c in self.password)
            and any(c.islower() for c in self.password)
            and any(c.isdigit() for c in self.password)
        ):
            return "Strong"

        if (
            len(self.password) >= 6
            and any(c.isupper() for c in self.password)
            and any(c.islower() for c in self.password)
        ):
            return "Medium"

        if len(self.password) >= 6:
            return "Weak"

        return "Very Weak"
