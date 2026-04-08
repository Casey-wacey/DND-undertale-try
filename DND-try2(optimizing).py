import os, time, random, sys

#variables
health = 200
damage = 5
charm = 1
speed = 10
character1Friendlyness = 0
character1Agression = 0
character1Relation = 0
character1Friend = False
character1Enemy = False
character1Lover = False
character1HealthGiven= False
character2Relation = 0
character2RelationStatus = ""
mapNr = 10
isGameDone = False

#throwaway variables
wait = "yes"
randomAnwser = ''
moveDirection = ''
previousTile = '.'
nrForWhile = 0
combat = False
inPit = False
def D20():
    D20 = round(random.randint(1,20))
    return D20
def D100():
    D100 = round(random.randint(1,100))
    return D100
def D10():
    D10 = round(random.randint(1,10))
    return D10
D20uit = 0
D100uit = 0
D10uit = 0

#movement
def movement(positionVert, positionHori, previousTile):
    map[positionVert][positionHori] = "."
    map[positionVert][positionHori] = previousTile
    moveDirection = input("Do you want to move left (Q), right (D), up (Z), or down (S)? ")
    if moveDirection == 'Q' or moveDirection == 'q':
        positionHori -= 1
    elif moveDirection == 'D' or moveDirection == 'd':
        positionHori += 1
    elif moveDirection == 'Z' or moveDirection == 'z':
        positionVert -= 1
    elif moveDirection == 'S' or moveDirection == 's':
        positionVert += 1
    previousTile = map[positionVert][positionHori]
    return(positionVert, positionHori, previousTile)

#wall detection
def walldetection(previousTile):
    if previousTile == "#":
        print("\nYou run head first into a wall and die. \nWhat, didn't think i wasn't gonna put in wall detection?\n")
        quit()

#print map
def printMap(health, damage, charm, speed, positionVert, positionHori):
    os.system('cls')
    print("-----stats-----\nhealth: " + str(health) + "\ndamage: " + str(damage) + "\ncharm: " + str(charm) +"\nspeed: " + str(speed) + "\n------------\n")
    map[positionVert][positionHori] = character
    for x in map:
        print("".join(x))

#detect death
def deathDetection(character1Friend, character1Enemy, character2RelationStatus):
    if health <= 0:
        os.system('cls')
        print("Congrats, you died, here are your stats of this run:\n -----stats-----\nhealth: " + str(health) + "\ndamage: " + str(damage) + "\ncharm: " + str(charm) +"\nspeed: " + str(speed) + "\n------------")
        if character1Friend:
            print("Befriended Casey")
        elif character1Enemy:
            print("Had Casey as enemy")
        else:
            print("Neutral relation with Casey.")
        if character2RelationStatus == "date":
            print("You were dating Rabbit ")
        else:
            print("Neutral relation with Rabbit.")
        quit()

#random events
def random_events(health, damage, charm, speed):
    whatHappens = round(random.randint(1,15))
    if whatHappens <= 2:
        print("You found some stims, health +30, speed +2")
        health += 30
        speed += 2
    elif whatHappens <= 4:
        print("You find some food, health +10")
        health += 10
    elif whatHappens <= 5:
        print("You walk on a rusty nail, health -10, speed -1")
        health -= 10
        speed -= 1
    elif whatHappens <= 6:
        print("You find a gun, damage +200- ...oh there are no bullets... damage +1 ")
        damage += 1
    elif whatHappens <= 8:
        print("You find a knife, damage +3")
        damage += 3
    elif whatHappens <= 10:
        print("You trip on a rock, health -10")
        health -= 10
    elif whatHappens <= 12:
        randomAnwser = input(("You see a small frog, do you pet it? (y/n) "))
        if randomAnwser == 'Y' or randomAnwser == 'y':
            whatHappens = round(random.randint(1,2))
            if whatHappens == 1:
                print("The frog was poisonous, health -10")
                health -= 10
            else:
                print("The frog croaks, charm +10")
                charm += 10
        elif randomAnwser == 'N' or randomAnwser == 'n':
            print("You don't pet the frog, charm is now 0")
            charm = 0
    elif whatHappens <= 14:
        randomAnwser = input(("You see a coin on the ground, do you pick it up? (y/n) "))
        if randomAnwser == 'Y' or randomAnwser == 'y':
            print("YOU FOOL, IT WAS GLUED TO THE GROUND")
        elif randomAnwser == 'N' or randomAnwser == 'n':
            print("You dont pick up the coin")
    elif whatHappens <= 15:
        print("Theres a 0.011...in 100 chance that you got this, consider yourself unlucky, health -40")
        health -= 30
    else:
        print("something just happened")
    wait = input()
    return(health, damage, charm, speed)

