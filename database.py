import datetime
import pygame
import pickle

# load images
Home_page = pygame.image.load('Graph/Homepageblank/Home_page.jpg')
NTU_map = pygame.image.load('Graph/Map/NTU_map_2_1.jpg')
Search_option = pygame.image.load('Graph/Homepageblank/Search_option.jpg')
Distance_result = pygame.image.load('Graph/distance/distance_result_new.jpg')
Canteen_information_blank = pygame.image.load('Graph/Homepageblank/canteen_information_blank.jpg')
Food_option = pygame.image.load('Graph/foodtype/food_option.jpg')

Price_selecting = pygame.image.load('Graph/Price/price_selecting.jpg')
Food_available= pygame.image.load('Graph/foodtype/food_result.jpg')
Priced_dishes = pygame.image.load('Graph/Price/price_sorted_dishes_3.jpg')

Price10 = pygame.image.load('Graph/Price/price_10.jpg')
Price9 = pygame.image.load('Graph/Price/price_9.jpg')
Price8 = pygame.image.load('Graph/Price/price_8.jpg')
Price7 = pygame.image.load('Graph/Price/price_7.jpg')
Price6 = pygame.image.load('Graph/Price/price_6.jpg')
Price5 = pygame.image.load('Graph/Price/price_5.jpg')
Price4 = pygame.image.load('Graph/Price/price_4.jpg')
Price3 = pygame.image.load('Graph/Price/price_3.jpg')
Price2 = pygame.image.load('Graph/Price/price_2.jpg')
Price1 = pygame.image.load('Graph/Price/price_1.jpg')


Blank = pygame.image.load('Graph/Homepageblank/blank_2.jpg')
Blank_null = pygame.image.load('Graph/Homepageblank/blank.jpg')

Rating_canteen = pygame.image.load('Graph/rankrating/rating_canteen.jpg')
User_rating = pygame.image.load('Graph/rankrating/user_rate_page.jpg')
Distance_list = pygame.image.load('Graph/distance/full_distance_list.jpg')

canteen1_img = pygame.image.load('Graph/canteenimage/canteen1_img.jpg')
canteen2_img = pygame.image.load('Graph/canteenimage/canteen2_img.png')
canteen9_img = pygame.image.load('Graph/canteenimage/canteen9_img.png')
canteen11_img = pygame.image.load('Graph/canteenimage/canteen11_img.png')
canteen16_img = pygame.image.load('Graph/canteenimage/canteen16_img.png')

canteenT_img = pygame.image.load('Graph/canteenimage/canteenT_img.jpg')
canteenN_img = pygame.image.load('Graph/canteenimage/canteenN_img.jpg')
canteen13_img = pygame.image.load('Graph/canteenimage/canteen13_img.png')
canteenA_img = pygame.image.load('Graph/canteenimage/northspine_img.png')
canteenB_img = pygame.image.load('Graph/canteenimage/koufu_img.png')

rank_option = pygame.image.load('Graph/rankrating/rank_display.jpg')

rank_canteenfull_option = pygame.image.load('Graph/rankrating/canteenfullrank.jpg')


