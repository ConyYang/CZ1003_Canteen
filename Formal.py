import pygame
from database import *
import itertools
from math import *
import pickle
from test_update import *
import webbrowser
import time

# IMPORTANT: comment the following block for the first time execution
pickle_out = open('database.pickle_1','rb')
canteen = pickle.load(pickle_out)
canteen1_Menue = pickle.load(pickle_out)
canteen2_Menue = pickle.load(pickle_out)
canteen9_Menue = pickle.load(pickle_out)
canteen11_Menue = pickle.load(pickle_out)
canteen13_Menue = pickle.load(pickle_out)
canteen16_Menue = pickle.load(pickle_out)
canteenA_Menue = pickle.load(pickle_out)
canteenB_Menue = pickle.load(pickle_out)
canteenT_Menue = pickle.load(pickle_out)
canteenN_Menue = pickle.load(pickle_out)
pickle_out.close()

#required for directions, able to access this value across different functions
class cursor():
    location = (0,0)

canteen_rating = {**{'canteen1':canteen['canteen1'][3]},**{'canteen2':canteen['canteen2'][3]},
                  **{'canteen9':canteen['canteen9'][3]},**{'canteen11':canteen['canteen11'][3]},
                  **{'canteen13':canteen['canteen13'][3]},**{'canteen16':canteen['canteen16'][3]},
                  **{'canteenA':canteen['canteenA'][3]},**{'canteenB':canteen['canteenB'][3]},
                  **{'canteenT':canteen['canteenT'][3]},**{'canteenN':canteen['canteenN'][3]}}

canteen_foodtype = {**canteen1_Menue,**canteen2_Menue,**canteen9_Menue,
                    **canteen11_Menue,**canteen13_Menue,**canteen16_Menue,
                    **canteenA_Menue, **canteenB_Menue,**canteenT_Meune,
                    **canteenN_Menue} # in case new value

# loading finished


pygame.init()  # initialize pygame


pygame.display.set_caption("NTUFood")  # set the window's caption


def auto_save():  # To save the user changed data
    pickle_in = open('database.pickle_1', 'wb')  # save edited data
    pickle.dump(canteen, pickle_in)
    pickle.dump(canteen1_Menue, pickle_in)
    pickle.dump(canteen2_Menue, pickle_in)
    pickle.dump(canteen9_Menue, pickle_in)
    pickle.dump(canteen11_Menue, pickle_in)
    pickle.dump(canteen13_Menue, pickle_in)
    pickle.dump(canteen16_Menue, pickle_in)
    pickle.dump(canteenA_Menue, pickle_in)
    pickle.dump(canteenB_Menue, pickle_in)
    pickle.dump(canteenT_Meune, pickle_in)
    pickle.dump(canteenN_Menue, pickle_in)
    pickle_in.close()


def display_message(str, a, b, R, G, B, size):  # a,b is coordinator. show text message on screen
    my_font = pygame.font.SysFont(None, size)
    text = my_font.render(str, 1, (R, G, B))
    screen.blit(text, (a,b))
    pygame.display.update()


# -----------------------------
# start of "sort by rank function", written by Yang, edited by Zhang

def pick_dish(canteen_name,dish_name,rating_canteen):
    if dish_name in canteen[canteen_name][1]:
        return rating_canteen[dish_name][0]
    else:
        pass


def list_get (canteen_rating,dishname):
    new_canteen_rating = {}
    for key,value in canteen_rating.items():
        a = pick_dish(key,dishname,value)
        if a != None:
            new_canteen_rating.update({key:a})
        else:
            pass
    a = list(sorted(new_canteen_rating.items(), reverse=True, key=lambda x: x[1]))
    return a


# ------------------------------------------------------------------------------------

def display_rank(list,dish_name):
    waiting = 1
    running = 1
    while waiting:
        if running:
            screen.blit(Blank, (0, 0))
            pygame.display.flip()
            x = [440, 440, 440, 440, 440, 440, 440, 440, 440, 440]
            y = [250, 300, 350, 400, 450, 500, 550, 600, 650, 700]
            i = 1
            for k in list:
                display_message(str(k), x[i - 1], y[i - 1], 0, 0, 0, 40)
                i += 1
            display_message(dish_name, 440, 200, 20, 0, 150, 50)
            running = 0
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                if 1089 <= cursor_position[0] <= 1236 and 667 <= cursor_position[1] <= 699:
                    return 0

#----------------------------------------------


def rating_average(rating_n):
    n = 0
    sum_rating = 0
    for value in rating_n.values():
        value_real = value[0]
        n+=1
        sum_rating += value_real
    average_rating = sum_rating/n
    return round(average_rating,2)


def rating_all (canteen_rating):
    new_canteen_rate = {}
    for key,value in canteen_rating.items():
        canteen_rate = {key:rating_average(value)}
        new_canteen_rate.update(canteen_rate)
    sort_result = sorted(new_canteen_rate.items(), reverse=True, key=lambda x: x[1])
    b = list(sort_result)
    return b

def rating_all_keys (canteen_rating):
    new_canteen_rate = {}
    for key,value in canteen_rating.items():
        canteen_rate = {key:rating_average(value)}
        new_canteen_rate.update(canteen_rate)
    sort_result = sorted(new_canteen_rate.items(), reverse=True, key=lambda x: x[1])
    sort_list_name = []
    for i in range(0, len(sort_result)):
        sort_list_name.append(sort_result[i][0])
    return sort_list_name


