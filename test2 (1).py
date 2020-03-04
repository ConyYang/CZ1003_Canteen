import pygame


pygame.init()  # initialize pygame

pygame.display.set_caption("NTUFood")  # set the window's caption
Home_page = pygame.image.load('/Users/zhangxinyi/Documents/untitled/Home_page.jpg')
NTU_map = pygame.image.load('/Users/zhangxinyi/Documents/untitled/NTU_map_2.png')  # load the ntu map (on my computer)
screen = pygame.display.set_mode((1237, 700))  # set the size of the window
screen.blit(Home_page, (0, 0))  # display the map with specified location
pygame.display.flip()  # update the whole screen
Test_d = pygame.image.load('/Users/zhangxinyi/Documents/untitled/price_10.jpg')
running = True  # used to terminate the programme


def display_message(str, a, b, R, G, B, size):  # a,b is coordinator
    my_font = pygame.font.SysFont("Monaco", size)
    text = my_font.render(str, 1, (R, G, B))
    screen.blit(text, (a,b))
    pygame.display.update()


def mouse_position():  # to display the cursor's position
    waiting = 1
    while waiting:
        screen.blit(Test_d, (0, 0))
        cursor_position = pygame.mouse.get_pos()
        cursor_position_str = str(cursor_position)
        display_message('Current selected position:'+cursor_position_str, 0, 0, 0, 0, 0,40)
        display_message('Please click on ', 940, 23, 255, 255,255,35)
        display_message('the corresponding area', 940,46, 255, 255,255,35)
        display_message('of the map to show ', 940, 69, 255, 255,255,35)
        display_message('your current location', 940, 92, 255, 255,255,35)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = 0
                food_preference()


def food_preference():  # once the location was selected, ask for food preference
    screen = pygame.display.set_mode((1237, 700))
    cursor_position = pygame.mouse.get_pos()
    cursor_position_str = str(cursor_position)
    display_message('You have select position (x,y)='+ cursor_position_str, 0,0,255,255,255,40)
    nearest_canteen_list = distance_calculation(cursor_position)
    nearest_canteen_list_str = ''
    for i in range(0,3):  # program breaks down here since the list contains nothing now.
        nearest_canteen_list_str = nearest_canteen_list_str + ',' + str(nearest_canteen_list[i])
        # not tested, but i think .render only accept strings
    display_message('The nearest canteens are:'+ nearest_canteen_list_str, 0, 50, 255,255,255,40)


def distance_calculation(current_position):
    pass
    return []  # list contains three nearest canteen's names


def user_rating():
    pass


def update_information():
    pass


def choose_function(position):
    waiting = 1
    while waiting:

        if 157 <= position[0] <=357 and 438<= position[1] <=542:
            waiting = 0

            mouse_position()

        elif 519 <= position[0] <= 715 and 438<= position[1] <=542:
            waiting = 0
            user_rating()

        elif 882 <= position[0] <=1078 and 438<= position[1] <=542:
            waiting = 0
            update_information()


while running:  # main body
    for event in pygame.event.get():
        cursor_position = pygame.mouse.get_pos()
        mouse_state = pygame.mouse.get_pressed()
        if mouse_state[0]:
            choose_function(cursor_position)

        if event.type == pygame.QUIT:
            running = False

pygame.quit()