#canteen information [name, address, telephone, opening hours, stalls, seating capacity]
canteen1_info = ["Food Court 1", "Hall 1, 21 Nanyang Circle, Singapore 639778", "Tel: 6334 3033", "Daily: 7am to 9pm", "Stalls: 9", "Seating capacity: 310"]
canteen2_info = ["Food Court 2", "Hall 2, 35 Students Walk, Singapore 639548", "Tel: 6334 3003", "Daily: 7am to 9pm", "Stalls: 10", "Seating capacity: 446"]
canteen9_info = ["Food Court 9", "Hall 9, 50 Nanyang Avenue, Singapore 639798", "Hp: 9692 3456", "Daily: 7am to 9pm", "Stalls: 9", "Seating capcity: 293"]
canteen11_info = ["Food Court 11", "Hall 11, 20 Nanyang Avenue, Singapore 639809", "Hp: 9786 6726", "Daily: 7am to 9pm", "Stalls: 6", "Seating capacity: 210"]
canteen13_info = ["Food Court 13", "Hall 13, 32 Nanyang Crescent, Singapore 637658", "Hp: 9851 0908", "Daily: 7am to 9pm", "Stalls: 8", "Seating capacity: 210"]
canteen16_info = ["Food Court 16", "Hall 16, 50 Nanyang Walk, Singapore 639929", "Hp: 9450 5893", "Daily: 7am to 9pm", "Stalls: 5", "Seating capacity: 304"]
canteenA_info = ["NS Food Court", "North Spine Plaza, 76 Nanyang Drive", "Tel: 6465 8588", "Mon to Fri: 7am to 9pm, Sat: 7am to 3pm", "Stalls: 19", "Seating capacity: 1838"]
canteenB_info = ["Koufu @ SS","50 Nanyang Avenue, Singapore 639798", "Tel: 6790 0355", "Mon to Fri: 7am to 9pm, Sat: 7am to 3pm", "Stalls: 15", "Seating capcity: 1050"]
canteenT_info = ["Tamarind Food Court", "Blk 23, 38 Nanyang Crescent, Singapore 636866", "Hp: 8296 3633", "Daily: 7am to 9pm", "Stalls: 9", "Seating capacity: 440"]
canteenN_info = ["North Hill Food Court", "Blk 21A, 60 Nanyang Crescent, Singapore 636957", "Hp: 8508 0232", "Daily: 7am to 9pm", "Stalls: 8", "Seating capacity: 440"]

# location
location1 = (471,475)
location2 = (509,408)
location9 = (630,285)
location11= (738,240)
location13 = (474,172)

location16 = (429,219)
locationB = (231,498)
locationA = (285,291)
locationT = (688,194)
locationN = (761,293)

# canteen 1
remaining_openhour1 = 21 - datetime.datetime.now().hour
rating_1 = {'CHINESE CUSINE':[5,1],'INDIA':[5,1],
             'PASTA EXPRESS':[5,1],'VEGETARIAN':[5,1]}
foodtype1 = {'CHINESE CUSINE':4.56,'INDIA':3.01,
             'PASTA EXPRESS':5.55,'VEGETARIAN':7.30}
# canteen 2
remaining_openhour2 = 21 - datetime.datetime.now().hour
rating_2 = {'CHINESE CUSINE':[5,1],
             'Desserts':[5,1],'INDIA':[5,1],'JAPANESE':[5,1],'MIXED RICE':[5,1],
             'WESTERN':[5,1],
             'XIANCAI':[5,1],'YONG TAU FOO':[5,1]}
foodtype2 = {'CHINESE CUSINE':2.97,
             'Desserts':1.8,'INDIA':2.43,'JAPANESE':3.83,'MIXED RICE':2.40,
             'WESTERN':6.06,
             'XIANCAI':7.31,'YONG TAU FOO':3.65}
# canteen 9
remaining_openhour9 = 21 - datetime.datetime.now().hour
rating_9 = {'CHINESE CUSINE':[5,1],
             'Desserts':[5,1],'JAPANESE':[5,1],
             'XIANCAI':[5,1],'XIANGGUO':[5,1]}
foodtype9 = {'CHINESE CUSINE':3.08,
             'Desserts':1.95,'JAPANESE':6.0,
             'XIANCAI':2.65,'XIANGGUO':6.50}
#canteen 11
remaining_openhour11 = 21 - datetime.datetime.now().hour
rating_11 = {'CHICKEN RICE':[5,1],'INDIA':[5,1],
              'VEGETARIAN':[5,1],'WESTERN':[5,1],
                  'YONG TAU FOO':[5,1]}
foodtype11 = {'CHICKEN RICE':6.30,'INDIA':3.20,
              'VEGETARIAN':6.77,'WESTERN':3.42,
                  'YONG TAU FOO':3.42}
#canteen 13
remaining_openhour13 = 21 - datetime.datetime.now().hour
rating_13 = {'Desserts':[5,1],'INDIA':[5,1],'JAPANESE':[5,1],
              'MIXED RICE':[5,1],'XIANCAI':[5,1]}
