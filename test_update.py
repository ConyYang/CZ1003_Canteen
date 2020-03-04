
def ask_for_dish_name():
    decision_name = True
    while decision_name:
        dish_name = input('Enter new dish name: ')
        answer = int(input('Is' + ' ' + dish_name + ' ' + 'correctly spelled?(Yes:1, NO:0)'))
        if answer == 1:
            return dish_name
        else:
            continue


def isfloat(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


def ask_for_dish_price():
    decision_price = True
    while decision_price:
        dish_price = input('enter price for dish: ')
        if isfloat(dish_price):
            price = round(float(dish_price), 3)
            dish_price = str(price)
            answer = int(input('Is' + ' ' + dish_price + ' ' + 'entered as expected?(Yes:1, NO:0)'))
            if answer == 1:
                decision_price = False
                return price
            else:
                continue
        else:
            print('Not valid digit')
            continue


def add_new_dishes(canteen_etc_Menue):
    name = ask_for_dish_name()
    price = ask_for_dish_price()
    dish_dict = {name: price}
    canteen_etc_Menue.update(dish_dict)
    return canteen_etc_Menue


def change_dish_value(canteen_etc_Menue, index):
    value_list = list(canteen_etc_Menue.values())
    key_list = list(canteen_etc_Menue.keys())
    price = ask_for_dish_price()
    key_dict = key_list[index]
    canteen_etc_Menue[key_dict] = price
    return canteen_etc_Menue


def change_dish_name(canteen_etc_Menue, index):
    key_list = list(canteen_etc_Menue.keys())
    key_dict = key_list[index]
    new_key = ask_for_dish_name()
    canteen_etc_Menue[new_key] = canteen_etc_Menue.pop(key_dict)
    return canteen_etc_Menue


def seller_update(canteen_etc_menue, choice):
    while True:
        if choice == 1:
            return add_new_dishes(canteen_etc_menue)
        elif choice == 2:
            key_list = list(canteen_etc_menue.keys())
            m = 0
            for key in key_list:
                print(str(m) + '.'+ key, end=',')
                m += 1
            print('\n')
            try:
                index = int(input("Which dish to change?"))
            except:
                continue
            return change_dish_value(canteen_etc_menue, index)

        elif choice == 3:
            key_list = list(canteen_etc_menue.keys())
            m = 0
            for key in key_list:
                print(str(m) + '.'+ key, end=',')
                m += 1
            print('\n')
            try:
                index = int(input("Which dish to change?"))
            except:
                continue
            return change_dish_name(canteen_etc_menue, index)

