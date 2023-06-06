##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas as pd

EMAIL = "luizsantos.github@gmail.com"
PASSWORD = "yazgjjicimkbdyml"


def send_email(message, recipient):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # make the connection secure
        connection.starttls()
        # login
        connection.login(user=EMAIL, password=PASSWORD)
        # send email
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=recipient,
            msg=f"Subject:Happy Birthday!\n\n{message}")


today_mth = dt.datetime.now().month
today_day = dt.datetime.now().day
letter_templates = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

# Load Birthday CSV
df = pd.read_csv('birthdays.csv')

for index, row in df.iterrows():

    # Check if today matches a birthday in the birthdays.csv
    if today_mth == row.month and today_day == row.day:
        print(f"Today is {row['name']}'s birthday! Let's send our greetings!")
        # Pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f'letter_templates/{random.choice(letter_templates)}') as letter_data:
            greeting_data = letter_data.readlines()
            greeting_msg = ''.join(greeting_data).replace("[NAME]", row['name'])
            send_email(message=greeting_msg, recipient=row['email'])
