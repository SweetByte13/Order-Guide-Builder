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
    print("4. List Items by proveyer")
    print("5. List full order guide")
    print("6. List order guide based on items near par")
    print("7. List guide of items from highest to lowest in stock")
    print("8. Search for item by name")
    print("9. Search for department by id")
    print("10. Manage Proveyers")
    print("11. Manage Items")
    print("12. Manage Pars")
    print("13. Manage Catagories")
    print("14. Manage Departments")



if __name__ == "__main__":
    main()