foodtype13 = {'Desserts':3.20,'INDIA':5.12,'JAPANESE':4.80,
              'MIXED RICE':6.20,'XIANCAI':4.52}

#canteen 16
remaining_openhour16 = 21 - datetime.datetime.now().hour
rating_16 = { 'PASTA EXPRESS':[5,1],'VEGETARIAN':[5,1],'WESTERN':[5,1],
                'XIANCAI':[5,1],'XIANGGUO':[5,1],'YONG TAU FOO':[5,1]}
foodtype16 = { 'PASTA EXPRESS':4.30,'VEGETARIAN':3.20,'WESTERN':7.00,
                'XIANCAI':3.78,'XIANGGUO':6.27,'YONG TAU FOO':4.29}

# canteen A
remaining_openhourA = 21 - datetime.datetime.now().hour
rating_A = {'CHINESE CUSINE':[5,1],
             'Desserts':[5,1],'JAPANESE':[5,1],
             'XIANCAI':[5,1],'XIANGGUO':[5,1]}
foodtypeA = {'CHINESE CUSINE':3.08,
             'Desserts':1.95,'JAPANESE':6.0,
             'XIANCAI':2.65,'XIANGGUO':6.50,}

# canteen B
remaining_openhourB = 21 - datetime.datetime.now().hour
rating_B = {'CHINESE CUSINE':[5,1],'CHICKEN RICE':[5,1],
             'Desserts':[5,1],'INDIA':[5,1],'JAPANESE':[5,1],'MIXED RICE':[5,1],
             'PASTA EXPRESS':[5,1],'VEGETARIAN':[5,1],
             'YONG TAU FOO':[5,1]}
foodtypeB = {'CHINESE CUSINE':2.96,'CHICKEN RICE':2.81,
             'Desserts':2.00,'INDIA':3.12,'JAPANESE':3.62,'MIXED RICE':2.72,
             'PASTA EXPRESS':3.42,'VEGETARIAN':2.51,
             'YONG TAU FOO':3.50}

#canteen tamarind
remaining_openhourT = 21-datetime.datetime.now().hour
rating_T = {'CANTONESE': [5,1], 'Desserts': [5,1],
             'JAPANESE': [5,1],   'XIANGGUO': [5,1],
             'PASTA EXPRESS':[5,1]}
foodtypeT = {'CANTONESE': 5.20, 'Desserts': 1.45,
             'JAPANESE':6.10,   'XIANGGUO': 3.12,
             'PASTA EXPRESS':4.50}

#canteen NorthHill
remaining_openhourN = 21-datetime.datetime.now().hour
rating_N = {'INDIA':[5,1],'JAPANESE':[5,1],'MIXED RICE':[5,1],
             'PASTA EXPRESS':[5,1],'VEGETARIAN':[5,1],'WESTERN':[5,1]}
foodtypeN = {'INDIA':4.70,'JAPANESE':6.60,'MIXED RICE':4.80,
             'PASTA EXPRESS':6.00,'VEGETARIAN':3.70,'WESTERN':5.78}

# --------------------------------------------------------------------------------------------------------

# canteen1_shop_menue
canteen1_CC_Menue = {'XiaolongBao': 2.56,         'Beijing Duck': 6.78,
                     'Braised Pork Leg': 7.23,    'egg in tea': 3.51,
                     'Meat Balls': 5.90,          'Fry chicken': 8.92}
canteen1_I_Menue =  {'Hors dOeuveres':7.00,       'Samosa':7.21,
                     'Shashlik':2.50,             'chickpea':1.70,
                     'cheese':  1.23,             'cottage':1.25}
canteen1_P_Menue =  {'vegetable fritters': 1.20,  'Spicy potatoes': 1.50,
                     'lenti wafers':1.56}
canteen1_V_Menue =  {'Vegetable Rice':7.82,       'Vegetable combo':1.90,
                     'Orange and Tomato':6.40,    'Valentine': 7.92}
