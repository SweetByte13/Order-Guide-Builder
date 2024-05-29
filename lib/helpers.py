# lib/helpers.py
from models.proveyer import Proveyer
from models.item import Item
from models.catagory import Catagory
from models.par import Par
from models.department import Department

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
        
def list_items_by_proveyer():
    id_ = input("Enter the proveyer's ID: ")
    if proveyer := Proveyer.find_by_id(id_):
        returned_items = proveyer.get_items()
        for item in returned_items:
            print(item)
    else: print(f'Proveyer ID not found')
    
def create_new_proveyer():
    name = input("Please enter perveyor's name:")
    catagory = input("Please enter perveyor's catagory:")
    order_minimum = input("Please enter perveyor's order minimum:")
    cut_off_time = input("Please enter perveyor's cut off time:")
    Proveyer.create(name, catagory, order_minimum, cut_off_time)
    
def update_new_proveyer():
    id_ = input("Enter proveyer ID: ")
    if proveyer := Proveyer.find_by_id(id_):
        proveyer.order_min = int(input("Please enter perveyor's order minimum:"))
        proveyer.cut_off_time = int(input("Please enter perveyor's cut off time:"))
        proveyer.update()
    else: print(f'Proveyer ID not found')
    
def delete_new_proveyer():
    id_ = input("Enter proveyer ID: ")
    if proveyer := Proveyer.find_by_id(id_):
        proveyer.delete()
    else: print(f'Proveyer ID not found')
    
def create_new_item():
    name = str(input("Please enter item's name:"))
    par_id = int(input("Please enter item's par ID:"))
    catagory_id = int(input("Please enter items's catagory ID:"))
    Item.create(name, par_id, catagory_id)
    
def update_new_item():
    id_ = input("Enter item ID: ")
    if item := Item.find_by_id(id_):
        print(item)
        item.name = str(input("Please enter updated item's name:"))
        item.par_id = int(input("Please enter updated item's par ID:"))
        item.catagory_id = int(input("Please enter updated items's catagory ID:"))
        item.update()
    else: print(f'Item ID not found')
    
def delete_new_item():
    id_ = input("Enter item ID: ")
    if item := Item.find_by_id(id_):
        item.delete()
    else: print(f'Proveyer ID not found')
    
def create_new_par():
    name = str(input("Please enter par's name:"))
    in_stock = int(input("Please enter par's in stock amount:"))
    par_amount = int(input("Please enter par's par amount:"))
    Par.create(name, in_stock, par_amount)
    
def update_new_par():
    id_ = input("Enter par ID: ")
    if par := Par.find_by_id(id_):
        print(par)
        par.name = str(input("Please enter updated item's name:"))
        par.stock = int(input("Please enter updated item's in stock amount:"))
        par.par_amount = int(input("Please enter updated items's par amount:"))
        par.update()
    else: print(f'Item ID not found')
    
def delete_new_par():
    id_ = input("Enter par ID: ")
    if par := Par.find_by_id(id_):
        par.delete()
    else: print(f'Proveyer ID not found')
    
def create_new_catagory():
    name = str(input("Please enter catagory's name:"))
    Catagory.create(name)
    
def update_new_catagory():
    id_ = input("Enter catagory ID: ")
    if catagory := Catagory.find_by_id(id_):
        print(catagory)
        catagory.name = str(input("Please enter updated catagory's name:"))
        catagory.update()
    else: print(f'Catagory ID not found')
    
def delete_new_catagory():
    id_ = input("Enter catagory ID: ")
    if catagory := Catagory.find_by_id(id_):
        catagory.delete()
    else: print(f'Catagory ID not found')
    
def create_new_department():
    name = str(input("Please enter department's name:"))
    Department.create(name)
    
def update_new_department():
    id_ = input("Enter department ID: ")
    if department := Department.find_by_id(id_):
        print(department)
        name_input = str(input("Please enter updated department's name:"))
        if name_input == "":
            print("Invalid Value")
            return
        department.name = name_input
        department.update()
    else: print(f'Department ID not found')
    
def delete_new_department():
    id_ = input("Enter department ID: ")
    if department := Department.find_by_id(id_):
        department.delete()
    else: print(f'Department ID not found')