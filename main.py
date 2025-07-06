import os
from cryptography.fernet import Fernet


def write_key():
    if os.path.exists("key.key"):
        print("Ключ присутствует")
    else:
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        print("Ключ создан")


def load_key():
    with open("key.key", "r") as key_file:
        key_from_file = key_file.read()
    key_from_file = key_from_file.rstrip()
    return key_from_file


def add(fer):
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    with open("passwords.txt", "a") as passwords_file:
        passwords_file.write(f"{login}|{fer.encrypt(password.encode()).decode()}\n")


def view(fer):
    with open("passwords.txt", "r") as view_passwords:
        for users in view_passwords.readlines():
            users_data = users.rstrip()
            user_login, user_password = users_data.split("|")
            print(f"Логин: {user_login} | Пароль: {fer.decrypt(user_password.encode()).decode()}")
            
def main():
    write_key()
    load_key()
    key = load_key()
    key_from_file = Fernet(key)

    exit = False

    while exit == False:
        choice = input("Выберите пункт: 1.Добавить пароль | 2.Просмотреть пароли | 3.Выйти | ")
        if choice == "1":
            add(key_from_file)
        elif choice == "2":
            view(key_from_file)
        elif choice == "3":
            print("Bblxog")
            exit = True

if __name__ == "__main__":
    main()
