import random

#variables
health = 25

def showInstructions():

    #main menu
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to Mansion Maze")
    print("Made by: Nathan Manzano")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Instructions:")
    print("'go [direction]'" " USE CARDINAL DIRECTIONS")
    print("'get [item]'")
    print("'fight [enemy name]'")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Objective:" "FIND THE EXIT")


def showStatus():

    #print status
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You are at the " + rooms[currentRoom]["name"])
    print("Health:", health)

    #inventory
    print("Inventory : " + str(inventory))

    #print item
    if "item" in rooms[currentRoom]:
        print("You see a " + rooms[currentRoom]["item"]  +" in the room.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #if enemy in the room
    if "enemy" in rooms[currentRoom]:
        print("Enemy Spotted: " + rooms[currentRoom]["enemy"])
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#inventory
inventory = []

#locations
rooms = {

            1 : { "name" : "Dining hall" ,
                  "east" : 2,
                  "south" : 3,
                  "north" : 5,
                  "west" : 12,
                  "item" : "sword"} ,

            2 : {"name" : "Bedroom" ,
                 "west" : 1,
                 "south" : 4 ,
                 "item" : "pillow",
                 "enemy": "ghost"} ,

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

            10 : {"name" : "Library" ,
                  "north" : 3,
                  "east" : 9,
                  "west" : 16,
                  "enemy": "ghost"} ,

            11 : {"name" : "Study" ,
                  "east" : 3,
                  "north" : 12,
                  "south" : 16,
                  "item" : "pencil"} ,

            12 : {"name" : "Ballroom" ,
                  "east" : 1,
                  "south" : 11,
                  "north" : 13,
                  "enemy": "ghost"} ,

            13 : {"name" : "Lounge" ,
                  "east" : 5,
                  "south" : 12,
                  "enemy": "skeleton"} ,

            14 : {"name" : "Observatory" ,
                  "west" : 6,
                  "south" : 7,
                  "enemy": "skeleton"} ,

            15 : {"name" : "Janitorial Closet" ,
                  "north" : 8,
                  "west" : 9,
                  "item" : "mop"} ,

            16 : {"name" : "Cellar" ,
                  "east" : 10,
                  "north" : 11,} ,

        }

#starting prerequisites
currentRoom = 5
showInstructions()

#start game
while True:
    showStatus()

    #get input
    move = input(">").lower().split()

    #if get command
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
                print("That is a wall.")

    #if get command
    if move[0] == "get":
        #if item
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
            #add to inventory
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
            if "sword" in inventory or "pencil" in inventory or "cue" in inventory or "chain" in inventory:
                enemyAttack = random.randrange(10)

                if enemyAttack >= 5:
                    health -= enemyAttack

                    if health == 0:
                        print("YOU HAVE DIED")
                        break

                    else:
                        print("You have been damaged but so has your enemy!")

                else:
                    del rooms[currentRoom]["enemy"]
                    print("You have slain the enemy!")
                    health += 3
                    print("You healed a small amount!")

            else:
                print("YOU DIED DUE TO BEING UNARMED!")
                break

        else:
            print("No enemies here!")

    #Death room
    if rooms[currentRoom] == rooms[16]:
        print("You found the trap room.")
        print("YOU HAVE DIED")
        break

     #Winning room
    if rooms[currentRoom] == rooms[15]:
        
        if "mop" in inventory:
            print("You've Escaped!")
            print("YOU WIN")
            break