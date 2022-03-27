#Ryne Bigueras
#CSS225 Milestone Game

import random



def Chapter1():
    print('Chapter 1: Waking up')
    print("Miria wakes up")
    print("in an unknown forest")
    print("she feels danger slowly creeping")
    print("What to do?")
    action = input("sneak or fight? ")

    if (action == "sneak"):
        print("Sneak Away healthy: AGI and DEX Increased. Go to next Chapter.")
        Chapter2()
    else:
        print("Miria draws her weapon")
        dice = random.randint(1,6)
        print("You roll for attack. 3 or lower is a failure: Rolled...", dice)
    if dice in range(1,3+1):
        print("You are injured: STR and CON Increased. Go to next Chapter.")
        Chapter2()
    else:
        print("No damage and healthy: STR and CON Increased. Go to next Chapter.")
        Chapter2()

   

def Chapter2():

    print('Chapter 2: Kamura Village')
    action = input("injured or healthy? ")


    if (action == "injured"):
        print("Pass Out in front of town gates.")
        print("Go to straight to Chapter 4.")
    
        Chapter4()

    else:
        print("Miria walks to local bar")
        print("Start asking questions with locals")
        print("But the questions start to annoy patrons.")

    action2 = input("fight or sneak? ")

    if action2 == "sneak":
        dice = random.randint(1,6)
        print("Try to Slip away and avoid a fight. 2 or lower is a failure: Rolled...", dice)
        if dice in range(1, 2+1):
            print("Failed: Miria gets caught and beaten")
            print("Go to Chapter 4")
            Chapter4()

        else:
            print("Miria get away with no injury")
            print("Go to Chapter 3")
            Chapter3()

    else:
        print("Miria raises her fists in a fighting stance")
        dice = random.randint(1,6)
        print("Miria rolls to start punching. 2 or lower is a failure: Rolled...", dice)
        
        if dice in range(1,2+1):
            print("Miria is injured in the fight and Passes out")
            print("Go to Chapter 4.")
            Chapter4()
        else:
            print("Wins the fight and takes no damage.")
            print("Go to next Chapter.")

            Chapter3()



def Chapter3():
    print('Chapter 3: Village Attacked')

    print("Miria walks away from the bar.")
    print("She hears growls, howls and screams coming to her.")
    print("Miria is forced to fight")

    action = input("stab or strike? ")
    print(action)

    if (action == "stab"):
        dice = random.randint(1,6)
        print("Miria backstabs. 2 or lower is a failure: Rolled...", dice)
        if dice in range(1, 2+1):
                print("Missed and got hurt: Pass out due to injury.")
                print("Monsters defeated by guards")
                print("Go to next Chapter.")
                Chapter4()
        else:
                print("Successfully kill monsters")
                print("Pass out due to exhaustion")
                print("Go to next Chapter.")
                Chapter4()
    

        
    else:
        print("Miria draws sword.")
        dice = random.randint(1,6)
        print("Miria swings towards monsters. 2 or lower is a failure: Rolled...",dice)
        if dice in range(1, 2+1):
            print("Miria misses and is injured.")
            print("she passes out because of injury.")
            print("Town guards dispatches monsters")
            print("Go to next Chapter.")
            Chapter4()
        else:
            print("Successfully smite monsters down")
            print("Miria got tired and passed out")
            print("Go to next Chapter.")
            Chapter4()


def Chapter4():

    print('Chapter 4: Waking up again')
 

    print("Miria wakes up in a bed.")
    print("She is tended by a child.")

    action = input("injured or exhausted? ")


    if (action == "injured"):
        print("Miria wakes up with only has half life.")
        print("Miria must pay for room: 30 Gold a day")
        print("She needs to make money through adventures")
        print("Go to next Chapter.")
        Chapter5()

        
    else:
        print("Miria is praised by the town")
        print("She has killed the monsters before passing out.")
        print("Miria stays in home for free.")
        print("She stays in bed and recoup energy.")
        print("She goes to guild for adventuring with full life")
        print("Go to next Chapter.")
        Chapter5()



#CH 5
def Chapter5():
    print("Chapter 5: Adventure")
    print("Miria walks to guild hall.")
    print("Miria has to choose quests")


    action3 = input("How much life you have? full or half? ")


    if (action3 == "full"):
        action4 = input("hunt or gather? ")
        if (action4 == "hunt"):
            dice = random.randint(1,6)
            print("Slay monsters. 2 or lower is a failure: Rolled...", dice)
            if dice in range(1,2+1):
                print("Miria Fails the Hunt injured to half life")
                print("Turn in Quest: No reward.")

                Chapter5()
                    
            else:
                print("Successfully Hunt Monsters")
                print("Turn in Quest")
                print("Earn 50 Gold.")
                print("Earn 100 Exp.")
                Chapter5()
        else:
            print("Miria finds herbs in the near forest")
            print("Can't fail: Turn in quest")
            print("Earn 10 exp and 5 Gold")
            print("Quest again")
            Chapter5()
            
    else:
        print("Beacuse of injury")
        print("Gathering is only option")
        print("Can't fail: Turn in quest.")
        print("Earn little exp and money. Regain Health to full")
    
        Chapter5()

Chapter1()
