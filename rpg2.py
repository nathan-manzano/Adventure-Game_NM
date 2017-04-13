import random

#variables
health = 10

def showInstructions():
    #main menu
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("Medieval RPG")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("Commands:")
    print("'go [direction]'")
    print("use cardinal directions!")
    print("'get [item]'")
    print("'fight'")


def showStatus():
    #print status
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You are at the " + rooms[currentRoom]["name"])

    #inventory
    print("Inventory : " + str(inventory))
    #print item
    if "item" in rooms[currentRoom]:
        print("You found a " + rooms[currentRoom]["item"])
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #if enemy in the room
    if "enemy" in rooms[currentRoom]:
        print("Enemy Spotted: " + rooms[currentRoom]["enemy"])

#inventory
inventory = []

#locations
rooms = {

            1 : { "name" : "Dining hall" ,
                  "east" : 2,
                  "south" : 3,
                  "north" : 5,
                  "west" : 12} ,

            2 : {"name" : "Bedroom" ,
                 "west" : 1,
                 "south" : 4 ,
                 "item" : "pillow" } ,

            3 : {"name" : "Great Hall" ,
                 "north" : 1 ,
                 "south" : 10,
                 "west" : 11,
                 "item" : "sword",
                 "enemy" : "monster"} ,

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
                 "item" : "Cue stick"} ,

            7 : {"name" : "Grand foyer" ,
                 "north" : 14,
                 "south" : 8} ,

            8 : {"name" : "Conservatory" ,
                 "north" : 7,
                 "south" : 15,
                 "item" : "Trumpet"} ,
            
            9 : {"name" : "Gallery" ,
                 "east" : 15,
                 "west" : 10} ,

            10 : {"name" : "Library" ,
                  "north" : 3,
                  "east" : 9,
                  "west" : 16} ,

            11 : {"name" : "Study" ,
                  "east" : 3,
                  "north" : 12,
                  "south" : 16,
                  "item" : "Pencil"} ,

            12 : {"name" : "Ballroom" ,
                  "east" : 1,
                  "south" : 11,
                  "north" : 13} ,

            13 : {"name" : "Lounge" ,
                  "east" : 5,
                  "south" : 12} ,

            14 : {"name" : "Observatory" ,
                  "west" : 6,
                  "south" : 7} ,

            15 : {"name" : "Janitorial Closet" ,
                  "north" : 8,
                  "west" : 9,
                  "item" : "Mop"} ,

            16 : {"name" : "Cellar" ,
                  "east" : 10,
                  "north" : 11,
                  "item" : "Chain"} ,

        }

#starting room
currentRoom = 5
showInstructions()

#start game
while True:
    showStatus()

    #get input
    move = input(">").lower().split()

    #if go
    if move[0] == "go":
        #if door
        if move[1] in rooms[currentRoom]:
            #new room
            currentRoom = rooms[currentRoom][move[1]]
        #if no door
        else:
            print("Can't go this way.")

    #if get
    if move[0] == "get":
        #if item
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
            #add to inventory
            inventory += [move[1]]
            print(move[1] + " got!")
            #remove item from room
            del rooms[currentRoom]["item"]
        #if no item
        else:
            print("Can't get " +move[1]  + "!")
    
    if move[0] == "fight":
        if "sword" in inventory:
            enemyAttack = random.random()
            enemyHit = random.randrange(4)
            if enemyAttack > 5:
                health -= enemyHit
                del rooms[currentRoom]["enemy"]
                print("You've slain the enemy but took damage!")
                if health == 0:
                    print("YOu have been slain")
                    break

                else:
                    del rooms[currentRoom]["enemy"]
                    print("You have slain the enemy")
        else:
            print("You died defensiveless!")
            break

                          
