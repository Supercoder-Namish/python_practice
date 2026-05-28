menu = ['Butter Paneer','Butter Chicken','Naan','Roti','Biryani']

def show_menu():
    for dish in menu:
        print(dish)

def add_dish(dish):
    is_dish_available = is_dish_available_in_menu(dish)
    print("is_dish_available ->" + str(is_dish_available))
    if (is_dish_available == True):
        print('Dish already exists ->' + dish)
        return
    else:
        menu.append(dish)
        print('in add_dish function dish ' + dish + 'add it to the menu\n')
        show_menu()
        print('successfully added to menu\n')

def is_dish_available_in_menu(dish):
    for d in menu:
        if d == dish:
            print('Dish already exists ->' + dish + 'is_dish_available_in_menu\n')
            return True
            return True
        else:
            print('Dish does not exist ->' + dish + 'is_dish_available_in_menu\n')
            return False



def add_dish_to_index_in_menu(dish,index):
    menu_new = []
    is_dish_available = is_dish_available_in_menu(dish)
    if (is_dish_available == True):
        print('Dish already exists ->' + dish)
        return
    elif (is_dish_available == False):
        idx = 0
        for d in menu:
            if idx == index:
                menu_new.append(dish)
            else:
                menu_new.append(d)
            idx = idx + 1
    return menu_new



if __name__ == '__main__':
    print(show_menu())

    print(add_dish('Butter Paneer'))

    print(menu)

    updated_menu = add_dish_to_index_in_menu('Rogan Josh',3)
    print(updated_menu)