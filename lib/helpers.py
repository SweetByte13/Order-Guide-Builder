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
    print(f'{Proveyer.get_all()}')
    id_ = input("Enter the proveyer's ID: ")
    if proveyer := Proveyer.find_by_id(id_):
        returned_items = proveyer.get_items()
        for item in returned_items:
            print(item)
    else: print(f'Proveyer ID not found')
    
def search_proveyer_by_id():
    id_ = input("Enter the proveyer's ID: ")
    if proveyer := Proveyer.find_by_id(id_):
        print(proveyer)
    else: print(f'Proveyer not found')
    
def create_new_proveyer():
    name_input = input("Please enter perveyor's name:")
    if name_input == "":
        print("Invalid Value")
        return 
    order_min_input = input("Please enter perveyor's order minimum using whole numbers:")
    if order_min_input == "":
        print("Invalid Value")
        return 
    cut_off_time_input = input("Please enter perveyor's cut off time using army time:")
    if cut_off_time_input == "":
        print("Invalid Value")
        return 
    Proveyer.create(str(name_input), int(order_min_input), int(cut_off_time_input))
    print(f'New Proveyer: {name_input}, {order_min_input}, {cut_off_time_input}')
    
def update_new_proveyer():
    print(f'{Proveyer.get_all()}')
    id_ = input("Enter proveyer ID: ")
    if proveyer := Proveyer.find_by_id(id_):
        print(proveyer)
        name_input = input("Please enter the updated perveyor's name:")
        if name_input == "":
            print("Invalid Value")
            return 
        proveyer.name = str(name_input)
        order_min_input = input("Please enter the updated perveyor's order minimum using whole numbers:")
        if order_min_input == "":
            print("Invalid Value")
            return 
        proveyer.order_min = int(order_min_input)
        cut_off_time_input = input("Please enter the updated perveyor's cut off time using army time:")
        if cut_off_time_input == "":
            print("Invalid Value")
            return 
        proveyer.cut_off_time = int(cut_off_time_input)
        proveyer.update()
        print(f'Proveyer has been updated')
    else: print(f'Proveyer ID not found')
    
def delete_new_proveyer():
    print(f'{Proveyer.get_all()}')
    id_ = input("Enter proveyer ID: ")
    if proveyer := Proveyer.find_by_id(id_):
        print(proveyer)
        proveyer.delete()
        print (f'Proveyer has been deleted')
    else: print(f'Proveyer ID not found')
    
def create_new_item():
    name_input = input("Please enter item's name:")
    if name_input == "":
        print("Invalid Value")
        return 
    name = str(name_input)
    stock_input = input("Please enter stock amount:")
    if stock_input == "":
        print("Invalid Value")
        return
    stock = int(stock_input)
    par_amount_input = input("Please enter par amount:")
    if par_amount_input == "":
        print("Invalid Value")
        return
    par_amount = int(par_amount_input)
    print(f'{Catagory.get_all()}')
    catagory_id_par = input("Please enter items's catagory ID:")
    if catagory_id_par == "":
        print("Invalid Value")
        return
    catagory_id = int(catagory_id_par)
    par = Par.create(name, stock, par_amount)
    Item.create(name, par.id, catagory_id)
    print(f'New Item: {name}, {par.id}, {catagory_id}')
    
def update_new_item():
    id_ = input("Enter item ID: ")
    if item := Item.find_by_id(id_):
        print(item)
        name_input = str(input("Please enter updated item's name:"))
        if name_input == "":
            print("Invalid Value")
            return
        item.name = name_input
        print(f'{Catagory.get_all()}')
        catagory_id = input("Please enter updated items's catagory ID:")
        if catagory_id == "":
            print("Invalid Value")
            return
        item.catagory_id = int(catagory_id)
        item.update()
        print(f'{item} has been updated')
    else: print(f'Item ID not found')
    
def delete_new_item():
    print(f'{Item.get_all()}')
    id_ = input("Enter item ID: ")
    if item := Item.find_by_id(id_):
        item.delete()
        print(f'{item} has been deleted')
    else: print(f'Item ID not found')
    
def create_new_par():
    name_input = input("Please enter par's name:")
    if name_input == "":
            print("Invalid Value")
            return
    name = str(name_input)
    in_stock_input = input("Please enter par's in stock amount:")
    if in_stock_input == "":
        print("Invalid Value")
        return
    in_stock = int(in_stock_input)
    par_amount_input = input("Please enter par's par amount:")
    if par_amount_input == "":
        print("Invalid Value")
        return
    par_amount = int(par_amount_input)
    Par.create(name, in_stock, par_amount)
    print(f"New Par: {name}, {in_stock}, {par_amount}")
    
def update_new_par():
    print(f'{Par.get_all()}')
    id_ = input("Enter par ID: ")
    if par := Par.find_by_id(id_):
        print(par)
        name_input = input("Please enter updated pars's name:")
        if name_input == "":
            print("Invalid Value")
            return
        par.name = str(name_input)
        stock_input = input("Please enter updated par's in stock amount:")
        if stock_input == "":
            print("Invalid Value")
            return
        par.stock = int(stock_input)
        par_amount_input = input("Please enter updated pars's par amount:")
        if par_amount_input == "":
            print("Invalid Value")
            return
        par.par_amount = int(par_amount_input)
        par.update()
        print(f'{par} has been updated')
    else: print(f'Item ID not found')
    
def delete_new_par():
    print(f'{Par.get_all()}')
    id_ = input("Enter par ID: ")
    if par := Par.find_by_id(id_):
        par.delete()
        print(f'{par} has been deleted')
    else: print(f'Par ID not found')
    
def create_new_catagory():
    name = input("Please enter catagory's name:")
    if name == "":
            print("Invalid Value")
            return
    Catagory.create(name)
    print(f'New Catagory: {name}')
    
def update_new_catagory():
    print(f'{Catagory.get_all()}')
    id_ = input("Enter catagory ID: ")
    if catagory := Catagory.find_by_id(id_):
        print(catagory)
        name_input = str(input("Please enter updated catagory's name:"))
        if name_input == "":
            print("Invalid Value")
            return
        catagory.name = name_input
        catagory.update()
        print(f'{catagory} updated')
    else: print(f'Catagory ID not found')
    
def list_departments():
    department = Department.get_all()
    for department in department:
        print(department)
    
def create_new_department():
    name = str(input("Please enter department's name:"))
    if name == "":
            print("Invalid Value")
            return
    Department.create(name)
    print(f'New Department:{name}')
    
def update_new_department():
    print(f'{Department.get_all()}')
    id_ = input("Enter department ID: ")
    if department := Department.find_by_id(id_):
        print(department)
        name_input = str(input("Please enter updated department's name:"))
        if name_input == "":
            print("Invalid Value")
            return
        department.name = name_input
        department.update()
        print(f'{department} updated')
    else: print(f'Department ID not found')
    
def delete_new_department():
    print(f'{Department.get_all()}')
    id_ = input("Enter department ID: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'{department} has been deleted')
    else: print(f'Department ID not found')
    
