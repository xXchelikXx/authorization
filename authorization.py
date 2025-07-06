from main import load_key

import os
from cryptography.fernet import Fernet


def authorization(login, password, fer):
    is_authorizationed = False
    with open("passwords.txt", "r") as passwords_file:
        for users in passwords_file.readlines():
            users_data = users.rstrip()
            user_login, user_password = users_data.split("|")
            user_password = fer.decrypt(user_password.encode()).decode()
            if user_login == login and user_password == password:
                is_authorizationed = True
    return is_authorizationed

def main():
    key = load_key()
    key_from_file = Fernet(key)
    while True:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        if authorization(login, password, key_from_file):
            print("Bce ok")
            break
        else:
            print("makux Hem 👎")


if __name__ == "__main__":
    main()