import csv

def save_emails():
    emails = []
    while True:
        email = input("Enter an email address (or 'done' to finish): ")
        if email == 'done':
            break
        emails.append(email)

    with open('emails.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([[email] for email in emails])

    print("Emails saved successfully.")

def open_emails():
    with open('emails.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0])

# Usage example
save_emails()
open_emails()