canteen1_Menue = {**canteen1_CC_Menue,**canteen1_I_Menue,**canteen1_P_Menue,**canteen1_V_Menue}
# --------------------------------------------------------------------------------------------------------

# canteen2_shop_menue
canteen2_CC_Menue = {'Steamed Chicken rice':2.80, 'Roasted Meat Rice':3.00,
                     'BBQ Pork Rice':3.00,        'Lemon Chicken rice':3.00,
                     'Chicken Laksa':3.50,        'Winter Melon Prok Rib':2.50}
canteen2_D_Menue  = {'Tuna Sandwiches':1.60,      'Egg Sandwiches':1.60,
                     'Breakfast Set':1.80,        'Iced Cocoa Dino':2.20}
canteen2_I_Menue  = {'Roll Boom':2.00,            'Roll John':3.00,
                    'Mertabk':2.20,               'George':2.50}
canteen2_J_Menue  = {'BBQ Beef':4.90,             'BBQ Chickn':4.30,
                    'Sun Du Bu': 4.00,            'Kim Chi Chi Gao':4.00,
                    'Bulgogi':4.30,               'Ginseng Chicken Soup':5.50,
                    'Ramen': 2.80,                'Korean Rice cake':3.80}
canteen2_M_Menue  = {'1 veg+ 1meat': 1.80,        '1 veg + 1 fish':2.20,
                     '1 Veg + 1Sotong': 2.70,     '2veg + 2 meat':2.90}
canteen2_W_Menue  = {'Plain Yakisoba':4.00,       'Chicken egg Veg don':5.50,
                     'chicken Kato Curry':5.50,   'Seafood Plaze':4.90,
                     'Frilled Chicken':4.50,      'Carbonara':3.80,
                     'seafood chicken sousage':3.80,
                     'cream Spagetti':4.00,       'vegetarian':3.80}
canteen2_XA_Menue = {'Sauteed Mutton': 7.50,      'Sauted Pig': 6.50,
                     'Sweet and Sour Pork': 6.00, 'Mushroom Cabbage':4.50,
                     'Stir fried Eggs & Tomatoes': 4.50,
                     'Saulted egg': 8.00,
                     'Sichaun Chilli Ribs':7.50,  'Seaweed Soup':4.00}
canteen2_Y_Menue  = {'Superior Bone Broth Set Meal':4.00,
                    'Sliced Pork/Beef':3.80,      'Yong Ta Foo': 4.00,
                    'Handmade Noodle': 2.80}
canteen2_Menue = {**canteen2_CC_Menue,**canteen2_D_Menue,**canteen2_I_Menue,**canteen2_I_Menue,**canteen2_J_Menue,
                  **canteen2_M_Menue, **canteen2_W_Menue,**canteen2_XA_Menue,**canteen2_Y_Menue}

# --------------------------------------------------------------------------------------------------------
# canteen9_shop_menue
canteen9_CC_Menue = {'Mixed Veg':2.50,            'Shrimped Fried Rice':3.00,
                     'Seafood':3.00,              'Fried Beef Hefen':3.00,
                     'Beef Rice wirh Ginger & Onion':3.50,
                     'Black Pepper Beef Rice':3.50}
canteen9_D_Menue =  {'Breakfast Set1':1.70,       'Breakfast Set2':1.70,
                    'Breakfast set3':2.20,        'Breakfast Set4':2.20}
canteen9_J_Menue =  {'Special Tankatsa Ramen':6.90,
                     'Original Ramen':4.80,       'Red Ramen':6.00,
                     'Black Ramen':6.00,          'Vegetable Ramen':6.00}
canteen9_XC_Menue = {'ShaoZiMian':2.70,           'Tomato &Egg Handmade Noodle':2.50,
                     'Spicy Veg Handmade Noodle':2.70,
                     'YouPoMian':2.70}
canteen_XG_Menue =  {'4Veg+BrownRice':5.30,       '4Veg+Chicken':6.80,
                    '4Veg+Beef':7.30,             '4Veg+HandmadeNoodle':5.40}
