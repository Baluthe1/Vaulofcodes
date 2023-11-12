
# Initialize an empty inventory
inventory = []

# Function to add new items to the inventory
def add_item():
    item_name = input("Enter the item name: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price per unit: "))
    inventory.append({"name": item_name, "quantity": quantity, "price": price})
    print(f"{item_name} added to the inventory.")

# Function to update existing items' quantities
def update_quantity():
    item_name = input("Enter the item name to update quantity: ")
    for item in inventory:
        if item["name"] == item_name:
            new_quantity = int(input("Enter the new quantity: "))
            item["quantity"] = new_quantity
            print(f"Quantity of {item_name} updated to {new_quantity}.")
            break
    else:
        print(f"{item_name} not found in the inventory.")

# Function to view the current inventory
def view_inventory():
    print("Current Inventory:")
    for item in inventory:
        print(f"{item['name']} - Quantity: {item['quantity']}, Price: ${item['price']}")

# Function to remove items from the inventory
def remove_item():
    item_name = input("Enter the item name to remove: ")
    for item in inventory:
        if item["name"] == item_name:
            inventory.remove(item)
            print(f"{item_name} removed from the inventory.")
            break
    else:
        print(f"{item_name} not found in the inventory.")

# Main loop for menu-based interaction
while True:
    print("\nMenu:")
    print("1. Add new item")
    print("2. Update item quantity")
    print("3. View inventory")
    print("4. Remove item")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_item()
    elif choice == "2":
        update_quantity()
    elif choice == "3":
        view_inventory()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")