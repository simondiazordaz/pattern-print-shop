#functions for patterns and shapes 

import shapes 

 

#initializing variables 

in_shop = True
pattern_choice = ""
shape_choice = ""
mod_choice = ""
exit_shop = "0"
 

#shopping interface where user can choose patterns 

print(f"Welcome to the Pattern Print Shop. Please select from the following menu:\n") 

while in_shop: #keeps user in shop until they choose to exit
    
    pattern_choice = ""
    shape_choice = ""
    mod_choice = ""
    exit_shop = "0"
    x = ""
    y = ""
    symbol = "a"
    
    while not(pattern_choice == "A" or pattern_choice == "B" or pattern_choice == "C" or pattern_choice == "Q"): 
        print(f"\nA- To print a rectangle" 

            f"\nB- To print a pyramid" 

            f"\nC- To print a diamond" 

            f"\n" 

            f"\nQ- Quit the shop" 

            f"\n") 

        pattern_choice = str(input()) 

 

#pattern and shape selection 

    if pattern_choice == "A": #prints rectangles 

        while type(x) != int:
            x = input("\nEnter a width: ")
            if x.isdigit() == True:
                x = int(x)
        while type(y) != int:
            y = input("Enter a height: ")
            if y.isdigit() == True:
                y = int(y)
        while symbol.isalpha() == True:
            symbol = input("Please pick a symbol; !, @, #, $, %, ^, &, *, or numbers: ")
        while not(shape_choice == "1" or shape_choice == "2" or shape_choice == "3"):
            print(f"\nSelect a rectangle type:\n" 

            f"\n1- Hollow rectangle" 

            f"\n2- Solid rectangle" 

            f"\n3- Return to main menu" 

            f"\n") 

            shape_choice = str(input()) 

        if shape_choice == "1": 

            shapes.hollow_rectangle(symbol, x, y) 

        elif shape_choice == "2": 

            shapes.solid_rectangle(symbol, x, y) 

        else: 

            pattern_choice = "init"

    elif pattern_choice == "B": #prints pyramids 
        while type(y) != int:
            y = input("\nEnter a height: ")
            if y.isdigit() == True:
                y = int(y)
        while symbol.isalpha() == True:
            symbol = input("Please pick a symbol; !, @, #, $, %, ^, &, *, or numbers: ") 
        while not(shape_choice == "1" or shape_choice == "2" or shape_choice == "3"): 
            print(f"\nSelect a pyramid type:\n" 
            f"\n1- Half pyramid" 
            f"\n2- Full pyramid" 
            f"\n3- Return to main menu" 
            f"\n") 
            shape_choice = str(input()) 

        if shape_choice == "1" or shape_choice == "2": 
            while not(mod_choice == "1" or mod_choice == "2" or mod_choice == "3" or mod_choice == "4" or mod_choice == "5"):
                print(f"Choose your modifications:\n" 

                f"\n1- Keep as is" 

                f"\n2- Inverted pyramid" 

                f"\n3- Hollow pyramid" 

                f"\n4- Inverted hollow pyramid" 

                f"\n5- Return to main menu" 

                f"\n") 

                mod_choice = str(input()) 

            if mod_choice == "1" or mod_choice == "2" or mod_choice == "3" or mod_choice == "4": 

                shapes.pyr_maker(shape_choice, mod_choice, symbol, y) #makes pyramids based on modifications 

            else: 

                pattern_choice = "init" 

                mod_choice = str(input()) 

        else: 

            pattern_choice = "init"

 

    elif pattern_choice == "C": #prints diamonds 
        while type(y) != int:
            y = input("\nEnter a height: ")
            if y.isdigit() == True:
                y = int(y)
        while symbol.isalpha() == True:
            symbol = input("Please pick a symbol; !, @, #, $, %, ^, &, *, or numbers: ") 
        while not(shape_choice == "1" or shape_choice == "2" or shape_choice == "3"):
            print(f"Select a diamond type:\n" 

            f"\n1- Half diamond" 

            f"\n2- Full diamond" 

            f"\n3- Return to main menu" 

            f"\n") 

            shape_choice = str(input()) 

        if shape_choice == "1" or shape_choice == "2": 

            print(f"Choose your modifications:\n" 

            f"\n1- Keep as is" 

            f"\n2- Hollow diamond" 

            f"\n3- Return to main menu" 

            f"\n") 

            mod_choice = str(input()) 

            if mod_choice == "1" or mod_choice == "2": 

                shapes.diamond_maker(shape_choice, mod_choice, symbol, y) #makes diamonds based on modifications 

            elif mod_choice == "3": 

                pattern_choice = "init" 

            else: 

                while not(mod_choice == "1" or mod_choice == "2" or mod_choice == "3" or mod_choice == "4" or mod_choice == "5"): 

                    print(f"Try again:\n" 

                    f"\n1- Keep as is" 

                    f"\n2- Inverted diamond" 

                    f"\n3- Hollow diamond" 

                    f"\n4- Inverted hollow diamond" 

                    f"\n5- Return to main menu" 

                    f"\n") 

                mod_choice = str(input()) 

        else: 

            pattern_choice = "init" 

    else: #quits the shop 

        in_shop = False

    while not(exit_shop == "1" or exit_shop == "2"):    #Asks user if they want to leave the shop 

        print(f"\nWould you like to continue doing business?" 

        f"\n1- Yes" 

        f"\n2- No" 

        f"\n") 

        exit_shop = str(input()) 

    if exit_shop == "1": 

        print("\nPlease continue shopping.")

    else: 

        in_shop = False

print("\nThank you for your business.") 