def display_allcanteen_rank(list):
    waiting = 1
    running = 1
    while waiting:
        if running:
            screen.blit(rank_canteenfull_option, (0, 0))
            pygame.display.flip()
            x = [220, 760, 220, 760, 220, 760, 220, 760, 220, 760, 220, 760]
            y = [250, 250, 340, 340, 430, 430, 520, 520, 610, 610, 700, 700]
            i = 1
            for k in list:
                display_message(str(k), x[i - 1], y[i - 1], 0, 0, 0, 40)
                i += 1
            running = 0
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                if 1089 <= cursor_position[0] <= 1236 and 667 <= cursor_position[1] <= 699:
                    return 0
        sort_list = rating_all_keys(canteen_rating)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                auto_save()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                local_cursor_position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                if 1089 <= local_cursor_position[0] <= 1236 and 667 <= local_cursor_position[1] <= 699:
                    return 0
                elif 197 <= local_cursor_position[0] <= 485 and 235 <= local_cursor_position[1] <= 301:
                    display_canteen_info_rank2(sort_list[0])
                    running =1
                elif 197 <= local_cursor_position[0] <= 485 and 328 <= local_cursor_position[1] <= 380:
                    display_canteen_info_rank2(sort_list[2])
                    running = 1
                elif 197 <= local_cursor_position[0] <= 485 and 417 <= local_cursor_position[1] <= 471:
                    display_canteen_info_rank2(sort_list[4])
                    running = 1
                elif 197 <= local_cursor_position[0] <= 485 and 508 <= local_cursor_position[1] <= 560:
                    display_canteen_info_rank2(sort_list[6])
                    running = 1
                elif 197 <= local_cursor_position[0] <= 485 and 592 <= local_cursor_position[1] <= 650:
                    display_canteen_info_rank2(sort_list[8])
                    running = 1
                elif 725 <= local_cursor_position[0] <= 1013 and 235 <= local_cursor_position[1] <= 301:
                    display_canteen_info_rank2(sort_list[1])
                    running = 1
                elif 725 <= local_cursor_position[0] <= 1013 and 328 <= local_cursor_position[1] <= 380:
                    display_canteen_info_rank2(sort_list[3])
                    running = 1
                elif 725 <= local_cursor_position[0] <= 1013 and 417 <= local_cursor_position[1] <= 471:
                    display_canteen_info_rank2(sort_list[5])
                    running = 1
                elif 725 <= local_cursor_position[0] <= 1013 and 508 <= local_cursor_position[1] <= 560:
                    display_canteen_info_rank2(sort_list[7])
                    running = 1
                elif 725 <= local_cursor_position[0] <= 1013 and 592 <= local_cursor_position[1] <= 650:
                    display_canteen_info_rank2(sort_list[9])
                    running = 1

def display_canteen_info_rank2(key_canteen_name):
    tem_info = canteen[key_canteen_name][4]
    pygame.display.flip()
    screen.blit(Blank, (0, 0))
    tem_img = canteen_img[key_canteen_name]
    screen.blit(tem_img, (175, 283))
    display_message(tem_info[0], 699, 191, 0, 0, 0, 60)
    display_message(tem_info[1], 546, 263, 0, 0, 0, 40)
    display_message(tem_info[2], 546, 313, 0, 0, 0, 40)
    display_message(tem_info[3], 546, 363, 0, 0, 0, 40)
    display_message(tem_info[4], 546, 413, 0, 0, 0, 40)
    display_message(tem_info[5], 546, 463, 0, 0, 0, 40)
    pygame.display.flip()
    waiting = 1
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                if 1089 <= cursor_position[0] <= 1236 and 667 <= cursor_position[1] <= 699:
                    return 0

# -----------------------------------------------

# display rank