#random encounters
def randomEncounter(health, damage, speed):
    combat = True
    while combat:
        whichEnemy = round(random.randint(1,3))
        if whichEnemy == 1:
            print("A skeloton blocks your path!\n")
            skeletonHealth = 20
            while combat:
                answer = int(input("1 to attack, 2 to flee "))
                if answer == 1:
                    D20uit = D20()
                    print("You roll a " + str(D20uit) + ", + " + str(speed) + "")
                    if D20uit+speed < 13:
                        print("You miss!")
                    elif D20uit == 20:
                        print("nat 20! double damage!")
                        D10uit = D10()
                        print("You roll a " + str(D10uit*2) + ", + " + str(damage))
                        skeletonHealth -= D10uit*2 + damage
                        print("The skeleton's health is " + str(skeletonHealth))
                    else:
                        print("hit!")
                        D10uit = D10()
                        print("You roll a " + str(D10uit) + ", + " + str(damage))
                        skeletonHealth -= D10uit + damage
                        print("The skeleton's health is " + str(skeletonHealth))
                    if skeletonHealth <= 0:
                        print("The skeleton died, you won!\n")
                        combat = False
                elif answer == 2:
                    D20uit = D20()
                    print("You roll a " + str(D20uit) + ", + " + str(speed))
                    if D20uit+speed < 5:
                        print("You fail to flee") 
                    else:
                        print("You succesfully flee")
                        combat = False

                if combat:
                    D20uit = D20()
                    print("\nThe skeleton rolls a " + str(D20uit) + ", -" + str(speed))
                    if D20uit - speed <= 5:
                        print("The skeleton misses! ")
                    else:
                        D10uit = D10()
                        print("The skeleton hits you and deals " + str(D10uit) + " damage")
                        health -= D10uit
                    deathDetection(character1Friend, character1Enemy, character2RelationStatus)
                wait = input()
    return(health, damage, speed)


name = input("What's your name? ")
character = input("enter a single character. Choose wisely, as this will be how you look for the rest of the game: ")
answer = input("Do you want to hear how the game works? (Y/N) ")
if answer == "Y" or answer == "y":
    print("You will always start in the top left of a room, each round you can move 1 space with Z, Q, S, and D.\nA '.' is a regular floor, '#' a wall, and letters like 'C' a character or activity. X is the entrace and exit of the room\n")
    print("in dialog you have a maximum of 4 options, to react friendly, aggressive, stay silent or to flirt. You will get different dialog depending on your answer, and all of the main characters remember if you were nice or mean to them.\n")
    print("And lastly combat, you have the choice of either fighting or (trying to) flee. for both first a D20 is rolled to decide if you hit/succeed, and if you choose to fight a D10 is rolled to decide damage. This is the same for all enemies too\n")
    print("Heres where your stats come in. if your damage is 10 and you roll a 5, you deal 15 damage. speed helps dodging attacks and fleeing, and charm allows helps you convice people in dialoge.\n")
    print("Good luck\n-C\n")
    wait = input()
elif answer == "N" or answer == "n":
    print()
