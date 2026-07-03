def treasure_island():
    print("\n🏝 Treasure Island Project\n")

    print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____/
*******************************************************************************
''')

    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    choice1 = input(
        'You\'re at a crossroad. Where do you want to go?\n'
        'Type "left" or "right": '
    ).lower()

    if choice1 == "left":

        choice2 = input(
            'You have come to a lake.\n'
            'There is an island in the middle of the lake.\n'
            'Type "wait" to wait for a boat or "swim" to swim across: '
        ).lower()

        if choice2 == "wait":

            choice3 = input(
                "You arrive at the island unharmed.\n"
                "There is a house with three doors.\n"
                "One Red, one Yellow and one Blue.\n"
                "Which colour do you choose? "
            ).lower()

            if choice3 == "red":
                print("\n🔥 It's a room full of fire.\nGame Over!")

            elif choice3 == "yellow":
                print("\n🏆 Congratulations! You found the treasure.\nYou Win!")

            elif choice3 == "blue":
                print("\n🐻 You entered a room full of beasts.\nGame Over!")

            else:
                print("\n🚪 That door doesn't exist.\nGame Over!")

        else:
            print("\n🐊 You were attacked by a crocodile.\nGame Over!")

    else:
        print("\n🕳 You fell into a hole.\nGame Over!")