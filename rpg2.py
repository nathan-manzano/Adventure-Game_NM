import random

#variables
health = 25
enemyHealth = 10
weaponDamage = 0

def showInstructions():

    #main menu
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to Mansion Maze")
    print("Made by: Nathan Manzano")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Instructions:")
    print("'go [direction]'" " USE CARDINAL DIRECTIONS")
    print("'get [item]'")
    print("'equip [item in inventory]'")
    print("'drop [item]'")
    print("'fight [enemy name]'")
    print("YOU CANNOT FIGHT WITHOUT A EQUIPPED WEAPON")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Objective:" " FIND THE EXIT")

def showStatus():

    #print status
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You are at the " + rooms[currentRoom]["name"])
    print("Health:", health)
    #inventory
    print("Inventory : " + str(inventory))
    if len(equipped) > 0:
        print("Equipped: " + str(equipped), "Damage: ", weaponDamage)
    if len(inventory) >= 2:
        print("Your inventory is currently full!")
    #print item
    if "item" in rooms[currentRoom]:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("You see a " + rooms[currentRoom]["item"]  +" in the room.")
    if rooms[currentRoom] == rooms[15]:
        print("I have a strange urge to grab this book...")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #if enemy in the room
    if "enemy" in rooms[currentRoom]:
        print("Enemy Spotted: " + rooms[currentRoom]["enemy"])
        print("Enemy health: ", enemyHealth)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#inventory
inventory = []
equipped = []

#locations
rooms = {
            1 : { "name" : "Dining hall" ,
                  "east" : 2,
                  "south" : 3,
                  "north" : 5,
                  "west" : 12,
                  "item" : "pencil"} ,

            2 : {"name" : "Bedroom" ,
                 "west" : 1,
                 "south" : 4 ,
                 "enemy": "ghost",
                 "item" : "pillow" } ,

            3 : {"name" : "Great Hall" ,
                 "north" : 1 ,
                 "south" : 10,
                 "west" : 11,
                 "enemy" : "goblin"} ,

            4 : {"name" : "Bathroom" ,
                 "north" : 2,
                 "item" : "towel"} ,

            5 : {"name" : "Entry hall" ,
                 "east" : 6,
                 "west" : 13,
                 "south" : 1} ,

            6 : {"name" : "Billiard room" ,
                 "west" : 5,
                 "east" : 14,
                 "item" : "cue",
                 "enemy": "skeleton"} ,

            7 : {"name" : "Grand foyer" ,
                 "north" : 14,
                 "south" : 8,
                 "item": "chain",
                 "enemy": "skeleton",} ,

            8 : {"name" : "Conservatory" ,
                 "north" : 7,
                 "south" : 15,
                 "item" : "trumpet",
                 "enemy" : "chicken",} ,
            
            9 : {"name" : "Gallery" ,
                 "east" : 15,
                 "west" : 10,
                 "enemy": "ghost"} ,

            10 : {"name" : "Janitorial Closet" ,
                  "north" : 3,
                  "east" : 9,
                  "west" : 16,
                  "enemy": "ghost",
                  "item" : "mop"} ,

            11 : {"name" : "Study" ,
                  "east" : 3,
                  "north" : 12,
                  "south" : 16,
                  "item" : "sword"} ,

            12 : {"name" : "Ballroom" ,
                  "east" : 1,
                  "south" : 11,
                  "north" : 13,
                  "enemy": "ghost"} ,

            13 : {"name" : "Lounge" ,
                  "east" : 5,
                  "south" : 12,
                  "item" : "hatchet",
                  "enemy": "skeleton"} ,

            14 : {"name" : "Observatory" ,
                  "west" : 6,
                  "south" : 7,
                  "enemy": "skeleton"} ,

            15 : {"name" : "Library" ,
                  "north" : 8,
                  "west" : 9,
                  "item" : "book"} ,

            16 : {"name" : "Cellar" ,
                  "east" : 10,
                  "north" : 11,} ,
        }

#starting prerequisites
currentRoom = 5
showInstructions()

