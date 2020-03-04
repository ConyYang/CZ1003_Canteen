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