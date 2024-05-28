# lib/helpers.py
from models.proveyer import Proveyer
from models.item import Item
from models.catagory import Catagory

def exit_program():
    print("Goodbye!")
    exit()

def list_proveyers():
    proveyers = Proveyer.get_all()
    for proveyer in proveyers:
        print(proveyer)

def list_items():
    items = Item.get_all()
    for item in items:
        print(item)
        
def list_catagories():
    catagories = Catagory.get_all()
    for catagory in catagories:
        print (catagory)