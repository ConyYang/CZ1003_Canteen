def rate_for_store(index, canteen_name, store_name_list):
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
