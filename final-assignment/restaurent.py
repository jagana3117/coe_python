def add_item(menu, item):
    menu.append(item)
    return menu
def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
        return menu
    else:
        return f"{item} does not exist in the menu."
def check_item(menu, item):
    if item in menu:
        return f"{item} is available"
    else:
        return f"{item} is not available"
initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
updated_menu = add_item(initial_menu, add_item)
remove_item = "Salad"
updated_menu = remove_item(updated_menu, remove_item)
check_item = "Pizza"
availability = check_item(updated_menu, check_item)
print(f"Updated menu: {updated_menu}")
print(availability)