canteen9_Menue = {**canteen9_CC_Menue,**canteen9_D_Menue,**canteen9_J_Menue,**canteen9_XC_Menue,**canteen_XG_Menue}

# --------------------------------------------------------------------------------------------------------
# canteen11_shop_menue
canteen11_CR_Menue = {'Shrimp Noodle': 3.50,            'Dazhaxie':8.90,
                      'Fried Water Crab Meat':4.20,     'Lotus Root': 6.59,
                      'Braised River Carp':2.10,        'Radish Soup':1.20}
canteen11_I_Menue  = {'Fish Roll Soy Source':6.40,      'Fillet with Gingko':8.50,
                      'Sluggish-Clearing Soup':3.70,    'Stewed Mussel':3.20,
                      'Indian Style Duck':2.30,         'Spicy Orange Beef':5.11}
canteen11_V_Menue  = {'Tuna Rice with Ark Shell':4.50,
                      'Yellow Tail':6.22,               'Octopus Rice':4.33,
                      'Sea urchin': 1.21,               'Sea Bream': 1.38,
                      'VInegarish Octopus':2.30}
canteen11_W_Menue  = {'Cream of Mushroom Soup':3.10,    'Cream of Carrot Soup': 5.55,
                      'Traditional Tomato Soup':5.15,
                      'Deep-Fried Chicken': 4.30,       'Bacon Rolls':2.33}
canteen11_Y_Menue  = {'Yak Ear':1.87,                   'Boiled Chicken Slice':3.10,
                      'Seaweed in Sauce':1.64,          'Toon in Sauce':3.67,
                      'Bitter Melon with Sashimi':3.59, 'Shredded Dried Tofu':3.82}
canteen11_Menue = {**canteen11_CR_Menue,**canteen11_I_Menue,**canteen11_V_Menue,**canteen11_W_Menue,**canteen11_Y_Menue}

# --------------------------------------------------------------------------------------------------------
# canteen13_shop_menue
canteen13_D_Menue = {'Mango Pancake':1.75,      'Banana Pancake':1.40,
                     'Red bean Gultinous Dumpling':3.10,
                     'Milk Pudding':0.80,        'coconut Pudding':0.80,
                     'Durian Pudding':1.00,      'Strawberry Pudding':1.20}
canteen13_I_Menue = {'Palak Rolls':1.42,         'Vegetable Samosa(vegan)':0.80,
                     'Tamatar Ka Saar':3.44,     'Mulligatwany Soup':7.20,
                     'Smoked Eggplant Raita':3.80,
                     'Cucumber Raita':0.80,       'Rainbow Salad':1.00}
canteen13_J_Menue = {'Japanese Style Salad':3.00, 'Simmered Tofu&Beef':2.20,
                     'Marinated Squid':3.10,      'Stir Vegetables':8.10,
                     'Assorted Deed fried':7.25,  'Clear Soup':6.80,
                     'Grilled Head of salmon':5.99}
canteen13_M_Menue = {'Fresh soybean Cake':1.70,   'Grated Radish':0.70,
                     'Meat Tofu':5.32,            'Cabbage rice':3.20,
                     'Carrot rice':3.24,          'Broccolli Rice':7.54}
canteen13_XA_Menue = {'Standard MeiGanCai':1.90,   'Baked Egg mulk':3.00,
                     'Tossed Clear Noodles':5.80, 'Dezhou Chicken':6.10,
                     'Sliced OX Toungue':3.51,    'Iced Chinese Broccoli':7.11}
canteen13_Menue = {**canteen13_D_Menue, **canteen13_I_Menue, **canteen13_J_Menue, **canteen13_M_Menue, **canteen13_XA_Menue}
# --------------------------------------------------------------------------------------------------------
# canteen16_shop_menue
canteen16_P_Menue = {'T-Bone Steak':6.30,    'Sizzling Sirloin Steak':5.70,
                     'BArbecued Ribs':4.32,  'Pork Piccatta':8.20,
                     'Lamb Chop':1.80,       'Mutton Leg':6.20,
                     'Seafood Kebas':2.30}
