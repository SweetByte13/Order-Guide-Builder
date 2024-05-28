# lib/cli.py
#!/usr/bin/env python3

from helpers import (
    exit_program,
    list_proveyers,
    list_items,
    list_catagories
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_proveyers()
        elif choice == "2":
            list_items()
        elif choice == "3":
            list_catagories()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List Proveyers")
    print("2. List Items")
    print("3. List Catagories")

if __name__ == "__main__":
    main()
