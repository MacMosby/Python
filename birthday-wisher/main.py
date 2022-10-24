import datetime as dt
import random
import smtplib
import pandas

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthday_dict = data.to_dict(orient="records")
print(birthday_dict)


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
year_today = now.year
month_today = now.month
day_today = now.day

for person in birthday_dict:
    year = person["year"]
    month = person["month"]
    day = person["day"]

    if month == month_today and day == day_today:
        letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        letter = random.choice(letters)
        with open(f"letter_templates/{letter}", "r") as text_data:
            mail = text_data.read()
            final_mail = mail.replace("[NAME]", person["name"])
            print(final_mail)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


# 4. Send the letter generated in step 3 to that person's email address.

        MY_EMAIL = "mrodenbusch.business@gmail.com"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password="gehtdichnichtsan")

            recipient_email = person["email"]
            print(recipient_email)

            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=recipient_email,
                msg=f"Subject:HAPPY BIRTHDAY!!!\n\n{final_mail}")