canteen16_V_Menue = {'Bocky Roll':5.20,      'Fresh Walnuts in Sauce':3.00,
                     'Spinach Soup':3.20,    'Chinese Cabbage':7.00,
                     'Black Fungus in Sauce':4.30}
canteen16_W_Menue = {'Beef Burger':3.50,     'Chicken Burger':4.50,
                     'American Hot dog':7.30,'Beef Sandwhiches':2.00,
                     'Smoked Salmon':3.50,   'Mashed Potatoes Sweet':1.50,
                     'sweet Corn with source':1.52}
canteen16_XA_Menue = {'White Gourd and cuttlefish soup':3.77,
                      'Carrot and fish soup':7.50,
                      'Stewed Crab in Terrine':6.12,
                      'Three-skin slice':2.50,
                      'Sliced egg yolk':1.10, 'Fried meat balls':2.00}
canteen16_XG_Menue = {'Beef Tendon Soup':5.40, 'Rice Mash and Yam':3.00,
                      'Drug Soup':6.99,        'Frog Soup':8.40}
canteen16_Y_Menue = {'Silver Mushroom':3.40,   'Chinese Wolfberry':7.20,
                     'Fried Pork Spicy':4.40,
                     'Beeled Squid':5.50,      'Chicken in Shap':5.42}
canteen16_Menue = {**canteen16_P_Menue,**canteen16_V_Menue,**canteen16_W_Menue,
                   **canteen16_XA_Menue,**canteen16_XG_Menue,**canteen16_Y_Menue}

# --------------------------------------------------------------------------------------------------------
# canteenA_shop_menue
canteenA_J_Menue  = {'Hotplate Soba Set':5.50,   'Hotplate Pork Set':5.80,
                     'Hotplate Chicken + Beef Set': 5.80,
                     'Bimbibap':4.80,            'Chicken/Pork Rice Set':4.20,
                     'Kimichi Fried Rice':4.00,  'Hot Plate Beef Rice':6.20,
                     'Chicken Kimichi Soup':4.00,'Seafood Kimichi Soup':4.50}
canteenA_P_Menue =  {'Chicken Set':4.80,         'Fish Set':4.80,
                     'Meat Set':5.80,            'Pasta':4.20,
                     'Side Order':3.20,           'Combo Set': 7.80}
canteenA_XA_Menue = {'Spicy & Sour Noodle':4.20, 'ZhaJiang Noodle':4.20,
                     'Pork Rib Noodle':4.20,     'Beef Noodle':5.20,
                     'Liang Pi':3.20,            'Wonton Soup':3.20,
                     'Biang Biang Noodle':3.20,  'Fried egg & Tomato Noodle':4.20,
                     'Rou Jia Mo':2.80,          'Steamed Veg':2.20}
canteenA_XG_Menue = {'3VegA+2VegB':6.40,         '2VegA+3VegB':6.60,
                     '3VegA+2Meat':7.20,         '2Veg+2Seafood':8.20}
canteenA_Menue = {**canteenA_J_Menue,**canteenA_P_Menue,**canteenA_XA_Menue,**canteenA_XG_Menue}

# --------------------------------------------------------------------------------------------------------
# canteenB_shop_menue
canteenB_CC_Menue = {'Hot & Spicy Meat Set':2.50, 'Healthy Set':2.50,
                     'Pineapple/Chicken Set':2.50,'3 flavours Set':2.90,
                     'Fried Meat Ball Set':3.50,  'Home-Cookied Rice Set':3.50,
                     'Mala Beef Noodle':3.30,     'Bean Paste Noodle':3.00}
canteenB_CR_Menue = {'Roasted Chicken Rice':2.50, 'Steamed Chicken Rice':2.50,
                     'Char Stew Rice':3.00,       'Steamed Fork Rice':3.00,
                     'Roasted Chicken Rice Set':4.0,
                     'Thai Style Chicken Cutlet Rice':2.50,
                     'Lemon Chicken Cutlet Rice':2.50,
                     'Mayonnaise Chicken Cutlet':2.50}
