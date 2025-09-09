def add(menu, item):
    if item not in menu:
        menu.append(item)
    else:
        print(f"{item} already exists in the menu.")
    return menu
def remove(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} does not exist in the menu.")
    return menu
def check(menu, item):
    if item in menu:
        return f"{item} is available"
    else:
        return f"{item} is not available"
n = int(input("Enter number of initial menu items: "))
menu = []
for i in range(n):
    menu.append(input(f"Enter item {i+1}: "))
add_item = input("Enter an item to add: ")
menu = add(menu, add_item)
remove_item = input("Enter an item to remove: ")
menu = remove(menu, remove_item)
check_item = input("Enter an item to check availability: ")
availability = check(menu, check_item)
print("\nUpdated menu:", menu)
print("Availability:", availability)