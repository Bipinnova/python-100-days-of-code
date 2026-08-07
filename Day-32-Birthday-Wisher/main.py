from datetime import datetime as dt
import random
import pandas as pd
import smtplib

MY_EMAIL = "bipininfo6826@gmail.com"
MY_PASSWORD = "ckry hbph ovlx belh"

today = dt.now()
#print(f"0:\n {today}")
today_tuple = (today.month, today.day)
#print(f"1:\n {today_tuple}")

# 1. Update the birthdays.csv

data = pd.read_csv("birthdays.csv")
#print(f"2:\n {data}")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
#print(f"3:\n {birthdays_dict}")


# 2. Check if today matches a birthday in the birthdays.csv

if today_tuple in birthdays_dict:
    #print(f"4:\n {birthdays_dict[today_tuple]}")
    birthday_person = birthdays_dict[today_tuple]
    #print(f"5:\n {birthday_person}")
    
    
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    #print(f"6:\n {file_path}")
    with open(file_path) as letter_file:
        #print(f"7:\n {letter_file}")
        contents = letter_file.read()
        #print(f"8:\n {contents}")
        contents = contents.replace("[NAME]", birthday_person["name"])
        #print(f"9:\n {contents}")
        
        
    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        #print(f"10:\n {connection}")
        connection.starttls()
        #print(f"11:\n {connection}")
        connection.login(MY_EMAIL, MY_PASSWORD)
        #print(f"12:\n {connection}")
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
        #print(f"13:\n {connection}")