canteenB_D_Menue = {'Tao Suan+Spring Roll':2.00,    'Cheng Tng+Peanut Sessame Ball':2.00,
                    'Red Bean Soup+Green Bean Sesame Ball':2.00,
                    'Green Bean Soup+Big Pau':2.00, 'Pulut Hitam+Chwee Kueh':2.00,
                    'Ginkgo Nuts Soup+BBQ Pau':2.00}
canteenB_I_Menue = {'Biryani Dum Set A':3.00,       'Tandoori Naan Set':3.50,
                    'Chicken/Saedine Murtabak':3.00,'Chapati Set':3.00,
                    'Poori Set':2.50,               'Mee Goreng/NasiGorgeng':2.50}
canteenB_J_Menue = {'Chicken Karrage Don':3.30,     'Chicken Katsu Don':3.50,
                    'Tartkayi Chicken Don':3.30,    'Teriyaki Salmon Don':4.00,
                    'Ebi Fry Don':3.70,             'Curry Chicken Don':3.60,
                    'Horplate Ebi Fuyong':3.90,     'Hotplate Chicken Fuyong':3.70}
canteenB_M_Menue = {'1Meat+1Veg':1.90,   '1Meat+2Veg':2.40,
                    '2Meat+1Veg':3.00,   '2Meat+2Veg':3.60,}
canteenB_P_Menue = {'Tomato+Ham+Olives':3.30,        'Spicy+Pepperoni+Mushroom':3.30,
                    'Cream+Bacon+Onions':3.30,       'AglioOlio+Beef+Corn+Egg':3.80,
                    'Tomato+Bacon+Beef+Onions':4.30, 'Cream+Chicken+Beef+Onions':4.30}
canteenB_V_Menue = {'Curry Noodles':2.30, 'Yeg Kway Chap':2.50, 'Veg Laksa':2.50,
                    'Veg Lor Mee':  2.50, 'Veg Longtong':2.50,  'Veg Hor Fun':2.80,
                    'Veg Tom YUm Seafood':2.80, 'Veg Hereal Mutton':2.80, 'Veg Chicken Rice':2.80}
canteenB_Y_Menue = {'6 Pieces':3.00, '6P+Rice/Noodles': 3.50, '6P+Laksa':3.50, '6P+Noodles+Laksa':4.00}

canteenB_Menue = {**canteenB_CC_Menue, **canteenB_CR_Menue, **canteenB_D_Menue, **canteenB_I_Menue,
                     **canteenB_J_Menue,**canteenB_M_Menue,**canteenB_P_Menue,**canteenB_V_Menue,**canteenB_Y_Menue}

# --------------------------------------------------------------------------------------------------------
# canteenT_shop_menue
canteenT_CT_Menue = {'Spiced Beef ':7.92,         'Steamed Duck Rice':6.70,
                     'Banana Ball': 4.50,         'Chicken Soup': 2.60,
                     'Crisp Goose': 7.80,         'Mellon':1.20}
canteenT_D_Menue =  {'Apple Juice':1.20,          'Cola':1.30,
                     'Buda Drink': 1.40,          'Bloody Marry':1.50}
canteenT_J_Menue =  {'Toufu Sushi': 2.40,         'Monster Sushi': 7.80,
                     'Big Big Sushi':6.00,        'Super Big Sushi':8.00,
                     'Spicy Garlley': 4.50,       'Super spicy Garlley':5.63}
canteenT_XG_Menue = {'LongShrimp': 2.45,          'Spicy Vegetable': 3.45,
                     'Paotong': 3.00,             'GaoPaoTong':3.10}
canteenT_P_Menue  = {'Mushroom Pizza': 3.80,      'Lettuce Pizza':3.40,
                     'Oliver Pizza': 4.72,        'Julia Pizza': 5.10}
canteenT_Meune = {**canteenT_CT_Menue,**canteenT_D_Menue,**canteenT_J_Menue,**canteenT_XG_Menue,**canteenT_P_Menue}

