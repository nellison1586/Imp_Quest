import random

RAT_STATS = ("Rat",3,4,3,5,3)                   #Tuples containing all the info for the enemies, first slot is their name, 2nd is Strength value, 3rd is Dex, 4th is Mind, 5th is Speed, and 6th is gold amount when defeated
SLIME_STATS = ("Slime",2,2,2,2,1)
BAT_STATS = ("Bat",4,4,4,9,3)
TROLL_STATS = ("Troll",8,5,5,3,7)
WOLF_STATS = ("Wolf",5,5,4,7,5)


def m_stats(stats_mstats: list, index: int, amount: int):       #Modifies a specific value in a provided Stat list by a specified amount, used to change/add/lose health, stats, gold, items etc.
    stats_mstats[index] = stats_mstats[index] + amount
    return stats_mstats

def check_inv_for_empty(stats_check_inv: list):                           #Checks the last 4 indexes (the players inventory) in the Stat list and checks if any of them are empty or not, if it finds one, it will return the index of the first-
    emptyindex: int = -1                                        #empty slot it finds, otherwise it will return -1 which indicates that the player has no room for more items
    for i in range(7,11):
        if stats_check_inv[i]==0:
            emptyindex = i
            break
    return emptyindex

def use_item(stats_use_item: list):
    itemlist = stats_use_item[-4:]
    nameindex = ["Meat", "Apple", "Bread", "Cheese", "Magic Potion"]
    itemchoice: int = -1
    print(itemlist)
    if(all(i == 0 for i in itemlist)):
        print ("You have no items to use")
        return
    print("**********************")
    print("INVENTORY (enter the items corresponding number to use, or 0 to go back)\n")
    for index, x in enumerate(itemlist):
        if( x== 1):
            print(index+1, ")", nameindex[0])
        elif(x == 2):
            print(index+1, ")", nameindex[1])
        elif(x == 3):
            print(index+1, ")", nameindex[2])
        elif(x == 4):
            print(index+1, ")", nameindex[3])
        elif(x == 5):
            print(index+1, ")", nameindex[4])
        else:
            print(index+1, ") none")
    print("\n**********************")
    while(itemchoice not in (0,1,2,3,4)):
        itemchoice = input("")
    if(itemchoice == 0):
        return
    else:
        print("Do you want to use ", nameindex[itemchoice-1], "? (1 for yes, 0 for no)")
        itemchoice = -1
        while(itemchoice not in (0,1)):
                itemchoice = input("")
        if(itemchoice == 0):
            return

        print("You consumed ", )
def d_stats(stats_dstats: list):                                #Function used to display all relevant information on the Imp's status to the player
    print(f"\nImp's current status: \n")
    print(f"***************************\n")
    print("\tCURRENT CONDITION: ", end=" ")
    if stats_dstats[0]==5:                                      #Health values are represented with text, showing how healthy the player is
        print("Great")
    elif stats_dstats[0]==4:
        print("Good")
    elif stats_dstats[0]==3:
        print("Fair")
    elif stats_dstats[0]==2:
        print("Bad")
    elif stats_dstats[0]==1:
        print("Critical")
    else:
        print("ERROR")                                          #There shouldn't be an instance where stats will be displayed if health is 0, so this let's me know if that accidentally happens

    print("\n\tCURRENT STATS:")
    print(f"\tSTRENGTH: ", stats_dstats[1])                     #Current Strength Stat
    print(f"\tDEX: ", stats_dstats[2])                          #Current Dex Stat
    print(f"\tMIND: ", stats_dstats[3])                         #Current Mind Stat
    print(f"\tSPEED: ", stats_dstats[4])                        #Current Speed Stat

    
    print(f"\n\tWEAPON: ", end=" ")                             #Shows which weapon is currently equipped, a value of 0 will display 'none'
    if stats_dstats[5]==1:
        print("Sword")
    elif stats_dstats[5]==2:
        print("Mace")
    elif stats_dstats[5]==3:
        print("Wand")
    elif stats_dstats[5]==4:
        print("Staff")
    elif stats_dstats[5]==5:
        print("Dagger")
    elif stats_dstats[5]==6:
        print("Bow")
    elif stats_dstats[5]==7:
        print("Magic Sword")
    elif stats_dstats[5]==8:
        print("Wizard Staff")
    elif stats_dstats[5]==9:
        print("Magic Bow")
    else:
        print("none")

    items = [stats_dstats[7],stats_dstats[8],stats_dstats[9],stats_dstats[10]]      #Shows what Items the player has currently, it will only include actual valid items, and shows nothing if there isn't an item
    print("\tITEMS:", end=" ")
    for i in items:
        if i==1:
            print("meat ", end="|")
        elif i==2:
            print("apple ", end="|")
        elif i==3:
            print("bread ", end="|")
        elif i==4:
            print("cheese ", end="|")
        elif i==5:
            print("magic potion ", end="|")
        elif i==6:
            print("bomb ", end="|")
        else:
            print("", end="")

    print(f"\n\tGOLD: ", stats_dstats[6])                               #How much gold the player is currently holding
    print(f"\n***************************\n")


