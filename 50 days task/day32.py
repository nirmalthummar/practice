# #### ### ## # TASK 1 # ## ### ####

# def password_validator():
#     while True:
#         password = input("Enter a password: ")

#         # Check password criteria
#         errors = []
#         if len(password) < 8:
#             errors.append("Password should be at least 8 characters long.")
#         if not any(char.isupper() for char in password):
#             errors.append("Password should have at least one uppercase letter.")
#         if not any(char.islower() for char in password):
#             errors.append("Password should have at least one lowercase letter.")
#         if not any(char.isdigit() for char in password):
#             errors.append("Password should have at least one digit.")

#         # Check if password is valid
#         if not errors:
#             return password
#         else:
#             print("Invalid password. Please fix the following errors:")
#             for error in errors:
#                 print(error)

# # Test the function
# valid_password = password_validator()
# print("Valid password:", valid_password)


# ##### ### TASK 2 ### ### ## #


def email_validator(emails):
    valid_emails = []
    for email in emails:
        if '@' not in email or email.startswith('@') or email.count('@') > 1:
            continue
        domain = email.split('@')[1]
        if domain.endswith('.com'):
            valid_emails.append(email)
    if not valid_emails:
        return 'all emails are invalid'
    return valid_emails

# Test the function
emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']
valid_emails = email_validator(emails)
print(valid_emails)


### ## # SECOND WAY ### ## #


def email_validator(emails):
    valid_emails = [email for email in emails if '@' in email and not email.startswith('@') and email.count('@') == 1 and email.split('@')[1].endswith('.com')]
    if not valid_emails:
        return 'all emails are invalid'
    return valid_emails

# Test the function
emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']
valid_emails = email_validator(emails)
print(valid_emails)


##### ##3 ## # THIRD  WAYYYY ##### ### ## #


def email_validator(emails):
    valid_emails = []
    
    for email in emails:
        if '@' in email and not email.startswith('@') and email.count('@') == 1 and email.split('@')[1].endswith('.com'):
            valid_emails.append(email)
    
    if not valid_emails:
        return 'all emails are invalid'
    return valid_emails

# Test the function
emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']
valid_emails = email_validator(emails)
print(valid_emails)