# --------------------------------------------------------------------------------------------------------
# canteenN_shop_menue
canteenN_I_Menue = {'Lily Soup':2.30,              'Indian Roppi':3.68,
                    'Tandoori':3.33,               'Fish Tikka':2.80,
                    'Boti Kebab':4.73,             'Tandorri chicken':5.80,
                    'Mala Chicken Tika':1.72}
canteenN_J_Menue = {'Green Tea Ramen':3.40,       'Miso Noodle':5.40,
                    'Prok Rib Noodle':6.80,       'Mix Vegetable Noodle':2.80,
                    'Hot Chili Noodle':7.60,      'Cold Noodle':4.60,
                    'Chilled Japanese Udon':7.30}
canteenN_MR_Menue = {'Black Bean Rice':3.50,      'chicken Scallion rice': 4.60,
                     'Kimichi fried rice':2.50,   'Sichuan Sausage Rice':2.80,
                     'Fried Shrimp rice':8.50,    'Rabbit Meat Rice':6.20}
canteenN_P_Menue = {'Duchesse Potatotes':3.60,    'Cabbage with apple':4.90,
                    'Healthy Sandwich with Tomato': 4.70,
                    'Club Beef Combo':5.70,       'American Hot Dog':5.00,
                    'Chicken Butter Buger':4.30,  'Paella':3.20}
canteenN_V_Menue = {'Prawn Aloo':6.25,            'Butter Platter':1.30,
                    'Vegetable shashlik':1.35,    'Palak Rolls':3.48,
                    'Onion Bhaijs':3.93,          'Mulligatwany Soup':7.28,
                    'Boti Kebab':3.98}
canteenN_W_Menue = {'Griolled Red snapper Fillet':7.38,
                    'Baked Lobster':4.92,         'Deep-fried squid rings':6.49,
                    'Quiche Lorraine':3.92,       'Macaroni with Seafood':8.68}
canteenN_Menue = {**canteenN_I_Menue,**canteenN_J_Menue,**canteenN_MR_Menue,
                  **canteenN_P_Menue,**canteenN_V_Menue,**canteenN_W_Menue}



# canteen-----------------------------------------------------------------------------------------------------------
canteen = {'canteen1':[location1,foodtype1,remaining_openhour1,rating_1,canteen1_info],
           'canteen2':[location2,foodtype2,remaining_openhour2,rating_2,canteen2_info],
           'canteen9':[location9,foodtype9,remaining_openhour9,rating_9,canteen9_info],
          'canteen11':[location11,foodtype11,remaining_openhour11,rating_11,canteen11_info],
          'canteen13':[location13,foodtype13,remaining_openhour13,rating_13,canteen13_info],
          'canteen16':[location16,foodtype16,remaining_openhour16,rating_16,canteen16_info],
           'canteenA':[locationA,foodtypeA,remaining_openhourA,rating_A,canteenA_info],
           'canteenB':[locationB,foodtypeB,remaining_openhourB,rating_B,canteenB_info],
           'canteenT':[locationT,foodtypeT,remaining_openhourT,rating_T,canteenT_info],
           'canteenN': [locationN, foodtypeN, remaining_openhourN,rating_N,canteenN_info]}




canteen_img = {'canteen1':canteen1_img,
               'canteen2':canteen2_img,
               'canteen9':canteen9_img,
               'canteen11':canteen11_img,
               'canteen13':canteen13_img,
               'canteen16':canteen16_img,
               'canteenB':canteenB_img,
               'canteenA':canteenA_img,
               'canteenT':canteenT_img,
               'canteenN':canteenN_img}

# canteen_rating = {**{'canteen1':rating_1},**{'canteen2':rating_2},
#                   **{'canteen9':rating_9},**{'canteen11':rating_11},
#                   **{'canteen13':rating_13},**{'canteen16':rating_16},
#                   **{'canteenA':rating_A},**{'canteenB':rating_B},
#                   **{'canteenT':rating_T},**{'canteenN':rating_N}}


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