def battle_scenario(stats_battle_scenario: list):                       #The function that determines how battles play out, requires the list of stats as an argument
    enemyrole = random.randint(1,100)                                   #Randomly generates a number from 1 to 100 to determine what enemy the player will encounter
    enemy_alive: bool = True                                            #Keeps track of whether the enemy is alive
    enemystats = ["", 0, 0, 0, 0, 0]                                    #List that takes the data from the above tuples to be used in the rest of the function
    attacktype: int = 0                                                 #Which kind of attack the player chooses, it determines what stats will be rolled against eachother to determine the outcome of the battle
    tally_damage: int = 0                                               #The amount of damage the player has taken, it is counted up every time the player fails a role against an enemy
    playerattackstat: int = 0                                           #Stores whichever attack stat the player chooses for use in the rest of the function
    if(enemyrole<=30):
        enemystats = SLIME_STATS
    elif(enemyrole>30 and enemyrole<=50):
        enemystats = RAT_STATS
    elif(enemyrole>50 and enemyrole <=70):
        enemystats = BAT_STATS
    elif(enemyrole>=70 and enemyrole <=90):
        enemystats = WOLF_STATS
    elif(enemyrole>90):
        enemystats = TROLL_STATS

    print("\n*******************")
    print("You have encountered a " + enemystats[0] + "!!!")        #Displays the enemy name
    print("\nWhat shall you do?:")
    print(f"1) Attack head-on")                                     #Attack will use the player and enemy's Strength stat for dice role
    print(f"2) Attack deftly")                                      #Attack will use the player and enemy's Dex stat for dice role
    print(f"3) Attack cunningly")                                   #Attack will use the player and enemy's Mind stat for dice role
    print(f"4) Flee")                                               #Will use the player and enemy's speed stat to determine if the player can run away successfully

    while attacktype not in (1, 2, 3, 4):                           #Make sure the user inputs a valid number
        try:
            attacktype = int(input("Choose a number: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue
        if (attacktype == 1):
            playerattackstat = stats_battle_scenario[1]             #Player's attack stat will be their strength stat
        elif(attacktype == 2):
            playerattackstat = stats_battle_scenario[2]             #Player's attack stat will be their dex stat
        elif(attacktype == 3):
            playerattackstat = stats_battle_scenario[3]             #Player's attack stat will be their mind stat
        elif(attacktype == 4):
            playerattackstat = stats_battle_scenario[4]             #Player's flee chance will be their speed stat
            print("You tried to flee...")
    while(enemy_alive):                                             #The main loop that determines the outcome of battle
        if(stats_battle_scenario[0]<=0):                            #Checks if the player is still alive and immediatly ends the loop if they are not
            print("You have fallen in battle. Game Over...")        #ded
            return
        playerattackrole = random.randint(playerattackstat, 10)     #Random number ranging from the player's attack stat to 10
        #print(playerattackrole)
        #print(enemystats[attacktype]) 
        if(playerattackrole > enemystats[attacktype]):              #Compares the player's attack stat to the enemy's corresponding stat
            if(attacktype != 4):                                    #If the player chose any of the non-fleeing commands and succeeds the role, the enemy is no longer alive and ends the loop
                enemy_alive = False
            else:
                print(".. and successed!\n")                        #If the player chose to flee, end the function, which prevents you from gaining any gold
                return
        else:
            m_stats(stats_battle_scenario, 0, -1)                   #If playerattackrole is lower than the enemie's stat, then you take 1 point of damage and retry the role until either you succeed or lose all your health
            tally_damage += 1                                       #tallies up how many times you failed the role2

    if(stats_battle_scenario[0]>0):                                 #Display outcome message when you defeat an enemy
        print("You have defeated ",  enemystats[0], "!!!\n")
        print("You have taken ", tally_damage, "damage\n")
        print("You have gained ", enemystats[5], "gold!!")
        m_stats(stats_battle_scenario, 6, enemystats[5])

        

def between_scenario(stats_between_scenario: list):
    choice: int = 0
    print("\n*******************")
    print("Do you want to use an item, or continue forward? (1 to continue, 2 to use an item)")
    while choice not in (1,2):
        choice = input(int)
    if(choice==1):
        use_item(stats_between_scenario)
    elif(choice==2):
        print("You decide to venture forth...")

def trade_scenario(stats_trade_scenario: list):
    print("\n*******************")                     #Function that determines how trading works
    print("Trade Scenario hasn't been finished yet!")
    return 0

def treasure_scenario(stats_treasure_scenario: list):               #Function that determines how finding a treasure chest works
    print("Treasure scenario hasn't been finished yet!!")
    return 0

def create_scenario(stats_create_scenario: list):                   #Function that generates 1 of the 3 above scenarios at a specified chance
    TOTALCHANCE: int = 0                                            #Adds up the % chance of all 3 scenarios
    BATTLECHANCE: int = 100                                         #% chance that a battle scenario will be generated
    TRADECHANCE: int = 0                                            #% chance that a trade scenario will be generated
    TREASURECHANCE: int = 0                                         #% chance that a treasure scenario will be generated
    ALLSCENARIOVALUES = [BATTLECHANCE, TRADECHANCE, TREASURECHANCE] #Store the 3 values in a list for later use
    for i in ALLSCENARIOVALUES:
        TOTALCHANCE = TOTALCHANCE + i

    if TOTALCHANCE != 100:                                          #Checks if the total % chance value of the 3 scenarios actually equals 100 and throws an error message if it doesn't
        print("ERROR: Scenario Chances must add up to 100!")
        return stats_create_scenario
    dicerole = random.randint(1, TOTALCHANCE)                       #Random number is generated to use for the dice role
    if(dicerole<=BATTLECHANCE):
        battle_scenario(stats_create_scenario)                      #generate battle scenario by calling the battlescenario function
    elif dicerole>BATTLECHANCE and dicerole <=BATTLECHANCE+TRADECHANCE:
        trade_scenario(stats_create_scenario)                       #generate trade scenario by calling the tradecenario function
    elif(dicerole>BATTLECHANCE+TRADECHANCE):
        treasure_scenario(stats_create_scenario)                    #generate treasure scenario by calling the trasurescenario function
        