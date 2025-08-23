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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input('You have come to a crucial fork on the island. '
                  'Which direction will you choose?\nType "left" or "right" ').lower()
if direction == "right":
    print("The right step took you over the edge. Game Over.")
else:
    wait = input('This path has brought you to a river. '
                 'Other treasure hunters are on your trail. '
                 '\nWill you take the chance to swim across the strong current or wait for a boat?\n'
                 'Type "swim" or "wait" ').lower()
    if wait == "wait":
        print("The other treasure hunters have captured you. "
              "They have gotten rid of their competition. Game over.")
    else:
        color = input('Swimming has saved you from capture. You have stumbled upon three chests. '
                      'Which one will you choose?\nType "blue", "red" or "yellow" ').lower()
        if color == "red" or "yellow":
            print("You have opened pandora's box. Game over.")
        if color == "blue":
            print("Congratulations! You have found the treasure!")