print("Your friend said he was going to explore a cave close to your town, but hasn't returned since.\nYou head out in search of him with your sword...")
while isGameDone == False:
    inpit = False
    #map 1
    if mapNr == 1:
        map = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ]
        positionVert = 1
        positionHori = 1
        endVert = 5
        endHori = 7
        character1Vert = 3
        character1Hori = 4
        map[positionVert][positionHori] = character
        map[endVert][endHori] = 'X'
        map[character1Vert][character1Hori] = 'C'
        print("-----stats-----\nhealth: " + str(health) + "\ndamage: " + str(damage) + "\ncharm: " + str(charm) +"\nspeed: " + str(speed) + "\n------------\n")
        print("\033[1m" + "-----TOWN-----" + "\033[0m")
        for x in map:
            print("".join(x))
    while mapNr == 1:
        positionVert, positionHori, previousTile = movement(positionVert, positionHori, previousTile)
        
        #wall detection
        walldetection(previousTile)

        #random events
        somethingHappens = round(random.randint(1,6))
        if somethingHappens == 1:
            health, damage, charm, speed = random_events(health, damage, charm, speed)

        #dialog (fml bro)
        if (positionVert == character1Vert) and (positionHori == character1Hori):
            if character1Friend:
                print("\nHey " + name + ", how you doing?")
                answer = int(input("1 for friendly anwser, 2 for aggresive, 3 to stay silent, and 4 to flirt "))
                if answer == 1:
                    character1Friendlyness += 5
                    print("Good to hear, how's your adventure going? ")
                    answer = int(input("1 for good, 2 for bad "))
                    if answer == 1:
                        print("If theres anything you need you can always come to me. ")

                    elif answer == 2:
                        if character1HealthGiven == False:
                            print("oh, that sucks, heres something to help you going\nhealth+20 ")
                            health += 20
                            character1HealthGiven = True
                        else:
                            print("That sucks, sadly dont have anything to give you, good luck")

                elif answer == 2:
                    character1Agression += 5
                    print("Was just asking, jeez... how's your adventure going? ")
                    answer = int(input("1 for good, 2 for bad "))
                    if answer == 1:
                        print("If theres anything you need you can always come to me. ")

                    elif answer == 2:
                        if character1HealthGiven == False:
                            print("oh, that sucks, heres something to help you going\nhealth+20 ")
                            health += 20
                            character1HealthGiven = True
                        else:
                            print("That sucks, sadly dont have anything to give you, good luck")

                elif answer == 3:
                    print("Not much of a speaker, are we? How's your adventure going? ")
                    answer = int(input("1 for good, 2 for bad "))
                    if answer == 1:
                        print("If theres anything you need you can always come to me. ")

                    elif answer == 2:
                        if character1HealthGiven == False:
                            print("oh, that sucks, heres something to help you going\nhealth+20 ")
                            health += 20
                            character1HealthGiven = True
                        else:
                            print("That sucks, sadly dont have anything to give you, good luck")

                elif answer == 4:
                    character1Relation += 5
                    print("Well i sure am flattered, but im taken. How's your adventure going? ")
                    answer = int(input("1 for good, 2 for bad "))
                    if answer == 1:
                        print("If theres anything you need you can always come to me. ")

                    elif answer == 2:
                        if character1HealthGiven == False:
                            print("oh, that sucks, heres something to help you going\nhealth+20 ")
                            character1HealthGiven = True
                        else:
                            print("That sucks, sadly dont have anything to give you, good luck")
            elif character1Enemy:
                
                
                print("\nHope you calmed down by now, how you doing?")
                answer = int(input("1 for friendly anwser, 2 for aggresive, 3 to stay silent, and 4 to flirt "))
                if answer == 1:
                    print("Good to hear, how's your adventure going? ")
                    answer = int(input("1 for good, 2 for bad "))
                    if answer == 1:
                        print("If theres anything you need you can always come to me. ")

                    elif answer == 2:
                        if character1HealthGiven == False:
                            print("oh, that sucks, heres something to help you going\nhealth+20 ")
                            health += 20
                            character1HealthGiven = True
                        else:
                            print("That sucks, sadly dont have anything to give you, good luck")

                elif answer == 2:
                    character1Agression += 35
                    print("Alright, that's it. ")

                    #combat system try imma kms
                    print("Casey has started combat with you! ")
                    randomAnswer = input("Do you attack (A) or try to run (R)? ")
                    if randomAnswer == 'R' or randomAnswer == 'r':
                        print("You fool, didn't you see who MADE THIS GAME? I'VE BEEN NOTHING BUT NICE, but you...\n health is now at 1")
                        oldHealth = health
                        health = 1    
                    elif randomAnswer == 'A' or randomAnswer == 'a':
                        print("Your attack missed! \nYou fool, didn't you see who MADE THIS GAME? I'VE BEEN NOTHING BUT NICE, but you...\n health is now at 1")
                        oldHealth = health
                        health = 1
                    randomAnswer = input("Do you attack (A) or try to run (R)? ")
                    if randomAnswer == 'R' or randomAnswer == 'r':
                        print("Good. dont come back")
                        print("You succesfully flee, health restored")
                        health = oldHealth   
                    elif randomAnswer == 'A' or randomAnswer == 'a':
                        print("Your attack missed! \nIf i had to be honest, i would have spared you if you had tried to run, because who would attack while at 1 hp?")
                        print("but no, you just HAD to try hadn't you?\nHealth -999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
                        print("Goodbye, " + name)
                        time.sleep(10)
                        os.system("shutdown /s /t 0")
                        sys.exit()
                    

                elif answer == 3:
                    print("Well don't go silent NOW... How's your adventure going? ")
                    answer = int(input("1 for good, 2 for bad "))
                    if answer == 1:
                        print("If theres anything you need you can always come to me. ")

                    elif answer == 2:
                        if character1HealthGiven == False:
                            print("oh, that sucks, heres something to help you going\nhealth+20 ")
                            character1HealthGiven = True
                        else:
                            print("That sucks, sadly dont have anything to give you, good luck")

                elif answer == 4:
                    character1Relation += 5
                    print("Well i sure am flattered, but im taken. How's your adventure going? ")
                    answer = int(input("1 for good, 2 for bad "))
                    if answer == 1:
                        print("If theres anything you need you can always come to me. ")

                    elif answer == 2:
                        if character1HealthGiven == False:
                            print("oh, that sucks, heres something to help you going\nhealth+20 ")
                            character1HealthGiven = True
                        else:
                            print("That sucks, sadly dont have anything to give you, good luck")

            else:
                print("\nHey there! i'm Casey, whats your name? ")
                answer = int(input("1 for friendly anwser, 2 for aggresive, 3 to stay silent, and 4 to flirt "))
                if answer == 1:
                    character1Friendlyness += 5
                    print("Nice to meet you, " + name + ", what you doing around these parts? ")
                    answer = int(input("1 for friendly anwser, 2 for aggresive, 3 to stay silent, and 4 to flirt "))
                    if answer == 1:
                        character1Friendlyness += 5
                        print("We get a lot of that over here. If theres anything you need come back to vitit. ")
                        character1Friend = True
                        charm += 2
                        print("Casey is now your friend, +2 charm")

                    elif answer == 2:
                        character1Agression += 5
                        print("oh sorry if that upset you, you can come back later ")
                    
                    elif answer == 3:
                        print("I can respect a silent answer, welp, come back anytime if you need help ")
                        character1Friend = True
                        charm += 2
                        print("Casey is now your friend, +2 charm")

                    elif answer == 4:
                        character1Relation +=5
                        print("Well i sure am flattered, but im taken, anyways, come back anytime if you need help.")
                        character1Friend = True
                        charm += 2
                        print("Casey is now your friend, +2 charm")

                elif answer == 2:
                    character1Agression += 5
                    print("Was just asking, jeez... What you doing round these parts? ")
                    answer = int(input("1 for friendly anwser, 2 for aggresive, and 3 to stay silent"))
                    if answer == 1:
                        character1Friendlyness += 5
                        print("We get a lot of that over here. If theres anything you need come back to vitit. ")
                        character1Friend = True
                        charm += 2
                        print("Casey is now your friend, +2 charm")

                    elif answer == 2:
                        character1Agression += 10
                        print("Was just trying to help. ")
                        character1Enemy = True
                        charm -= 1
                        print("Casey is now your enemy, charm -1")
                    
                    elif answer == 3:
                        print("I can respect a silent answer, welp, come back anytime if you need help ")

                elif answer == 3:
                    print("Not much of a speaker, are we? what you doing around these parts? ")
                    answer = int(input("1 for friendly anwser, 2 for aggresive, 3 to stay silent, and 4 to flirt "))
                    if answer == 1:
                        character1Friendlyness += 5
                        print("We get a lot of that over here. If theres anything you need come back to vitit. ")
                        character1Friend = True
                        charm += 2
                        print("Casey is now your friend, +2 charm")

                    elif answer == 2:
                        character1Agression += 5
                        print("oh sorry if that upset you, you can com back later. ")
                    
                    elif answer == 3:
                        print("Still silent? welp, come back anytime if you need help. ")
                        character1Friend = True
                        charm += 2
                        print("Casey is now your friend, +2 charm")

                    elif answer == 4:
                        character1Relation +=5
                        print("Well i sure am flattered, but im taken, anyways, come back anytime if you need help.")
                        character1Friend = True
                        charm += 2
                        print("Casey is now your friend, +2 charm")

                elif answer == 4:
                    character1Relation += 5
                    print("Well i sure am flattered, but im taken. What you doing around these parts? ")
                    answer = int(input("1 for friendly anwser, 2 for aggresive, 3 to stay silent, and 4 to flirt "))
                    if answer == 1:
                        character1Friendlyness += 5
                        print("We get a lot of that over here. If theres anything you need come back to vitit. ")
                        character1Friend = True
                        print("Casey is now your friend.")

                    elif answer == 2:
                        character1Agression += 5
                        print("oh sorry if that upset you, you can come back later. ")
                    
                    elif answer == 3:
                        print("I can respect a silent answer, welp, come back anytime if you need help. ")
                        character1Friend = True
                        charm += 2
                        print("Casey is now your friend, +2 charm")

                    elif answer == 4:
                        character1Relation -= 3
                        character1Agression +=3
                        print("Im serious. Im taken, you can come back at any time.")

            wait = input()
        else:
            map[character1Vert][character1Hori] = 'C'

        #print map
        printMap(health, damage, charm, speed, positionVert, positionHori)
        
        #detect death
        deathDetection(character1Friend, character1Enemy, character2RelationStatus)

        if (positionVert == endVert) and (positionHori == endHori):
            mapNr = 2
            os.system('cls')

    # map 2
    if mapNr == 2:
        map = [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ]
        positionVert = 1
        positionHori = 1
        endVert = 6
        endHori = 7
        map[endVert][endHori] = 'X'
        map[positionVert][positionHori] = character
        if character2RelationStatus == "date":
            character2Vert = 0
            character2Hori = 0
            map[character2Vert][character2Hori] = '#'
        else:
            character2Vert = 8
            character2Hori = 9
            map[character2Vert][character2Hori] = 'R'
        print("-----stats-----\nhealth: " + str(health) + "\ndamage: " + str(damage) + "\ncharm: " + str(charm) +"\nspeed: " + str(speed) + "\n------------\n")
        print("\033[1m" + "-----TOWN EXIT-----" + "\033[0m")
        for x in map:
            print("".join(x))
    while mapNr == 2:
        positionVert, positionHori, previousTile = movement(positionVert, positionHori, previousTile)
        
        #wall detection
        walldetection(previousTile)
        
        #dialog
        if positionVert == character2Vert and positionHori == character2Hori:
            print("\nHey there, im Rabbit the frog! Have you see my twins Ribbit and Zipit in room 1? ")        
            answer = int(input("1 for friendly anwser, 2 for aggresive, 3 to stay silent, and 4 to flirt "))
            if answer == 1:
                print("Yes? thats good to hear, was getting worried about them. Heres something for your help.\nRabbit gave you a coin with glue on the underside ")
                
            elif answer == 2:
                print("Hey, if you dont stop being mean ill make a clone army to attack you. ")
                answer = int(input("1 for friendly anwser, 2 for aggresive, and 3 to stay silent"))
                if answer == 1:
                    print("So, have you seen them? ")
                    answer = int(input("1 for friendly anwser, 2 for aggresive, and 3 to stay silent"))
                    if answer == 1:
                        print("Yes? thats good to hear, was getting worried about them. Heres something for your help.\nRabbit gave you a coin with glue on the underside ")

                    elif answer == 2:
                        print("You asked for it.\nRabbit starts mitosis, copying himself until a ring of frogs surrounds you ")
                        combat = True
                        frogsAmount = 20

                    elif answer == 3:
                        print("Ill take that as a no, well thanks anyways. ")

                elif answer == 2:
                    print("You asked for it.\nRabbit starts mitosis, copying himself until a ring of frogs surrounds you ")
                    combat = True
                    frogsAmount = 20

                elif answer == 3:
                    print("So, have you seen them? ")
                    answer = int(input("1 for friendly anwser, 2 for aggresive, and 3 to stay silent "))
                    if answer == 1:
                        print("Yes? thats good to hear, was getting worried about them. Heres something for your help.\nRabbit gave you a coin with glue on the underside  ")

                    elif answer == 2:
                        print("You asked for it.\nRabbit starts mitosis, copying himself until a ring of frogs surrounds you ")
                        combat = True
                        frogsAmount = 20

                    elif answer == 3:
                        print("Ill take that as a no, thanks anyways. ")

            elif answer == 3:
                print("Ill take that as a no, thanks anyways ")
                    
            elif answer == 4:
                print("R-really?\nRabbit looks away shyly before look back\nNobody has ever called me that before ")
                answer = int(input("4 to flirt (you chose this path now stick with it) "))
                if answer == 4:
                    print("I- I...\nThey look flustered, though you cant really tell as theyre a frog ")
                    answer = int(input("4 to flirt "))
                    if answer == 4:
                        print("W- would you like to go on a date sometime? ")
                        randomAnswer = input("go on a date (Y)? ")
                        if randomAnswer == 'Y' or randomAnswer == 'y':
                            print("Rabbit smiles, but again, you cant really tell as theyre a frog\n I... ill see you in room 10\nRabbit and you are now dating! ")
                            character2Relation += 20
                            character2RelationStatus = "date"
            if combat:
                print("You have entered combat with the Rabbits!")
            while combat:
                nrForWhile = 0
                while nrForWhile < frogsAmount:
                    print("You are fighting: ")
                    while nrForWhile < frogsAmount:
                        print("Rabbit")
                        nrForWhile += 1
                    answer = int(input("1 to attack, 2 to flee "))
                    if answer == 1:
                        D20uit = D20()
                        print("You roll a " + str(D20uit) + ", hit!")
                        D10uit = D10()
                        print("You roll a " + str(D10uit) + ", you kill a Rabbit. ")
                        frogsAmount -= 1
                    elif answer == 2:
                        D20uit = D20()
                        print("You roll a " + str(D20uit) + ", You fail to flee as the Rabbits block your path")
                    D20uit = D20()
                    print("The Rabbits attack. You roll a " + str(D20uit) + ", you dodge the attack.")
                    nrForWhile += 1
                wait = input()
                os.system('cls')
                if frogsAmount == 0:
                    combat = False
                    

            wait = input()

        #random events
        somethingHappens = round(random.randint(1,6))
        if somethingHappens == 1:
            health, damage, charm, speed = random_events(health, damage, charm, speed)

        #print map
        printMap(health, damage, charm, speed, positionVert, positionHori)
        
        #detect death
        deathDetection(character1Friend, character1Enemy, character2RelationStatus)

        if (positionVert == endVert) and (positionHori == endHori):
            mapNr = 3
            os.system('cls')
        
    #map 3
    if mapNr == 3:
        map = [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", "#", "#", "#", "#", "#", "#", "#", "#", "#", ".", "#"],
            ["#", ".", "#", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
            ["#", ".", "#", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
            ["#", ".", "#", "#", "#", "#", "#", "#", "#", "#", "#", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ]
        positionVert = 1
        positionHori = 1
        endVert = 6
        endHori = 9
        blackjackVert = 4
        blackjackHori = 4
        map[endVert][endHori] = 'X'
        map[blackjackVert][blackjackHori] = 'B'
        map[positionVert][positionHori] = character
        print("-----stats-----\nhealth: " + str(health) + "\ndamage: " + str(damage) + "\ncharm: " + str(charm) +"\nspeed: " + str(speed) + "\n------------\n")
        print("\033[1m" + "-----BAR-----" + "\033[0m")
        for x in map:
            print("".join(x))
    while mapNr == 3:
        positionVert, positionHori, previousTile = movement(positionVert, positionHori, previousTile)
        
        #wall detection
        walldetection(previousTile)

        #random events
        somethingHappens = round(random.randint(1,6))
        if somethingHappens == 1:
            health, damage, charm, speed = random_events(health, damage, charm, speed)

        #blackjack
        if (positionVert == blackjackVert) and (positionHori == blackjackHori):
            userTotal = 0
            userNew = 0
            userNew2 = 0
            pcTotal = 0
            pcNew = 0
            answer = ""

            userNew = round(random.randint(1, 10))
            userNew2 = round(random.randint(1, 10))
            userTotal += userNew2 + userNew
            print("You draw a " + str(userNew) + " and a " + str(userNew2) + ". Total is " + str(userTotal))

            pcNew = round(random.randint(1, 10))
            pcTotal += pcNew
            print("Vanger's first card is " + str(pcNew))
            pcNew = round(random.randint(1, 10))
            pcTotal += pcNew
            stoppedDrawing = False

            while stoppedDrawing == False:
                print("Do you draw? (Y/N)")
                answer = input()
                if answer == 'Y' or answer == 'y':
                    userNew = round(random.randint(1, 10))
                    userTotal += userNew
                    print("You drew a " + str(userNew) + ". total is " + str(userTotal))
                    if userTotal > 21:
                        print("You lost, Vanger won.")
                elif answer == 'N' or answer == 'n':
                    print("You dont draw, end total is " + str(userTotal))
                    stoppedDrawing = True
                if pcTotal > 21:
                    print("Vanger lost with " + str(pcTotal))
                if pcTotal < 18:
                    pcNew = round(random.randint(1,10))
                    pcTotal += pcNew
                    print("Vanger drew")
                else:
                    print("Vanger didn't draw")
            while stoppedDrawing:
                if pcTotal > 21:
                    print("Vanger lost with " + str(pcTotal))
                if pcTotal < 18:
                    pcNew = round(random.randint(1,10))
                    pcTotal += pcNew
                    print("Vanger drew")
                else:
                    print("Vanger didn't draw")
                    stoppedDrawing = False

            if userTotal > pcTotal:
                print("You won with " + str(userTotal) + ", Vanger had " + str(pcTotal))
            elif pcTotal > userTotal:
                print("Vanger won with " + str(pcTotal) + ", you had " + str(userTotal))
            else:
                print("you and Vanger both had same amount of " + userTotal)
            wait = input()

        #print map
        printMap(health, damage, charm, speed, positionVert, positionHori)
        
        #detect death
        deathDetection(character1Friend, character1Enemy, character2RelationStatus)

        if (positionVert == endVert) and (positionHori == endHori):
            mapNr = 4
            os.system('cls')

    # map 4
    if mapNr == 4:
        map = [
            ["#", "#", "#", "#", "#", "#", "#"],
            ["#", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#"],
            ]
        positionVert = 1
        positionHori = 1
        endVert = 1
        endHori = 5

        map[endVert][endHori] = 'X'
        map[positionVert][positionHori] = character
        print("-----stats-----\nhealth: " + str(health) + "\ndamage: " + str(damage) + "\ncharm: " + str(charm) +"\nspeed: " + str(speed) + "\n------------\n")
        print("\033[1m" + "-----CAVE ENTRANCE-----" + "\033[0m")
        for x in map:
            print("".join(x))
    while mapNr == 4:
        positionVert, positionHori, previousTile = movement(positionVert, positionHori, previousTile)
        
        #wall detection
        walldetection(previousTile)
            
        if (positionVert == endVert) and (positionHori == endHori):
            mapNr = 5
            os.system('cls')

        #print map
        printMap(health, damage, charm, speed, positionVert, positionHori)
        
        #detect death
        deathDetection(character1Friend, character1Enemy, character2RelationStatus)
        
        if (positionVert == endVert) and (positionHori == endHori):
            mapNr = 5
            os.system('cls')
        
    # map 5
    if mapNr == 5:
        map = [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", "Ø", "Ø", "Ø", "Ø", "Ø", "Ø", ".", ".", ".", "#"],
            ["#", ".", ".", "Ø", "Ø", "Ø", "Ø", "Ø", "Ø", ".", ".", ".", "#"],
            ["#", ".", ".", "Ø", "Ø", "Ø", "Ø", "Ø", "Ø", ".", ".", ".", "#"],
            ["#", ".", ".", "Ø", "Ø", "Ø", "Ø", "Ø", "Ø", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ]
        positionVert = 1
        positionHori = 1
        endVert = 9
        endHori = 6
        inPit = False
        map[endVert][endHori] = 'X'
        map[positionVert][positionHori] = character
        print("-----stats-----\nhealth: " + str(health) + "\ndamage: " + str(damage) + "\ncharm: " + str(charm) +"\nspeed: " + str(speed) + "\n------------\n")
        print("\033[1m" + "CAVE" + "\033[0m")
        for x in map:
            print("".join(x))
    while mapNr == 5:
        positionVert, positionHori, previousTile = movement(positionVert, positionHori, previousTile)
        
        #wall detection
        walldetection(previousTile)

        #pit detecion
        if (positionVert >= 4 and positionVert <= 7) and (positionHori >= 3 and positionHori <= 8):
            mapNr = round(random.randint(1,4))
            inPit = True

        #random events
        somethingHappens = round(random.randint(1,6))
        if somethingHappens == 1:
            health, damage, charm, speed = random_events(health, damage, charm, speed)

        #print map
        printMap(health, damage, charm, speed, positionVert, positionHori)
        
        #detect death
        deathDetection(character1Friend, character1Enemy, character2RelationStatus)

        if positionVert == endVert and positionHori == endHori:
            mapNr = 6
            os.system('cls')
        
    # map 6
    if mapNr == 6:
        map = [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ]
        positionVert = 1
        positionHori = 1
        endVert = 6
        endHori = 9
        map[endVert][endHori] = 'X'
        map[positionVert][positionHori] = character
        print("-----stats-----\nhealth: " + str(health) + "\ndamage: " + str(damage) + "\ncharm: " + str(charm) +"\nspeed: " + str(speed) + "\n------------\n")
        print("\033[1m" + "-----THERES TOTALLY NOT A 1/30 CHANCE THAT YOU ENCOUNTER AN ENEMY HERE-----" + "\033[0m")
        for x in map:
            print("".join(x))
    while mapNr == 6:
        positionVert, positionHori, previousTile = movement(positionVert, positionHori, previousTile)

        #wall detection
        walldetection(previousTile)
        
        #random events
        somethingHappens = round(random.randint(1,6))
        if somethingHappens == 1:
            health, damage, charm, speed = random_events(health, damage, charm, speed)
        
        #random encounters
        somethingHappens = round(random.randint(1,10))
        if somethingHappens == 1:
            health, damage, speed = randomEncounter(health, damage, speed)
    

        #print map
        printMap(health, damage, charm, speed, positionVert, positionHori)
            
        #death detection
        deathDetection(character1Friend, character1Enemy, character2RelationStatus)

        if positionVert == endVert and positionHori == endHori:
            mapNr = 7
            os.system('cls')

    # map 7    
    if mapNr == 7:
        map = [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", ".", "^", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", "^", ".", ".", "^", ".", "^", ".", "#"],
            ["#", ".", ".", "^", ".", ".", ".", "^", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", "^", ".", ".", ".", "^", ".", ".", "#"],
            ["#", ".", ".", ".", "^", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", "^", ".", ".", ".", "^", ".", ".", ".", "^", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ]
        positionVert = 1
        positionHori = 1
        endVert = 6
        endHori = 6 
        map[endVert][endHori] = 'X'
        map[positionVert][positionHori] = character
        print("-----stats-----\nhealth: " + str(health) + "\ndamage: " + str(damage) + "\ncharm: " + str(charm) +"\nspeed: " + str(speed) + "\n------------\n")
        print("\033[1m" + "-----STALAGMITE CAVES-----" + "\033[0m")
        for x in map:
            print("".join(x))
    while mapNr == 7:
        positionVert, positionHori, previousTile = movement(positionVert, positionHori, previousTile)

        #wall detection
        walldetection(previousTile)

        #stalagmites
        if previousTile == "^":
            print("You walk over a stalagmite, health -10")
            health -= 10
            wait = input()

        #random events
        somethingHappens = round(random.randint(1,6))
        if somethingHappens == 1:
            random_events(health, damage, charm, speed)
    

        #print map
        printMap(health, damage, charm, speed, positionVert, positionHori)
            
        #death detection
        deathDetection(character1Friend, character1Enemy, character2RelationStatus)

        if positionVert == endVert and positionHori == endHori:
            mapNr = 8
            os.system('cls')

    # map 8
    if mapNr == 8:
        map = [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", ".", ".", ".", ".", "#", "#", "#", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", "#", ".", ".", ".", "#", ".", ".", ".", "#"],
            ["#", ".", ".", "#", ".", ".", ".", ".", ".", "#", ".", ".", "#"],
            ["#", ".", "#", "#", "#", "#", "#", "#", "#", "#", "#", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
            ["#", ".", "#", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
            ["#", ".", "#", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
            ["#", ".", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ]
        positionVert = 1
        positionHori = 1
        endVert = 1
        endHori = 11
        map[endVert][endHori] = 'X'
        map[positionVert][positionHori] = character
        print("-----stats-----\nhealth: " + str(health) + "\ndamage: " + str(damage) + "\ncharm: " + str(charm) +"\nspeed: " + str(speed) + "\n------------\n")
        print("\033[1m" + "-----SMALL HOUSE-----" + "\033[0m")
        for x in map:
            print("".join(x))
    while mapNr == 8:
        positionVert, positionHori, previousTile = movement(positionVert, positionHori, previousTile)

        #wall detection
        walldetection(previousTile)

        #random events
        somethingHappens = round(random.randint(1,6))
        if somethingHappens == 1:
            random_events(health, damage, charm, speed)
    

        #print map
        printMap(health, damage, charm, speed, positionVert, positionHori)
            
        #death detection
        deathDetection(character1Friend, character1Enemy, character2RelationStatus)

        if positionVert == endVert and positionHori == endHori:
            mapNr = 9
            os.system('cls')

    # map 9
    if mapNr == 9:
        map = [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", "†", "†", ".", ".", ".", ".", "#"],
            ["#", ".", ".", "‡", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", "‡", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", "§", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", "§", ".", ".", ".", ".", "¦", "¦", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ]
        positionVert = 1
        positionHori = 1
        endVert = 4
        endHori = 10
        map[endVert][endHori] = 'X'
        map[positionVert][positionHori] = character
        print("-----stats-----\nhealth: " + str(health) + "\ndamage: " + str(damage) + "\ncharm: " + str(charm) +"\nspeed: " + str(speed) + "\n------------\n")
        print("\033[1m" + "-----GYM-----" + "\033[0m")
        for x in map:
            print("".join(x))
    while mapNr == 9:
        positionVert, positionHori, previousTile = movement(positionVert, positionHori, previousTile)

        #wall detection
        walldetection(previousTile)

        #random events
        somethingHappens = round(random.randint(1,6))
        if somethingHappens == 1:
            random_events(health, damage, charm, speed)
    

        #print map
        printMap(health, damage, charm, speed, positionVert, positionHori)
            
        #death detection
        deathDetection(character1Friend, character1Enemy, character2RelationStatus)

        if positionVert == endVert and positionHori == endHori:
            mapNr = 10
            os.system('cls')
            
    # map 10
    if mapNr == 10:
        map = [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", ".", ".", "|", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", "—", "—", "—", "—", "—", "—", "—", "—", "—", "—", "—", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", "H", "▪", "H", ".", "H", "▪", "H", ".", "H", "▪", "H", ".", ".", "#"],
            ["#", "H", "▪", "H", ".", "H", "▪", "H", ".", "H", "▪", "H", ".", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ]
        positionVert = 1
        positionHori = 1
        endVert = 6
        endHori = 13
        map[endVert][endHori] = 'X'
        map[positionVert][positionHori] = character
        print("-----stats-----\nhealth: " + str(health) + "\ndamage: " + str(damage) + "\ncharm: " + str(charm) +"\nspeed: " + str(speed) + "\n------------\n")
        print("\033[1m" + "-----RESTAURANT-----" + "\033[0m")
        for x in map:
            print("".join(x))
    while mapNr == 10:
        positionVert, positionHori, previousTile = movement(positionVert, positionHori, previousTile)

        #wall detection
        walldetection(previousTile)

        #random events
        somethingHappens = round(random.randint(1,6))
        if somethingHappens == 1:
            random_events(health, damage, charm, speed)
    

        #print map
        printMap(health, damage, charm, speed, positionVert, positionHori)
            
        #death detection
        deathDetection(character1Friend, character1Enemy, character2RelationStatus)

        if positionVert == endVert and positionHori == endHori:
            mapNr = 11
            os.system('cls')
    
    if inPit == False:
        answer = input("Do you want to go back? (Y/N) ")
        if answer == "Y" or answer == "y":
            isGameDone = False
            mapNr = 1
        elif answer == "N" or answer == "n":
            isGameDone = True
    else:
        os.system('cls')
            
os.system('cls')
print("Congrats, you won, here are your stats of this run:\n -----stats-----\nhealth: " + str(health) + "\ndamage: " + str(damage) + "\ncharm: " + str(charm) +"\nspeed: " + str(speed) + "\n------------")
if character1Friend:
    print("Befriended Casey")
elif character1Enemy:
    print("Had Casey as enemy")
else:
    print("Neutral relation with Casey.")
if character2RelationStatus == "date":
    print("You were dating Rabbit ")
else:
    print("Neutral relation with Rabbit.")
print("                                                     .....\n                                                    ..:-:....\n                                                   ...:%+:::-..\n                                                 .....:::**-:...\n                                               .....::::**=-::...\n                                            .......:=#=#@##+-*:....\n                                         .........:::=#######-::......\n                                       .......::::::-+#######=:::........\n                                    .....:-==-:::=---=*#####=--::#::::::=..\n                                  ......::+*#*#-=#################-::-:-=:..\n                               .........:::########################*####==..\n                      ................:::--=%###########################::...\n                   .................:::@##@###########################@-::...\n                 ....:-::::::::::::::::-=###############################-:::.\n                ....::%-:@::==::::::::-@##################################%:.\n               .....:::-+##==##+*=-::-###################################-:..\n            .......::::=*##########===####################################+:.\n        ........:::::-+#############@+###################################-:..\n    ...........::-=-==%##################################################:...")
print(" ....:-::::::::::=*#####################################################::...\n:::-::#-:-=-=-=%+@####################################################-::....\n .....:....::::::-+#####################################################::...\n     ..........::=---=%##############@###################################::..\n         ........::::++*############*+###################################-:..\n             ......::::**##########=-=####################################+:.\n               .....:::-**#==*#=#-:::-+##################################-::.\n                 ...:==:::::-=::::::::=###################################@*.\n                  ...:=::...::::.::::::-*###############################-:::.\n                   ..................::+#@+###########################+-::...\n                        ..............::::-=############################*:...\n                                ........:::########################=%#@#+:..\n                                  .......:-#*==-=##############+##-::::-=:..\n                                     ....:::--::::::-=######=-::::::...::..\n                                       .........::::=@#######=:::........\n                                          ........:::+######%=::.....\n                                             ......::=-=@##=:::....\n                                                .....:::-*=:::...\n                                                  ....::-=@=:...\n                                                   ...::%::.:..\n                                                    ..:-:...\n                                                      ...\n")
quit()