#start game
while True:
    #if enter is pressed don't end the program
    try:

        showStatus()

        #get input
        move = input(">").lower().split()

        #if go command
        if move[0] == "go":
            #if there is an enemy
            if "enemy" in rooms[currentRoom]:
                print("Can't escape! You must fight!")
            else:
                #if there is a door
                if move[1] in rooms[currentRoom]:
                    #new room
                    currentRoom = rooms[currentRoom][move[1]]
                #if there is no door
                else:
                    print("That is a wall or you mistyped your direction.")

        #if get command
        if move[0] == "get":
            #if item
            if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
                #if inventory if full don't add item
                if len(inventory) >= 2:
                    print("Your inventory is full!")
                #add item
                else:
                    inventory += [move[1]]
                    print(move[1] + " retrieved!")
                    #remove item from room
                    del rooms[currentRoom]["item"]
            #if no item
            else:
                print("Can't get " +move[1]  + "!")

        #if fight command
        if move[0] == "fight":
            #if there is an enemy
            if "enemy" in rooms[currentRoom] and move[1] in rooms[currentRoom]["enemy"]:
                #if you have the equipment to fight
                if "sword" in equipped or "pencil" in equipped or "cue" in equipped or "chain" in equipped or "hatchet" in equipped:
                    enemyAttack = random.randrange(10)
                    enemyHealth -= weaponDamage
                    if enemyHealth <= 0:
                        del rooms[currentRoom]["enemy"]
                        print("You have slain the enemy!")
                        enemyHealth = 10
                    elif health <= 0:
                        print("YOU HAVE DIED")
                        break
                    else:
                        health -= enemyAttack
                        print("You have been damaged but so has your enemy!")
                else:
                    print("YOU DIED DUE TO BEING UNARMED!")
                    break
            else:
                print("No enemies here!")

        #if drop command
        if move[0] == "drop":
            if len(inventory) > 0:
                if move[1] == "sword":
                    inventory.remove("sword")
                    print("'sword' dropped!")
                elif move[1] == "pillow":
                    inventory.remove("pillow")
                    print("'pillow' dropped!")
                elif move[1] == "towel":
                    inventory.remove("towel")
                    print("'towel' dropped!")
                elif move[1] == "cue":
                    inventory.remove("cue")
                    print("'cue' dropped!")
                elif move[1] == "trumpet":
                    inventory.remove("trumpet")
                    print("'trumpet' dropped!")
                elif move[1] == "mop":
                    inventory.remove("mop")
                    print("'mop' dropped!")
                elif move[1] == "pencil":
                    inventory.remove("pencil")
                    print("'pencil' dropped!")
                elif move[1] == "hatchet":
                    inventory.remove("hatchet")
                else:
                    print("Invalid object!")
            else:
                "Nothing to drop."

        #equip item
        if move[0] == "equip":
            if len(inventory) > 0:
                if move[1] == "sword":
                    weaponDamage = 10
                    equipped.clear()
                    equipped += [move[1]]
                    print("'sword' equipped!")
                elif move[1] == "pillow":
                    weaponDamage = 1
                    equipped.clear()
                    equipped += [move[1]]
                    print("'pillow' equipped!")
                elif move[1] == "towel":
                    weaponDamage = 2
                    equipped.clear()
                    equipped += [move[1]]
                    print("'towel' equipped!")
                elif move[1] == "cue":
                    weaponDamage = 6
                    equipped.clear()
                    equipped += [move[1]]
                    print("'cue' equipped!")
                elif move[1] == "trumpet":
                    weaponDamage = 2
                    equipped.clear()
                    equipped += [move[1]]
                    print("'trumpet' equipped!")
                elif move[1] == "mop":
                    weaponDamage = 3
                    equipped.clear()
                    equipped += [move[1]]
                    print("'mop' equipped!")
                elif move[1] == "pencil":
                    weaponDamage = 3
                    equipped.clear()
                    equipped += [move[1]]
                    print("'pencil' equipped!")
                elif move[1] == "hatchet":
                    weaponDamage = 8
                    equipped.clear()
                    equipped += [move[1]]
                    print("'hatchet' equipped!")
            else:
                weaponDamage = 0
                print("Nothing to equip!")

        #Death room
        if rooms[currentRoom] == rooms[16]:
            print("You found the trap room.")
            print("YOU HAVE DIED")
            break

         #Winning room
        if "book" in inventory:
            print("You found the secret passage!")
            print("YOU WIN")
            break

    except:
        pass