def display_by_rank():  # GUI, choose food preference.
    waiting = 1
    while waiting:
            screen.blit(rank_option, (0, 0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    auto_save()
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cursor_position = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        auto_save()
                        pygame.quit()
                    if 1089 <= cursor_position[0] <= 1236 and 667 <= cursor_position[1] <= 699:
                        return 0
                    if 139 <= cursor_position[0] <= 438 and 223 <= cursor_position[1] <= 273:
                        dish_name = "CHINESE CUSINE"
                        can_list_chn = list_get(canteen_rating, dish_name)
                        display_rank(can_list_chn, dish_name)
                    elif 139 <= cursor_position[0] <= 438 and 229 <= cursor_position[1] <= 349:
                        dish_name = "CANTONESE"
                        can_list_can = list_get(canteen_rating, dish_name)
                        display_rank(can_list_can, dish_name)
                    elif 139 <= cursor_position[0] <= 438 and 374 <= cursor_position[1] <= 424:
                        dish_name = "CHICKEN RICE"
                        can_list_chi = list_get(canteen_rating, dish_name)
                        display_rank(can_list_chi, dish_name)
                    elif 139 <= cursor_position[0] <= 438 and 449 <= cursor_position[1] <= 499:
                        dish_name = "Desserts"
                        can_list_des = list_get(canteen_rating, dish_name)
                        display_rank(can_list_des, dish_name)
                    elif 139 <= cursor_position[0] <= 438 and 525 <= cursor_position[1] <= 573:
                        dish_name = "INDIA"
                        can_list_ind = list_get(canteen_rating, dish_name)
                        display_rank(can_list_ind, dish_name)
                    elif 139 <= cursor_position[0] <= 438 and 600 <= cursor_position[1] <= 649:
                        dish_name = "JAPANESE"
                        can_list_jap = list_get(canteen_rating, dish_name)
                        display_rank(can_list_jap, dish_name)
                    elif 470 <= cursor_position[0] <= 769 and 223 <= cursor_position[1] <= 273:
                        dish_name = "MIXED RICE"
                        can_list_mix = list_get(canteen_rating, dish_name)
                        display_rank(can_list_mix, dish_name)
                    elif 470 <= cursor_position[0] <= 769 and 229 <= cursor_position[1] <= 349:
                        dish_name = "PASTA EXPRESS"
                        can_list_pas = list_get(canteen_rating, dish_name)
                        display_rank(can_list_pas, dish_name)
                    elif 470 <= cursor_position[0] <= 769 and 374 <= cursor_position[1] <= 424:
                        dish_name = "VEGETARIAN"
                        can_list_veg = list_get(canteen_rating, dish_name)
                        display_rank(can_list_veg, dish_name)
                    elif 470 <= cursor_position[0] <= 769 and 449 <= cursor_position[1] <= 499:
                        dish_name = "WESTERN"
                        can_list_wes = list_get(canteen_rating, dish_name)
                        display_rank(can_list_wes, dish_name)
                    elif 470 <= cursor_position[0] <= 769 and 525 <= cursor_position[1] <= 573:
                        dish_name = "XIANCAI"
                        can_list_xia = list_get(canteen_rating, dish_name)
                        display_rank(can_list_xia, dish_name)
                    elif 470 <= cursor_position[0] <= 769 and 600 <= cursor_position[1] <= 649:
                        dish_name = "XIANGGUO"
                        can_list_xig = list_get(canteen_rating, dish_name)
                        display_rank(can_list_xig, dish_name)
                    elif 801 <= cursor_position[0] <= 1099 and 223 <= cursor_position[1] <= 273:
                        dish_name = "YONG TAU FOO"
                        can_list_ytf = list_get(canteen_rating, dish_name)
                        display_rank(can_list_ytf, dish_name)
                    elif 844 <= cursor_position[0] <= 1122 and 423 <= cursor_position[1] <= 612:
                        can_list_all = rating_all(canteen_rating)
                        display_allcanteen_rank(can_list_all)


# end of sort by rank function

# to display each canteen's detailed information. By Heng Kai
def display_canteen_info(can_info):
    tem_info = canteen[can_info][4] # canteen information [name, address, telephone, opening hours, stalls, seating capacity]
    tem_img = canteen_img[can_info]
    waiting = 1
    while waiting:
        screen.blit(Canteen_information_blank, (0, 0))
        screen.blit(tem_img, (175, 283))
        display_message(tem_info[0], 699, 191, 0, 0, 0, 60)
        display_message(tem_info[1], 546, 263, 0, 0, 0, 40)
        display_message(tem_info[2], 546, 313, 0, 0, 0, 40)
        display_message(tem_info[3], 546, 363, 0, 0, 0, 40)
        display_message(tem_info[4], 546, 413, 0, 0, 0, 40)
        display_message(tem_info[5], 546, 463, 0, 0, 0, 40)
        pygame.display.flip()
   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                if 0 <= cursor_position[0] <= 149 and 667 <= cursor_position[1] <= 699:
                    return 0
                elif 1089 <= cursor_position[0] <= 1236 and 667 <= cursor_position[1] <= 699:
                    display_canteen_map(can_info)
# end

#get location based on mouse position, shows map if user have not input current location. By HengKai
def display_canteen_map(canteen_name):
    da = 72
    db = 91
    a = 48
    b = 45
    canteen_name = change_name(canteen_name)
    if cursor.location[0] != 0 and cursor.location[1] != 0:
        if (da + 3*a) <= cursor.location[0] <= (da+7*a) and (db) <= cursor.location[1] <= (db+4*b):
            display_can_directions(canteen_name, 'NIE')
        elif (da+7*a) <= cursor.location[0] <= (da+8*a) and (db+b) <= cursor.location[1] <= (db+3*b):
            display_can_directions(canteen_name, 'hall12')
        elif (da+8*a) <= cursor.location[0] <= (da+9*a) and (db+b) <= cursor.location[1] <= (db + 3*b):
            display_can_directions(canteen_name, 'hall13')
        elif (da+7*a) <= cursor.location[0] <= (da+8*a) and (db+3*b) <= cursor.location[1] <= (db+4*b):
            display_can_directions(canteen_name, 'hall16')
        elif (da+8*a) <= cursor.location[0] <= (da+9*a) and (db+3*b) <= cursor.location[1] <= (db+4*b):
            display_can_directions(canteen_name, 'hall3')
        elif (da+9*a) <= cursor.location[0] <= (da+10*a) and (db+b) <= cursor.location[1] <= (db+3*b):
            display_can_directions(canteen_name, 'hall14')
        elif (da+10*a) <= cursor.location[0] <= (da+12*a) and (db+b) <= cursor.location[1] <= (db+3*b):
            display_can_directions(canteen_name, 'hall15')
        elif (da+12*a) <= cursor.location[0] <= (da+15*a) and (db+2*b) <= cursor.location[1] <= (db+3*b):
            display_can_directions(canteen_name, 'tamarind')
        elif (da+12*a) <= cursor.location[0] <= (da+15*a) and (db+3*b) <= cursor.location[1] <= (db+4*b):
            display_can_directions(canteen_name, 'graduatehall')
        elif (da+10*a) <= cursor.location[0] <= (da+11*a) and (db+4*b) <= cursor.location[1] <= (db+6*b):
            display_can_directions(canteen_name, 'hall8')
        elif (da+11*a) <= cursor.location[0] <= (da+15*a) and (db+4*b) <= cursor.location[1] <= (db+7*b):
            display_can_directions(canteen_name, 'northhill')
        elif (da+a) <= cursor.location[0] <= (da+7*a) and (db+4*b) <= cursor.location[1] <= (db+7*b):
            display_can_directions(canteen_name, 'northspine')
        elif (da + 7*a) <= cursor.location[0] <= (da+10*a) and (db+5*b) <= cursor.location[1] <= (db+6*b):
            display_can_directions(canteen_name, 'adm')
        elif (da + 7*a) <= cursor.location[0] <= (da+10*a) and (db+6*b) <= cursor.location[1] <= (db+8*b):
            display_can_directions(canteen_name, 'hall2')
        elif (da+10*a) <= cursor.location[0] <= (da+14*a) and (db+7*b) <= cursor.location[1] <= (db+8*b):
            display_can_directions(canteen_name, 'meadow')
        elif (da+10*a) <= cursor.location[0] <= (da+13*a) and (db+8*b) <= cursor.location[1] <= (db+11*b):
            display_can_directions(canteen_name, 'src')
        elif (da+a) <= cursor.location[0] <= (da+6*a) and (db+7*b) <= cursor.location[1] <= (db+11*b):
            display_can_directions(canteen_name, 'southspine')
        elif da <= cursor.location[0] <= (da+a) and (db+7*b) <= cursor.location[1] <= (db+11*b):
            display_can_directions(canteen_name, 'hall7')
        elif (da+6*a) <= cursor.location[0] <= (da+9*a) and (db+8*b) <= cursor.location[1] <= (db+12*b):
            display_can_directions(canteen_name, 'nanyangcircle')
        elif (da+9*a) <= cursor.location[0] <= (da+10*a) and (db+8*b) <= cursor.location[1] <= (db+10*b):
            display_can_directions(canteen_name, 'hall6')
        elif (da+9*a) <= cursor.location[0] <= (da+10*a) and (db+10*b) <= cursor.location[1] <= (db+12*b):
            display_can_directions(canteen_name, 'pioneerhall')       
        else:
            pass
    else:
        
        waiting = 1
        while waiting:
            screen.blit(NTU_map, (0, 0))
            display_message('Enter your current location!', 400, 20, 0, 0, 0, 50)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    auto_save()
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cursor_position = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        auto_save()
                        pygame.quit()
                    if 1089 <= cursor_position[0] <= 1236 and 667 <= cursor_position[1] <= 699:
                        return 0
                    elif (da + 3*a) <= cursor_position[0] <= (da+7*a) and (db) <= cursor_position[1] <= (db+4*b):
                        display_can_directions(canteen_name, 'NIE')
                    elif (da+7*a) <= cursor_position[0] <= (da+8*a) and (db+b) <= cursor_position[1] <= (db+3*b):
                        display_can_directions(canteen_name, 'hall12')
                    elif (da+8*a) <= cursor_position[0] <= (da+9*a) and (db+b) <= cursor_position[1] <= (db + 3*b):
                        display_can_directions(canteen_name, 'hall13')
                    elif (da+7*a) <= cursor_position[0] <= (da+8*a) and (db+3*b) <= cursor_position[1] <= (db+4*b):
                        display_can_directions(canteen_name, 'hall16')
                    elif (da+8*a) <= cursor_position[0] <= (da+9*a) and (db+3*b) <= cursor_position[1] <= (db+4*b):
                        display_can_directions(canteen_name, 'hall3')
                    elif (da+9*a) <= cursor_position[0] <= (da+10*a) and (db+b) <= cursor_position[1] <= (db+3*b):
                        display_can_directions(canteen_name, 'hall14')
                    elif (da+10*a) <= cursor_position[0] <= (da+12*a) and (db+b) <= cursor_position[1] <= (db+3*b):
                        display_can_directions(canteen_name, 'hall15')
                    elif (da+12*a) <= cursor_position[0] <= (da+15*a) and (db+2*b) <= cursor_position[1] <= (db+3*b):
                        display_can_directions(canteen_name, 'tamarind')
                    elif (da+12*a) <= cursor_position[0] <= (da+15*a) and (db+3*b) <= cursor_position[1] <= (db+4*b):
                        display_can_directions(canteen_name, 'graduatehall')
                    elif (da+10*a) <= cursor_position[0] <= (da+11*a) and (db+4*b) <= cursor_position[1] <= (db+6*b):
                        display_can_directions(canteen_name, 'hall8')
                    elif (da+11*a) <= cursor_position[0] <= (da+15*a) and (db+4*b) <= cursor_position[1] <= (db+7*b):
                        display_can_directions(canteen_name, 'northhill')
                    elif (da+a) <= cursor_position[0] <= (da+7*a) and (db+4*b) <= cursor_position[1] <= (db+7*b):
                        display_can_directions(canteen_name, 'northspine')
                    elif (da + 7*a) <= cursor_position[0] <= (da+10*a) and (db+5*b) <= cursor_position[1] <= (db+6*b):
                        display_can_directions(canteen_name, 'adm')
                    elif (da + 7*a) <= cursor_position[0] <= (da+10*a) and (db+6*b) <= cursor_position[1] <= (db+8*b):
                        display_can_directions(canteen_name, 'hall2')
                    elif (da+10*a) <= cursor_position[0] <= (da+14*a) and (db+7*b) <= cursor_position[1] <= (db+8*b):
                        display_can_directions(canteen_name, 'meadow')
                    elif (da+10*a) <= cursor_position[0] <= (da+13*a) and (db+8*b) <= cursor_position[1] <= (db+11*b):
                        display_can_directions(canteen_name, 'src')
                    elif (da+a) <= cursor_position[0] <= (da+6*a) and (db+7*b) <= cursor_position[1] <= (db+11*b):
                        display_can_directions(canteen_name, 'southspine')
                    elif da <= cursor_position[0] <= (da+a) and (db+7*b) <= cursor_position[1] <= (db+11*b):
                        display_can_directions(canteen_name, 'hall7')
                    elif (da+6*a) <= cursor_position[0] <= (da+9*a) and (db+8*b) <= cursor_position[1] <= (db+12*b):
                        display_can_directions(canteen_name, 'nanyangcircle')
                    elif (da+9*a) <= cursor_position[0] <= (da+10*a) and (db+8*b) <= cursor_position[1] <= (db+10*b):
                        display_can_directions(canteen_name, 'hall6')
                    elif (da+9*a) <= cursor_position[0] <= (da+10*a) and (db+10*b) <= cursor_position[1] <= (db+12*b):
                        display_can_directions(canteen_name, 'pioneerhall')       
                    else:
                        display_message('Choose another location!', 400, 50, 0, 0, 0, 40)
                        time.sleep(0.5)
#end

#go to ntumap to display directions. By HengKai
def display_can_directions(canteen_name, from_location):
    a = canteen_name
    b = from_location
    n = 'http://maps.ntu.edu.sg/maps#q:from%20' + from_location + '%20to%20' + canteen_name
    webbrowser.open(n)
    return
#end

#change the canteen name to a name that ntu maps can understand. By HengKai
def change_name(canteen_name):
    if canteen_name == 'canteen1':
        return 'hall1'
    elif canteen_name == 'canteen2':
        return 'hall2'
    elif canteen_name == 'canteen9':
        return 'hall9'
    elif canteen_name =='canteen11':
        return 'hall11'
    elif canteen_name == 'canteen13':
        return 'hall13'
    elif canteen_name == 'canteen16':
        return 'hall16'
    elif canteen_name == 'canteenT':
        return 'tamarind'
    elif canteen_name == 'canteenN':
        return 'northhill'
    elif canteen_name == 'canteenA':
        return 'northspine'
    elif canteen_name == 'canteenB':
        return 'koufu'
    else:
        return canteen_name
#end

def display_sorted_canteen(sorted_list):  # price sorted canteen names, including GUI
    waiting = 1
    running = 1
    while waiting:
        if running:
            canteen_number = len(sorted_list)
            picture_to_be_displayed = 'Price' + str(canteen_number)
            screen.blit(eval(picture_to_be_displayed), (0, 0))  # may cause error
            pygame.display.flip()
            x = [274,810,274,810,274,810,274,810,274,810]
            y = [254,254,344,344,434,434,524,524,614,614]
            i = 0
            canteen_name = []
            canteen_manue = []
            for k,v in sorted_list.items():
                display_message(k, x[i], y[i], 0, 0, 0, 40)
                canteen_name.append(k)
                canteen_manue.append(v)
                i += 1
            running = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                auto_save()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    auto_save()
                    pygame.quit()
                if 1089 <= cursor_position[0] <= 1236 and 667 <= cursor_position[1] <= 699:
                    return 0
                elif i >= 1 and 188 <= cursor_position[0] <= 488 and 232 <= cursor_position[1] <= 307:
                    canteen_manu_display(canteen_name[0], canteen_manue[0],)
                    running = 1
                elif i >= 2 and 718 <= cursor_position[0] <= 1018 and 232 <= cursor_position[1] <= 307:
                    canteen_manu_display(canteen_name[1], canteen_manue[1],)
                    running = 1
                elif i >= 3 and 188 <= cursor_position[0] <= 488 and 320 <= cursor_position[1] <= 395:
                    canteen_manu_display(canteen_name[2], canteen_manue[2],)
                    running = 1
                elif i >= 4 and 718 <= cursor_position[0] <= 1018 and 320 <= cursor_position[1] <= 395:
                    canteen_manu_display(canteen_name[3], canteen_manue[3],)
                    running = 1
                elif i >= 5 and 188 <= cursor_position[0] <= 488 and 410 <= cursor_position[1] <= 480:
                    canteen_manu_display(canteen_name[4], canteen_manue[4],)
                    running = 1
                elif i >= 6 and 718 <= cursor_position[0] <= 1018 and 410 <= cursor_position[1] <= 485:
                    canteen_manu_display(canteen_name[5], canteen_manue[5],)
                    running = 1
                elif i >= 7 and 188 <= cursor_position[0] <= 488 and 495 <= cursor_position[1] <= 570:
                    canteen_manu_display(canteen_name[6], canteen_manue[6],)
                    running = 1
                elif i >= 8 and 718 <= cursor_position[0] <= 1018 and 495 <= cursor_position[1] <= 570:
                    canteen_manu_display(canteen_name[7], canteen_manue[7],)
                    running = 1
                elif i >= 9 and 188 <= cursor_position[0] <= 488 and 587 <= cursor_position[1] <= 662:
                    canteen_manu_display(canteen_name[8], canteen_manue[8],)
                    running = 1
                elif i >= 10 and 718 <= cursor_position[0] <= 1018 and 587 <= cursor_position[1] <= 662:
                    canteen_manu_display(canteen_name[9], canteen_manue[9],)
                    running = 1


def canteen_manu_display(name,food):  # display all menu of the selected canteen
    waiting = 1
    running = 1
    scroll_y = 0
    while waiting:
        pos_x = 540
        pos_y = 200
        if running:
            screen.blit(Blank, (0, scroll_y))
            pygame.display.flip()
            display_message(str(name), pos_x, pos_y + scroll_y, 0, 0, 0, 50)
            pos_y += 50
            pos_x -= 50
            for k_sub, v_sub in food.items():
                        display_message(str(k_sub) + ':' + str(v_sub), pos_x, pos_y + scroll_y, 0, 0, 0, 25)
                        pos_y += 30
            running = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                auto_save()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                running = 1
                pygame.display.flip()
                if event.key == pygame.K_UP:
                    scroll_y += 60
                elif event.key == pygame.K_DOWN:
                    scroll_y -= 60
            cursor_position = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.QUIT:
                    auto_save()
                    pygame.quit()
                if 1089 <= cursor_position[0] <= 1236 and 667+scroll_y <= cursor_position[1] <= 699+scroll_y:
                    return 0


def search_option():  # GUI, ask the users to choose searching type
    waiting = 1
    while waiting:
        screen.blit(Search_option, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                auto_save()
                pygame.quit()
            cursor_position = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.QUIT:
                    auto_save()
                    pygame.quit()
                if 1089 <= cursor_position[0] <= 1236 and 667 <= cursor_position[1] <= 699:
                    return 0
                elif 523 <= cursor_position[0] <= 697 and 350 <= cursor_position[1] <= 393:
                    get_user_position()
                elif 523 <= cursor_position[0] <= 697 and 429 <= cursor_position[1] <= 476:
                    price_selection()  # call price sorting function
                elif 523 <= cursor_position[0] <= 697 and 510 <= cursor_position[1] <= 558:
                    food_type_search()
                elif 523 <= cursor_position[0] <= 697 and 590 <= cursor_position[1] <= 636:
                    display_by_rank()


def price_selection():  # choose an interval of price
    waiting = 1
    while waiting:
        screen.blit(Price_selecting, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                auto_save()
                pygame.quit()
            cursor_position = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.QUIT:
                    auto_save()
                    pygame.quit()
                if 1089 <= cursor_position[0] <= 1236 and 667 <= cursor_position[1] <= 699:
                    return 0
                elif 468 <= cursor_position[0] <= 767 and 226 <= cursor_position[1] <= 300:
                    selected_list = price_whole(0,2)
                    display_sorted_canteen(selected_list)
                elif 468 <= cursor_position[0] <= 767 and 322 <= cursor_position[1] <= 391:
                    selected_list = price_whole(2, 4)
                    display_sorted_canteen(selected_list)
                elif 468 <= cursor_position[0] <= 767 and 414 <= cursor_position[1] <= 486:
                    selected_list = price_whole(4, 5)
                    display_sorted_canteen(selected_list)
                elif 468 <= cursor_position[0] <= 767 and 508 <= cursor_position[1] <= 577:
                    selected_list = price_whole(5, 6)
                    display_sorted_canteen(selected_list)
                elif 468 <= cursor_position[0] <= 767 and 599 <= cursor_position[1] <= 669:
                    selected_list = price_whole(6, 100)
                    display_sorted_canteen(selected_list)


# begin of distance function
def get_user_position():  # to let the user indicate his position
    waiting = 1
    while waiting:
        screen.blit(NTU_map, (0, 0))
        pygame.display.flip()
        cursor_position = pygame.mouse.get_pos()
        cursor_position_str = str(cursor_position)
        display_message('Current selected position:'+cursor_position_str, 400, 23, 0, 0, 0,40)
        if (1089 <= cursor_position[0] <= 1236 and 667 <= cursor_position[1] <= 699 or\
                29 <= cursor_position[0] <= 930 and 90 <= cursor_position[1] <= 703) ==0:
            display_message('You are not inside NTU!', 400, 50, 0, 0, 0, 40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                auto_save()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 1089 <= cursor_position[0] <= 1236 and 667 <= cursor_position[1] <= 699:
                    return 0
                elif 29 <= cursor_position[0] <= 930 and 90 <= cursor_position[1] <= 703:
                    cursor.location = cursor_position
                    nearest_canteen_list = distance_calculation(cursor_position)[0]
                    full_list = distance_calculation(cursor_position)[1]
                    distance_result(cursor_position_str, nearest_canteen_list, full_list)


def distance_result(cursor_position_str, nearest_canteen_list, full_list):
    # GUI display the distance result
    run = 1
    while run:
        screen = pygame.display.set_mode((1237, 700))  # set the size of the window
        screen.blit(Distance_result, (0, 0))  # display the map with specified location
        pygame.display.flip()  # update the whole screen
        display_message(cursor_position_str, 875,170,0,0,0,50)
        display_message(nearest_canteen_list[0], 544, 361, 0, 0, 0, 40)  # displays the 3 nearest canteen
        display_message(nearest_canteen_list[1], 544, 480, 0, 0, 0, 40)
        display_message(nearest_canteen_list[2], 544, 590, 0, 0, 0, 40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                auto_save()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                local_cursor_position = pygame.mouse.get_pos()
                if 1089 <= local_cursor_position[0] <= 1236 and 667 <= local_cursor_position[1] <= 699:
                    return 0
                elif 312 <= local_cursor_position[0] <= 386 and 657 <= local_cursor_position[1] <= 691:
                    display_full_distance(full_list)  # Show the full sorted list, need to be updated
                elif 444 <= local_cursor_position[0] <= 791 and 338 <= local_cursor_position[1] <= 441:
                    display_canteen_info(nearest_canteen_list[0])
                elif 444 <= local_cursor_position[0] <= 791 and 455 <= local_cursor_position[1] <= 527:
                    display_canteen_info(nearest_canteen_list[1])
                elif 444 <= local_cursor_position[0] <= 791 and 571 <= local_cursor_position[1] <= 643:
                    display_canteen_info(nearest_canteen_list[2])


def display_full_distance(full_list):  # print all canteens and corresponding distances
    waiting = 1
    running = 1
    while waiting:
        if running:
            screen.blit(Distance_list, (0, 0))
            pygame.display.flip()
            x = 200
            y = 250
            for i in full_list:
                display_message(str(i), x, y, 0, 0, 0, 40)
                y += 100
                if y >= 650:
                    y = 250
                    x += 300
            running = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                auto_save()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                local_cursor_position = pygame.mouse.get_pos()
                if 1089 <= local_cursor_position[0] <= 1236 and 667 <= local_cursor_position[1] <= 699:
                    return 0
    pass


def distance_calculation(cursor_position):  # calculate the distance and return the three nearest canteen
    can_dic = {}
    can_list = []
    x_u = cursor_position[0]
    y_u = cursor_position[1]
    n = 0
    for i in canteen:
        x_c = canteen[i][0][0]
        y_c = canteen[i][0][1]
        difference = sqrt((x_u - x_c)**2+(y_u - y_c)**2)
        can_dic[i] = int(difference)
        sorted_can_dic = sorted(can_dic.items(), key=lambda kv: kv[1])
    # print(can_dic) for test
    for j in range(0,3,1):
        can_list.append(min(can_dic, key=can_dic.get))
        can_dic.pop(can_list[n], None)
        n += 1
        # print(can_list) for test only
    return can_list, sorted_can_dic  # list contains three nearest canteen's names

# End of distance function

def get_range(dictionary, begin, end):  # choose the first five
    return dict(itertools.islice(dictionary.items(), begin, end+1))


def invert_dict(d):  # high to low
    d.reverse()
    d_dict = dict(d)
    return d_dict


def rangel(dict1,low,high):
    range_value = dict((k, v) for k, v in dict1.items() if low <= v <= high)
    return range_value


# --------------------

# begin of sort by price function: by Yang
def search_by_price(lower_price, upper_price, canteenn):  # search each canteen's manue
    sorted_by_value = sorted(canteenn.items(), key=lambda kv: kv[1]) # sort
    sorted_by_value_dict = dict(sorted_by_value)
    low = float(lower_price)
    high = float(upper_price)
    range_dishes = rangel(sorted_by_value_dict,low,high)
    return range_dishes
# ------------------price function

def price_whole(lower_price, upper_price):  # search the database for all food that meet requirement.
    range_dishes_1 = search_by_price(lower_price, upper_price,canteen1_Menue)
    range_dishes_2 = search_by_price(lower_price, upper_price,canteen2_Menue)
    range_dishes_9 = search_by_price(lower_price, upper_price,canteen9_Menue)
    range_dishes_11 = search_by_price(lower_price, upper_price,canteen11_Menue)
    range_dishes_13 = search_by_price(lower_price, upper_price, canteen13_Menue)
    range_dishes_16 = search_by_price(lower_price, upper_price, canteen16_Menue)
    range_dishes_A = search_by_price(lower_price, upper_price, canteenA_Menue)
    range_dishes_B = search_by_price(lower_price, upper_price, canteenB_Menue)
    range_dishes_T = search_by_price(lower_price, upper_price, canteenT_Meune)
    range_dishes_N = search_by_price(lower_price, upper_price, canteenN_Menue)
    whole_list_by_price= {}
    raw_dic = { 'canteen1':range_dishes_1,
                'canteen2': range_dishes_2,
                'canteen9': range_dishes_9,
                'canteen11': range_dishes_11,
                'canteen13': range_dishes_13,
                'canteen16': range_dishes_16,
                'canteenA': range_dishes_A,
                'canteenB': range_dishes_B,
                'canteenT': range_dishes_T,
                'canteenN': range_dishes_N, }

    for (k, v) in raw_dic.items():  # edited by Zhang
        if v != {}:
            whole_list_by_price.update({k:v})
    return whole_list_by_price

# This is the end of price function


# food type function starts here
def food_type_search():  # GUI, choose food preference.
    waiting = 1
    while waiting:
        screen.blit(Food_option, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                auto_save()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    auto_save()
                    pygame.quit()
                if 1089 <= cursor_position[0] <= 1236 and 667 <= cursor_position[1] <= 699:
                    return 0
                if 139 <= cursor_position[0] <= 438 and 223 <= cursor_position[1] <= 273:
                    can_list_chn = food_type_calculator("CHINESE CUSINE") # gets a list of canteens that sells this food
                    display_found_canteen(can_list_chn)
                elif 139 <= cursor_position[0] <= 438 and 229 <= cursor_position[1] <= 349:
                    can_list_can = food_type_calculator("CANTONESE")
                    display_found_canteen(can_list_can)
                elif 139 <= cursor_position[0] <= 438 and 374 <= cursor_position[1] <= 424:
                    can_list_chi = food_type_calculator("CHICKEN RICE")
                    display_found_canteen(can_list_chi)
                elif 139 <= cursor_position[0] <= 438 and 449 <= cursor_position[1] <= 499:
                    can_list_des = food_type_calculator("Desserts")
                    display_found_canteen(can_list_des)
                elif 139 <= cursor_position[0] <= 438 and 525 <= cursor_position[1] <= 573:
                    can_list_ind = food_type_calculator("INDIA")
                    display_found_canteen(can_list_ind)
                elif 139 <= cursor_position[0] <= 438 and 600 <= cursor_position[1] <= 649:
                    can_list_jap = food_type_calculator("JAPANESE")
                    display_found_canteen(can_list_jap)
                elif 470 <= cursor_position[0] <= 769 and 223 <= cursor_position[1] <= 273:
                    can_list_mix = food_type_calculator("MIXED RICE")
                    display_found_canteen(can_list_mix)
                elif 470 <= cursor_position[0] <= 769 and 229 <= cursor_position[1] <= 349:
                    can_list_pas = food_type_calculator("PASTA EXPRESS")
                    display_found_canteen(can_list_pas)
                elif 470 <= cursor_position[0] <= 769 and 374 <= cursor_position[1] <= 424:
                    can_list_veg = food_type_calculator("VEGETARIAN")
                    display_found_canteen(can_list_veg)
                elif 470 <= cursor_position[0] <= 769 and 449 <= cursor_position[1] <= 499:
                    can_list_wes = food_type_calculator("WESTERN")
                    display_found_canteen(can_list_wes)
                elif 470 <= cursor_position[0] <= 769 and 525 <= cursor_position[1] <= 573:
                    can_list_xia = food_type_calculator("XIANCAI")
                    display_found_canteen(can_list_xia)
                elif 470 <= cursor_position[0] <= 769 and 600 <= cursor_position[1] <= 649:
                    can_list_xig = food_type_calculator("XIANGGUO")
                    display_found_canteen(can_list_xig)
                elif 801 <= cursor_position[0] <= 1099 and 223 <= cursor_position[1] <= 273:
                    can_list_ytf = food_type_calculator("YONG TAU FOO")
                    display_found_canteen(can_list_ytf)


#serach canteen by food types. By HengKai
def food_type_calculator(food_type):  # search database for canteen with selected food type
    can_list = []
    for i in canteen:
        for x in canteen[i][1]:
            if food_type in x:
                can_list.append(i)
    return can_list  # return a list of canteen with the food
#end


def display_found_canteen(canteen_available):  # food type results GUI
    waiting = 1
    running = 1
    while waiting:
        if running:
            screen.blit(Food_available, (0, 0))
            pygame.display.flip()
            x = [274, 810, 274, 810, 274, 810, 274, 810, 274, 810]
            y = [354, 354, 444, 444, 534, 534, 624, 624, 714, 714]
            i = 1
            for k in canteen_available:
                display_message(str(i) + '. ' + k, x[i-1], y[i-1], 0, 0, 0, 40)
                i += 1
            running = 0
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                auto_save()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_position = pygame.mouse.get_pos()
                if 1089 <= cursor_position[0] <= 1236 and 667 <= cursor_position[1] <= 699:
                    return 0
            if event.type == pygame.KEYDOWN:
                for j in range(1, i):
                    if event.key == eval('pygame.K_' + str(j)):
                        display_canteen_info(canteen_available[j-1])
                        running = 1
                # show canteen detail pages

# End of food type function

# Begin of user rating function
def user_rating_canteen():  # GUI and choose which canteen to rate
    waiting = 1
    running = 1
    while waiting:
        if running:
            screen.blit(Rating_canteen, (0, 0))  # may cause error
            pygame.display.flip()
            running = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                auto_save()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    auto_save()
                    pygame.quit()
                if 1089 <= cursor_position[0] <= 1236 and 667 <= cursor_position[1] <= 699:
                    return 0
                elif 188 <= cursor_position[0] <= 488 and 232 <= cursor_position[1] <= 307:
                    store_selection(0)
                    running = 1
                elif 718 <= cursor_position[0] <= 1018 and 232 <= cursor_position[1] <= 307:
                    store_selection(1)
                    running = 1
                elif 188 <= cursor_position[0] <= 488 and 320 <= cursor_position[1] <= 395:
                    store_selection(2)
                    running = 1
                elif 718 <= cursor_position[0] <= 1018 and 320 <= cursor_position[1] <= 395:
                    store_selection(3)
                    running = 1
                elif 188 <= cursor_position[0] <= 488 and 410 <= cursor_position[1] <= 480:
                    store_selection(4)
                    running = 1
                elif 718 <= cursor_position[0] <= 1018 and 410 <= cursor_position[1] <= 485:
                    store_selection(5)
                    running = 1
                elif 188 <= cursor_position[0] <= 488 and 495 <= cursor_position[1] <= 570:
                    store_selection(6)
                    running = 1
                elif 718 <= cursor_position[0] <= 1018 and 495 <= cursor_position[1] <= 570:
                    store_selection(7)
                    running = 1
                elif 188 <= cursor_position[0] <= 488 and 587 <= cursor_position[1] <= 662:
                    store_selection(8)
                    running = 1
                elif 718 <= cursor_position[0] <= 1018 and 587 <= cursor_position[1] <= 662:
                    store_selection(9)
                    running = 1


def store_selection(index): # after choosing one canteen, choose a store
    waiting = 1
    running = 1
    while waiting:
        if running:
            screen.blit(Blank_null, (0, 0))
            pygame.display.flip()
            canteen_name_all = list(canteen.keys())
            canteen_name = canteen_name_all[index]
            manu_had = canteen[canteen_name][1]
            x = 300
            y = 200
            i = 1
            store_names = []
            for food in manu_had:
                display_message(str(i)+'. '+ str(food),x,y,0,0,0,40)
                store_names.append(food)
                i += 1
                y += 50
                if y >= 650:
                    y= 200
                    x += 300
            running = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                auto_save()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                for j in range(1, i):
                    if event.key == eval('pygame.K_'+str(j)):
                        rate_for_store(j, canteen_name, store_names)
                        running = 1
                        break
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    auto_save()
                    pygame.quit()
                if 1089 <= cursor_position[0] <= 1236 and 667 <= cursor_position[1] <= 699:
                    return 0


def rate_for_store(index, canteen_name, store_name_list):  # the current rating and GUI
    store_name = store_name_list[index-1]
    current_score = canteen[canteen_name][3][store_name][0]
    current_person_time = canteen[canteen_name][3][store_name][1]
    waiting = 1
    running = 1
    wait_rating = 1
    while waiting:
        if running:
            screen.blit(User_rating, (0, 0))
            pygame.display.flip()
            display_message(str(current_score),925,135,0,0,0,50)
            running = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                auto_save()
                pygame.quit()
            if wait_rating and event.type == pygame.KEYDOWN:
                for i in range(1,6):
                    if event.key == eval('pygame.K_' + str(i)):
                        display_message('You have rated: ' + str(i), 500, 400, 0, 0, 0, 40)
                        new_rate_calculation(current_score, current_person_time, i, canteen_name, store_name)
                        wait_rating = 0
                        break
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    auto_save()
                    pygame.quit()
                if 1089 <= cursor_position[0] <= 1236 and 667 <= cursor_position[1] <= 699:
                    return 0


def new_rate_calculation(current_score, current_person_time, added_rading, canteen_name, store_name):
    # update new rating to database
    total_score = current_score * current_person_time + added_rading
    canteen[canteen_name][3][store_name][0] = round((total_score)/(current_person_time + 1), 2)
    return 0

# end of rating function


# begin of the user update function
def choose_canteen():
    waiting = True
    while waiting:
        m = 1
        for i in canteen.keys():
            print(str(m) + '.'+ i , end=' ')
            m += 1
        canteen_number_str = input('Please choose one canteen (1，2，9，11，13，16, A, B, T, N): ')
        try:
            return eval('canteen' + canteen_number_str + '_Menue')
        except:
            print('Something Wrong, please try again')
            continue


def update_information():
    canteen_dishes = choose_canteen()
    waiting = 1
    while waiting:
        print('choice1: add new element; choice2: change value; choice3: change key value')
        user_selection = input('Welcome to user update, please enter number 1-3 to choose function: ')
        if user_selection.isdigit():
            seller_update(canteen_dishes, int(user_selection))
            print('Updated! Restart the pygame to refresh.') # may cause error
            auto_save()
            return 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                auto_save()
                pygame.quit()


# end of user update function
def choose_function(position):  # call one of the three main functions

        if 157 <= position[0] <=357 and 438<= position[1] <=542:

            search_option()

            return 0
        elif 519 <= position[0] <= 715 and 438<= position[1] <=542:

            user_rating_canteen()

            return 0

        elif 882 <= position[0] <=1078 and 438<= position[1] <=542:

            update_information()

            return 0


# the very beginning code
running = True  # used to terminate the programme

while running:  # main body
    screen = pygame.display.set_mode((1237, 700))  # set the size of the window
    screen.blit(Home_page, (0, 0))  # display the home page
    pygame.display.flip()  # update the whole screen
    for event in pygame.event.get():
        cursor_position = pygame.mouse.get_pos()
        mouse_state = pygame.mouse.get_pressed()
        if mouse_state[0]:

            choose_function(cursor_position)
            break
        if event.type == pygame.QUIT:
            auto_save()
            running = False

pygame.quit()

