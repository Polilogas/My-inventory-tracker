import os
import datetime

def home_page(menu, user_choice, inventory):
    """
    Manages the home page of the inventory system.

    How It Works:
    1. The function takes user input ('a' for add, 'r' for remove, 'p' for print) to perform corresponding user_choices.
    2. If 'a', it calls the add_item_to_inventory function to add a new item.
    3. If 'r', it calls the remove_item_from_inventory function to remove an item.
    4. If 'p', it prints the current items in the inventory.
    5. The loop continues until the user provides an invalid input.
    6. If an invalid input is received, the function prompts the user again.

    Parameters:
    - user_choice (str): User input to determine the user_choice ('a' for add, 'r' for remove, 'p' for print).
    - inventory (list): The list representing the current inventory.

    User Interuser_choice:
    - The user is prompted to input user_choices until an invalid input is provided.

    Note:
    - The function provides a simple interactive interface for managing the inventory.

    """
    while user_choice.lower() in ['a', 'r', 'p']:
        if user_choice.lower() == 'a':
            add_item_to_inventory(inventory)
            save_file(inventory)
            user_choice = input(menu)
        elif user_choice.lower() == 'r':
            save_file(inventory)
            remove_item_from_inventory(inventory)
            user_choice = input(menu)
        else:
            print_inventory()
            user_choice = input(menu)
        
    else:
        print("Not valid input!")
        user_choice = input(menu)
        home_page(menu, user_choice, inventory)

def get_year():
    year = int(input("[YYYY] : "))

    today = datetime.date.today()
    current_year = int(today.year)
    if year >= 1500 and year <= current_year:
        return str(year)
    else:
        print("The year must be between 1500 and " + str(current_year))
        return get_year()


def get_month():
    month = int(input("[MM] : "))
    if month >= 1 and month <= 12:
        if month >= 1 and month <= 9:
            month = "0" + str(month)
            return month
        else:
            return str(month)
    else:
        print("The month must be between 0 and 12")
        return get_month()


def get_day():
    day = int(input("[DD] : "))
    if day >= 1 and day <= 30:
        if day >= 1 and day <= 9:
            day = "0" + str(day)
            return day
        else:
            return str(day)
    else:
        print("The day must be between 0 and 30")
        return get_day()


def get_name():
    item_name = str(input("Enter the item name: "))
    if len(item_name) == 0:
        print("The name cannot be empty!")
        return get_name()
    elif len(item_name) > 20:
        print("The name lenght cannot be more than 20\n")
        return get_name()
    else:
        return item_name.capitalize()

def add_item_to_inventory(inventory):
    """
    Adds a new item to the inventory.

    This function prompts the user to input information about a new item.
    The provided information is then added as a new item to the inventory list.

    How It Works:
    1. The function prompts the user to input information about a new item, including its name, description, and purchase date (if applicable).
    2. The provided information is then structured into a dictionary representing the new item.
    3. This new item dictionary is appended to the inventory list, effectively adding the item to the inventory.
    4. The function prints a confirmation message indicating the successful addition of the item.

    Parameters:
    - inventory (list): The list representing the current inventory.

    User Input:
    - item_name (str): The name of the item.
    - description (str): A brief description of the item.
    - purchase_date (str, optional): The date of purchase.
    """
    item_name = get_name()
    description = str(input("Enter the item description: "))
    print("Enter the purchase date [YYYY - MM - DD]: ")

    purchase_year = get_year()
    purchase_month = get_month()
    purchase_day = get_day()
    purchase_date = purchase_year + "-" + purchase_month + "-" + purchase_day

    new_item = {
        "item_name": item_name,
        "description": description,
        "purchase_date": purchase_date
    }

    inventory.append(new_item)
    print("Item added successfully!")


def remove_item_from_inventory(inventory):
    """
    Removes an item from the inventory.

    Parameters:
    - inventory (list): The list representing the current inventory.

    How It Works:
    1. If the inventory is not empty, it presents a list of items with corresponding numbers.
    2. The user inputs the number associated with the item they want to remove.
    3. The selected item is removed from the inventory, and the user receives a confirmation message.

    User Interuser_choice:
    - Displays a numbered list of items in the inventory along with their names.
    - Asks the user to select an item by entering its corresponding number.
    - Removes the selected item from the inventory.

    Note:
    - If the inventory is empty, it notifies the user.

    """
    if len(inventory) > 0:
        print("Which item do you want to permanently remove from your inventory:")
        print_inventory()

        selected_item = input("Please select an item number or 'a' for All: ")
        try:
            selected_item = int(selected_item)
            selected_item -= 1
            inventory.pop(selected_item)
            print("Item removed successfully!")
            save_file(inventory)
        except:
            if selected_item.lower() == "a":
                verify = input("Are you sure you want to permanently remove all the items from your inventory? (Y/n) ")
                if verify.lower() == "y":
                    inventory.clear()
                    save_file(inventory)
                    print("All items from your inventory has been removed successfully!")
                else:
                    remove_item_from_inventory(inventory)
            else:
                print("\nInvalid input. Please enter a valid integer.")
                return remove_item_from_inventory(inventory)
    else:
        print("There are no items in your inventory")



def print_inventory():
    item_count = 0
    if len(inventory) == 0:
        print("Your inventory is empty")
    else:
        print("No\t" +"Name\t\t\t" + "Purchased Date\t\t" + "Description")
        for item in inventory:
            item_name = item.get("item_name", "")
            purchase_date = item.get("purchase_date", "")
            description = item.get("description", "")

            if len(item_name) <= 5:
                # Handle None values explicitly
                item_info = f"{item_name} \t\t\t{purchase_date} \t\t{description}" if None not in [description] else f"{item_name} \t \t {purchase_date}"
            elif len(item_name) > 5 and len(item_name) <= 14:
                item_info = f"{item_name} \t\t{purchase_date} \t\t{description}" if None not in [description] else f"{item_name} \t \t {purchase_date}"
            else:
                item_info = f"{item_name} \t{purchase_date} \t\t{description}" if None not in [description] else f"{item_name} \t \t {purchase_date}"
            
            print(str(item_count + 1) + ": " + "\t" + item_info)
            item_count += 1


def save_file(inventory):
    file = open('items.txt','w')
    for item in inventory:
        file.write(str(item) + "\n")
    file.close()

def is_file_empty(file_path):
    return os.path.getsize(file_path) == 0

def load_file(inventory):
    # check if the file exist
    file = os.path.exists("items.txt")
    if file:
        if is_file_empty("items.txt"):
            pass
            print("file is empty")
        else:
            with open('items.txt', 'r') as file:
                for line in file:
                    # Convert the string representation of dictionary to a dictionary
                    item_dict = eval(line.strip())
                    inventory.append(item_dict)
    else:
        # If file doesn't exist
        file = open('items.txt','w')
        file.close()

inventory = []
load_file(inventory)

menu = "\nDo you want to add (A), remove (R) or print(P) an item from the inventory? "
user_choice = input(menu)
home_page(menu, user_choice, inventory)