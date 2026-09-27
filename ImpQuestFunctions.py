import random

RAT_STATS = ("Rat",3,4,3,5,3)                   #Tuples containing all the info for the enemies, first slot is their name, 2nd is Strength value, 3rd is Dex, 4th is Mind, 5th is Speed, and 6th is gold amount when defeated
SLIME_STATS = ("Slime",2,2,2,2,1)
BAT_STATS = ("Bat",4,4,4,9,3)
TROLL_STATS = ("Troll",8,5,5,5,7)
WOLF_STATS = ("Wolf",5,5,4,7,5)
MIMIC_STATS = ("Mimic", 7,7,7,7,10)
DRAGON_STATS = ("Dragon", 9,9,9,9,10)

MEAT_STATS = ("Meat", 1, 1, 0, 0, 0, 5, "Restores health and increases Strength by 1.")                 #Tuples containing all the info for inventory items, first slot is their name, 2nd is Strength value, 3rd is Dex, 4th is Mind, 5th is Speed, 6th is base cost in gold, and 7th is its description
APPLE_STATS = ("Apple", 1, 0, 1, 0, 0, 5, "Restores health and increases Dex by 1.")
BREAD_STATS = ("Bread", 1, 0, 0, 1, 0, 5, "Restores health and increases Mind by 1.")
CHEESE_STATS = ("Cheese", 1, 0, 0, 0, 1, 5, "Restores health and increases Speed by 1.")
MAGIC_POTION = ("Magic Potion", 3, 1, 1, 1, 1, 30, "Restores health and increases all stats by 1.")
BOMB_STATS = ("Bomb", -5, 0, 0, 0, 0, 25, "Bomb to be used on enemies, DO NOT EAT!!")

SWORD_STATS = ("Sword", 0, 1, 1, 0, 0, 8, "Weapon that increases Strength and Dex by 1 each")                                      ##Tuples containing all the info for weapons, first slot is their name, 2nd is Strength value, 3rd is Dex, 4th is Mind, 5th is Speed, 6th is base cost in gold
MACE_STATS = ("Mace", 0, 2, 1, 0, 0, 20, "Weapon that increases Strength by 2 and Dex by 1")
WAND_STATS = ("Wand", 0, 0, 0, 1, 1, 8, "Weapon that increases Mind and Speed by 1 each")
STAFF_STATS = ("Staff", 0, 1, 0, 2, 0, 20, "Weapon that increases Strength by 1 and Mind by 2")
DAGGER_STATS = ("Dagger", 0, 0, 1, 0, 1, 8, "Weapon that increases Dex and Speed by 1 each")
BOW_STATS = ("Bow", 0, 0, 2, 0, 1, 20, "Weapon that increases Dex by 2 and Speed by 1" )
MAGICSWORD_STATS = ("Magic Sword", 0, 3, 1, 1, 1, 0, "Rare Weapon that increases Strength by 3 and all other stats by 1")
WIZARDSTAFF_STATS = ("Wizard Staff", 0, 1, 1, 3, 1, 0, "Rare Weapon that increases Mind by 3 and all other stats by 1")
MAGICBOW_STATS = ("Magic Bow", 0, 1, 3, 1, 1, 0, "Rare Weapon that increases Dex by 3 and all other stats by 1")


def m_stats(stats_mstats: list, index: int, amount: int):       #Modifies a specific value in a provided Stat list by a specified amount, used to change/add/lose health, stats, gold, items etc.
    if(index==0):
        if(stats_mstats[index]+amount>5):               #If Health is being modified, and the sum of the current amount and the amount that is added is over 5, set it to 5 (This makes it so 5 is the max health amount)
            stats_mstats[0] = 5
        else:
            stats_mstats[0] += amount
    elif(1 <= index <=4):                               #If the 4 main stats are being modified, and the sum of the current amount and the amount that is added is over 9, set it to 9 (This makes it so 9 is the stat cap)
        if(stats_mstats[index]+amount>9):
            stats_mstats[index]=9
        else:
            stats_mstats[index] += amount
    else:
        stats_mstats[index] += amount                   #All other indexes have no such limit since weapons and items are set directly and not simply added or subtracted
    return stats_mstats
    

def buffer():                                           #Buffer that displays a "Press Enter" and stays on screen until the user presses enter)
    b=input("\n(Press Enter)")                          #Value doesn't matter since it's just used to control the speed of the game

def check_inv_for_empty(stats_check_inv: list):                           #Checks the last 4 indexes (the players inventory) in the Stat list and checks if any of them are empty or not, if it finds one, it will return the index of the first-
    emptyindex: int = -1                                        #empty slot it finds, otherwise it will return -1 which indicates that the player has no room for more items
    for i in range(7,11):
        if stats_check_inv[i]==0:
            emptyindex = i
            return emptyindex
    return emptyindex

def check_price(yourgold: int, cost: int):
    if(yourgold-cost>=0):
        return True
    else:
        return False
 


def returniteminfo(i: int, j: int):                     #Returns an specified item's value at a specified index, used return values that modify health/stats/etc
    if( i== 1):
        return MEAT_STATS[j]
    elif(i == 2):
        return APPLE_STATS[j]
    elif(i == 3):
        return BREAD_STATS[j]
    elif(i == 4): 
        return CHEESE_STATS[j]
    elif(i == 5):
        return MAGIC_POTION[j]
    elif(i == 6):
        return BOMB_STATS[j]
    elif(i == 7):
        return SWORD_STATS[j]
    elif(i == 8):
        return MACE_STATS[j]
    elif(i == 9):
        return WAND_STATS[j]
    elif(i == 10):
        return STAFF_STATS[j]
    elif(i == 11):
        return DAGGER_STATS[j]
    elif(i == 12):
        return BOW_STATS[j]
    elif(i == 13):
        return MAGICSWORD_STATS[j]
    elif(i == 14):
        return WIZARDSTAFF_STATS[j]
    elif(i == 15):
        return MAGICBOW_STATS[j]
    elif(i not in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)):
        return 0

def equip_item(stats_equip_item: list, newwepindex: int):
    previous_weapon = stats_equip_item[5]

    if previous_weapon != 0:
        for stat_index in range(2, 6):
            m_stats(stats_equip_item,stat_index-1,-returniteminfo(previous_weapon, stat_index))

    stats_equip_item[5] = newwepindex

    for stat_index in range(2, 6):
        m_stats(stats_equip_item,stat_index-1,returniteminfo(newwepindex, stat_index))

def has_bomb(stats_has_bomb: list):
    for x in range(7,11):
        if(stats_has_bomb[x]==6):
            return True
    return False

def return_bomb_slot(stats_return_bomb_slot):
    emptyindex: int = -1                                        #empty slot it finds, otherwise it will return -1 which indicates that the player has no room for more items
    for i in range(7,11):
        if stats_return_bomb_slot[i]==6:
            emptyindex = i
            return emptyindex
    return emptyindex    

def use_item(stats_use_item: list):                         #Function that checks the users inventory for items, and then asks the user if they want to use items if there are any
    itemlist = stats_use_item[-4:]                          #takes the last 4 indexes in the user's stats (ie. the items) and puts them in their own list temperarily
    itemchoice: int = -1                                    #The initial value of the choice when the game asks you which item you want to use
    confirmchoice: int = -1                                 #The initial value of the choice when the game asks you if you want to confirm using the item
    if(all(i == 0 for i in itemlist)):                      #If all values in the list are 0, then print a message and return to previous state
        print ("You have no items to use")
        buffer()
        return
    print("**********************")
    print("INVENTORY (enter the items corresponding number to use, or 0 to go back)\n")
    for index, x in enumerate(itemlist):                                #Goes through itemlist and prints out the name and which slot it occupies
        print(index+1, ")", returniteminfo(x,0))

    print("\n**********************")
    while itemchoice not in (0,1,2,3,4):                #Loop that asks the user to enter 1 of 4 of your items, or 0 if you want to cancel
        try:
            itemchoice = int(input("Enter Value: "))    #Asks for valid input, and spits out an error if it isn't
        except ValueError:
            print("Must enter a valid number.")
    if(itemchoice == 0):                                #Returns the user to previous state if you enter 0
        between_scenario(stats_use_item)
        return
    if(itemlist[itemchoice-1] in (1,2,3,4,5)):              #Asks the user to confirm your choice to use an item
        print(returniteminfo(itemlist[itemchoice-1], 7), "Confirm your choice (1 for yes, 0 for no)")
    elif(itemlist[itemchoice-1] == 6):                      #Special message if the item selected is a bomb, since you're not suppose to use it outside of a battle (you can but it will kill you automatically)
        print(returniteminfo(itemlist[itemchoice-1], 7), "You really shouldn't use this right now... (1 for yes, 0 for no)")
    while confirmchoice not in (0,1):                       #Asks for valid input, spits out an error if it isn't
        try:
            confirmchoice = int(input())
        except ValueError:
            print("Must enter a valid number.")
    if(confirmchoice == 0):                                 #Cancels using the item and boots you back to a previous state
        between_scenario(stats_use_item)
        return
    elif(confirmchoice == 1):                               #Uses the item that you have selected
        print("You consumed ", returniteminfo(itemlist[itemchoice-1], 0))
        for m in range(1,5):                               #Loops through the user's Health, Strength, Dex, Mind, and Speed and modifies them based on the stats of the item you just used
            m_stats(stats_use_item, m - 1, returniteminfo(itemlist[itemchoice - 1], m))
            print(returniteminfo(itemlist[itemchoice - 1], m))
        itemlist[itemchoice - 1] = 0                        #sets the item of what you just used to 0, getting rid of it from your inventory and then takes itemlist and adds it back to the original stat list before returning it
        stats_use_item[-4:] = itemlist
        return stats_use_item


def d_stats(stats_dstats: list):                                #Function used to display all relevant information on the Imp's status to the player
    print(f"\nImp's current status: \n")
    print(f"***************************")
    print("\tCURRENT CONDITION: ", end="\n")
    if stats_dstats[0]==5:                                      #Health values are represented with text, showing how healthy the player is
        print("\tGreat (5)")
    elif stats_dstats[0]==4:
        print("\tGood (4)")
    elif stats_dstats[0]==3:
        print("\tOkay (3)")
    elif stats_dstats[0]==2:
        print("\tBad (2)")
    elif stats_dstats[0]==1:
        print("\tCritical! (1)")
    else:
        print(stats_dstats[0], "ERROR")                                          #There shouldn't be an instance where stats will be displayed if health is 0, so this let's me know if that accidentally happens

    print("\n\tCURRENT STATS:")
    print(f"\tSTRENGTH: ", stats_dstats[1])                     #Current Strength Stat
    print(f"\tDEX: ", stats_dstats[2])                          #Current Dex Stat
    print(f"\tMIND: ", stats_dstats[3])                         #Current Mind Stat
    print(f"\tSPEED: ", stats_dstats[4])                        #Current Speed Stat

    
    print(f"\n\tWEAPON: ", end=" ")                             #Shows which weapon is currently equipped, a value of 0 will display 'none'
    if stats_dstats[5]==7:
        print(SWORD_STATS[0])
    elif stats_dstats[5]==8:
        print(MACE_STATS[0])
    elif stats_dstats[5]==9:
        print(WAND_STATS[0])
    elif stats_dstats[5]==10:
        print(STAFF_STATS[0])
    elif stats_dstats[5]==11:
        print(DAGGER_STATS[0])
    elif stats_dstats[5]==12:
        print(BOW_STATS[0])
    elif stats_dstats[5]==13:
        print(MAGICSWORD_STATS[0])
    elif stats_dstats[5]==14:
        print(WIZARDSTAFF_STATS[0])
    elif stats_dstats[5]==15:
        print(MAGICBOW_STATS[0])
    else:
        print("none")

    items = [stats_dstats[7],stats_dstats[8],stats_dstats[9],stats_dstats[10]]      #Shows what Items the player has currently, it will only include actual valid items, and shows nothing if there isn't an item
    print("\tITEMS:", end=" ")
    for i in items:
        if i==1:
            print(MEAT_STATS[0], end="|")
        elif i==2:
            print(APPLE_STATS[0], end="|")
        elif i==3:
            print(BREAD_STATS[0], end="|")
        elif i==4:
            print(CHEESE_STATS[0], end="|")
        elif i==5:
            print(MAGIC_POTION[0], end="|")
        elif i==6:
            print(BOMB_STATS[0], end="|")
        else:
            print("", end="")

    print(f"\n\tGOLD: ", stats_dstats[6])                               #How much gold the player is currently holding
    print(f"***************************\n")


def battle_scenario(stats_battle_scenario: list, encounternum: int, Mimic_Encounter: bool):                      #The function that determines how battles play out, requires the list of stats as an argument
    enemyrole = random.randint(1,100)                                   #Randomly generates a number from 1 to 100 to determine what enemy the player will encounter
    enemy_alive: bool = True                                            #Keeps track of whether the enemy is alive
    enemystats = ["", 0, 0, 0, 0, 0]                                    #List that takes the data from the above tuples to be used in the rest of the function
    attacktype: int = 0                                                 #Which kind of attack the player chooses, it determines what stats will be rolled against eachother to determine the outcome of the battle
    tally_damage: int = 0                                               #The amount of damage the player has taken, it is counted up every time the player fails a role against an enemy
    playerattackstat: int = 0
    if(Mimic_Encounter==False):                                           #Stores whichever attack stat the player chooses for use in the rest of the function
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
    else:
        enemystats = MIMIC_STATS

    print("\n*******[ ENCOUNTER ", encounternum, "]*******")
    print("You have encountered a " + enemystats[0] + "!!!")        #Displays the enemy name
    print("\nWhat shall you do?:")
    print(f"1) Attack head-on")                                     #Attack will use the player and enemy's Strength stat for dice role
    print(f"2) Attack deftly")                                      #Attack will use the player and enemy's Dex stat for dice role
    print(f"3) Attack cunningly")                                   #Attack will use the player and enemy's Mind stat for dice role
    print(f"4) Flee")
    print(f"5) Throw bomb")                                               #Will use the player and enemy's speed stat to determine if the player can run away successfully

    while attacktype not in (1, 2, 3, 4, 5):                           #Make sure the user inputs a valid number
        try:
            attacktype = int(input("Choose a number: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")
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
        elif(attacktype == 5):
            if(has_bomb(stats_battle_scenario)):
                print("You threw a bomb!!")
                buffer()
                enemy_alive=False
            else:
                print("You do not have a bomb to throw")
                attacktype = 0
    while(enemy_alive):                                             #The main loop that determines the outcome of battle
        if(stats_battle_scenario[0]<=0):                            #Checks if the player is still alive and immediatly ends the loop if they are not
            print("You were defeated by", enemystats[0])
            print("You have fallen in battle...")                   #ded
            return
        playerattackrole = random.randint(playerattackstat, 10)     #Random number ranging from the player's attack stat to 10
        #print(playerattackrole)
        #print(enemystats[attacktype]) 
        if(playerattackrole > enemystats[attacktype]):              #Compares the player's attack stat to the enemy's corresponding stat
            if(attacktype != 4):                                    #If the player chose any of the non-fleeing commands and succeeds the role, the enemy is no longer alive and ends the loop
                enemy_alive = False
            else:
                print(".. and successed and took ", tally_damage, "damage\n")                        #If the player chose to flee, end the function, which prevents you from gaining any gold
                return
        else:
            m_stats(stats_battle_scenario, 0, -1)                   #If playerattackrole is lower than the enemie's stat, then you take 1 point of damage and retry the role until either you succeed or lose all your health
            tally_damage += 1                                       #tallies up how many times you failed the role2

    if(stats_battle_scenario[0]>0):
        if(attacktype != 5):                                 #Display outcome message when you defeat an enemy
            print("You have defeated ",  enemystats[0], "!!!\n")
            print("You have taken ", tally_damage, "damage\n")
            print("You have gained ", enemystats[5], "gold!!")
            m_stats(stats_battle_scenario, 6, enemystats[5])
            return 1
        else:
            print("You blew up the ", enemystats[0], "!!!\n")
            m_stats(stats_battle_scenario, return_bomb_slot(stats_battle_scenario), -6)

        

def between_scenario(stats_between_scenario: list):         #The function that plays after 1 of the 3 scenarios that let's you use any items you might have before continuing to the next scenario
    choice: int = -1
    print("\n*******************")
    print("Do you want to use an item, or continue forward? (Enter to 1 continue, 2 to use an item)") #Gives the player a choice whether to use an item or just move on
    while choice not in (1, 2):
        try:
            choice = int(input())       #Repeatedly asks the user for an answer, and spits out an error if it isn't valid
        except ValueError:
            print("Please press enter or 1.")
    if(choice==2):
        use_item(stats_between_scenario)        #If you choose to use an item, it will call the use_item function
    elif(choice==1):
        print("You decide to venture forth...") #If you choose not to use an item, it will display a message before letting you continue
        buffer()
        return

def trade_scenario(stats_trade_scenario: list):
    choice1: int = -1
    choice2: int = -1
    selected_index = -1
    traderslots = [0,0,0,0,0,0]     #First 3 slots are the items, the last 3 slots are the price for their corresponding item
    item_id =0
    price =0
    print("\n*******************")                     #Function that determines how trading works
    print("You have encountered a Trader!!")
    while choice1 not in (1, 0):
        try:
            choice1 = int(input("Would you like to buy something from the trader? (enter for yes 0 for no)"))       #Repeatedly asks the user for an answer, and spits out an error if it isn't valid
        except ValueError:
            print("Please enter 0 or enter.")
    if(choice1==1):    
        print("You have ", stats_trade_scenario[6], "Gold")     #Displays how much gold your carrying before you purchase
        print("The Trader is selling the following items: ")
        for i in range(len(traderslots)):           #Roles the item and prices for said items
            if(i<3):
                traderslots[i] = random.randint(1,12)   #roles the item's id
            elif(i>=3):
                traderslots[i] = returniteminfo(traderslots[i-3], 6) + random.randint(0,returniteminfo(traderslots[i-3], 6)//2)     #Roles the item's price. Determined by the item's base price + 0 up to half the item's base price added on
        for j in range(3):
            if(j<3):
                item_id = traderslots[j]
                price = traderslots[j+3]
                print(j+1, ")", returniteminfo(item_id,0), "-", price, "gold -", returniteminfo(item_id,7))
        while choice2 not in (0,1,2,3):
            try:
                choice2 = int(input("Which item would you like to buy? (Enter number to choose item, or 0 to exit)"))       #Repeatedly asks the user for an answer, and spits out an error if it isn't valid
            except ValueError:
                print("Please enter 0, 1, 2, or 3")
            print("\n*******************")
            if(choice2!=0): 
                selected_index = choice2 -1
                item_id = traderslots[selected_index]
                price = traderslots[selected_index+3]
                if(1 <= item_id <=6):           #If the item is non-equipable, checks the inv to see if it's full or not
                    if(check_price(stats_trade_scenario[6], price) and check_inv_for_empty(stats_trade_scenario)!=-1):
                        m_stats(stats_trade_scenario, check_inv_for_empty(stats_trade_scenario), item_id)
                        m_stats(stats_trade_scenario, 6, 0 - price)
                        print("Thank you for your purchase! Please come again!")
                    elif(check_inv_for_empty(stats_trade_scenario)==-1):
                        print("Looks like your inventory is full. Come back when you have less stuff!")
                        print("You leave the Trader")
                        return
                    else:
                        print("You can't afford this right now. Come back when you have more gold!")
                        print("You leave the Trader")

                elif(7 <= item_id <=12):        #If the Item is an equippable item, it will always swap out with what you have as long as you can afford the new item
                    if(check_price(stats_trade_scenario[6], price)):
                        equip_item(stats_trade_scenario, item_id)
                        m_stats(stats_trade_scenario, 6, 0 - price)
                        print("Thank you for your purchase! Please come again!")
                        print("You leave the Trader")
                    else:
                        print("You can't afford this right now. Come back when you have more gold!")
                        print("You leave the Trader")
            else:
                print("You changed your mind on buying something ")
                return
    
    elif(choice1==0):       #If you select 0, leave the trader and move on
        print("You decided not to buy anything")
        return


def treasure_scenario(stats_treasure_scenario: list, encounternum: int):    #Function that runs the treasure scenario
    choice1: int = -1
    choice2: int = -1
    MIMIC_CHANCE = 30               #Chance that a mimic will spawn instead of a normal trasure
    treasure_id: int = -1
    treasure_drop: int =-1
    old_item_id: int =-1          
    print("You have found a treasure chest!!!")
    while choice1 not in (1, 0):
            try:
                choice1 = int(input("Would you like to open it up? (enter 1 for yes, 0 for no)"))       #Repeatedly asks the user for an answer, and spits out an error if it isn't valid
            except ValueError:
                print("Please press enter or 0.")
    if(choice1==1):
        print("You opened the treasure chest. Inside there's...")
        buffer()
        if(random.randint(1,100)>=100-MIMIC_CHANCE):                #Roles for a chance of a mimic spawning
            print("It was a Mimic!!!")
            battle_scenario(stats_treasure_scenario, encounternum, True)    #Runs the battle scenario with extra code telling that a mimic spawned

            treasure_drop = random.randint(1,5)     #Encountering a mimc gives a chance for rare items to spawn instead of normal items
            if(treasure_drop==1):
                treasure_id = 6
            elif(treasure_drop==2):
                treasure_id = 13
            elif(treasure_drop==3):
                treasure_id = 14
            elif(treasure_drop==4):
                treasure_id = 15
            else:
                treasure_id = 0
        else:
            treasure_id = random.randint(1, 12)         #Normal treasure spawn function

        if(treasure_id>0):
            print("You found a ", returniteminfo(treasure_id,0), "!!!")
            buffer()
            if(1 <= treasure_id <=6):               #Checks if the item is a non-equipable item and sees if your inventory is full or not
                if(check_inv_for_empty(stats_treasure_scenario)!=-1):
                    print("Added ", returniteminfo(treasure_id,0), "to your inventory!!")
                    m_stats(stats_treasure_scenario, check_inv_for_empty(stats_treasure_scenario), treasure_id)
                    return
                else:
                    print("Your inventory is currently full")
                    buffer()
                    while choice2 not in (0,4):         #Gives the option to switch out a the treasure for one of your item slots
                        try:
                            choice2 = int(input("What item would you like to swap it out for? (Enter item number to swap, 0 to cancel)"))       #Repeatedly asks the user for an answer, and spits out an error if it isn't valid
                        except ValueError:
                            print("Please enter a valid number.")
                    for i in range(7,11):               
                        print(i-6,")", returniteminfo(stats_treasure_scenario[i],0))
                    if(choice2!=0):
                        old_item_id = stats_treasure_scenario(choice2+6)
                        print("You got rid of your", returniteminfo(stats_treasure_scenario, choice2+6,0))
                        m_stats(stats_treasure_scenario, choice2+6, -old_item_id)
                        m_stats(stats_treasure_scenario, choice2+6, treasure_id)
                        print("And replaced it with ", returniteminfo(treasure_id,0))
            if(7 <= treasure_id <= 15):         #If the item is an equipable item, always gives you the option to swap it out with your current weapon
                
                if(stats_treasure_scenario[5]!=0):
                    print("Do you want to equip the ", returniteminfo(treasure_id,0), "?")
                    while choice2 not in (0,1):
                        try:
                            choice2 = int(input("1 for yes, 0 for no: "))       #Repeatedly asks the user for an answer, and spits out an error if it isn't valid
                        except ValueError:
                            print("Please enter a valid number.")
                    if(choice2==1):     #Code that asks you if you want to swap out your weapon
                        print("You threw out your ", returniteminfo(stats_treasure_scenario[5],0), " and replaced it with the", returniteminfo(treasure_id,0))
                        equip_item(stats_treasure_scenario, treasure_id)
                    else:
                        print("You left the ", returniteminfo(treasure_id,0), "behind...")  #Abandons weapon if you choose not to equip it
                else:
                    print("You equipped the ", returniteminfo(treasure_id,0) )
                    equip_item(stats_treasure_scenario, treasure_id)
    else:
        print("You left the Treasure chest alone...")
        buffer()
    return 

def create_scenario(stats_create_scenario: list, encounternum: int):                   #Function that generates 1 of the 3 above scenarios at a specified chance
    TOTALCHANCE: int = 0                                            #Adds up the % chance of all 3 scenarios
    BATTLECHANCE: int = 60                                         #% chance that a battle scenario will be generated
    TRADECHANCE: int =  30                                           #% chance that a trade scenario will be generated
    TREASURECHANCE: int = 10                                         #% chance that a treasure scenario will be generated
    ALLSCENARIOVALUES = [BATTLECHANCE, TRADECHANCE, TREASURECHANCE] #Store the 3 values in a list for later use
    for i in ALLSCENARIOVALUES:
        TOTALCHANCE = TOTALCHANCE + i

    if TOTALCHANCE != 100:                                          #Checks if the total % chance value of the 3 scenarios actually equals 100 and throws an error message if it doesn't
        print("ERROR: Scenario Chances must add up to 100!")
        return stats_create_scenario
    dicerole = random.randint(1, TOTALCHANCE)                       #Random number is generated to use for the dice role
    if(dicerole<=BATTLECHANCE):
        battle_scenario(stats_create_scenario, encounternum, False)                      #generate battle scenario by calling the battlescenario function
    elif dicerole>BATTLECHANCE and dicerole <=BATTLECHANCE+TRADECHANCE:
        trade_scenario(stats_create_scenario)                       #generate trade scenario by calling the tradecenario function
    elif(dicerole>BATTLECHANCE+TRADECHANCE):
        treasure_scenario(stats_create_scenario, encounternum)                    #generate treasure scenario by calling the trasurescenario function

def dragon_scenario(stats_dragon_scenario):                     #Function that controls the final dragon scenario
    enemystats = ["",9,9,9,9,0]                                  #List that takes the data from the above tuples to be used in the rest of the function
    attacktype: int = 0                                                 #Which kind of attack the player chooses, it determines what stats will be rolled against eachother to determine the outcome of the battle                                               #The amount of damage the player has taken, it is counted up every time the player fails a role against an enemy
    playerattackstat: int = 0
    playerattackrole: int = 0
    dragon_health: int = 3              #Dragon has health unlike other enemies
    print("You finally made it to the dragon's lair...")
    buffer()
    print("Are you ready?")
    buffer()
    print("Before you can think, the dragon flies down towards you and begins to attack!!!")
    buffer()
    print("\n*******[ FINAL ENCOUNTER ]*******")
    while(stats_dragon_scenario[0]>0 and dragon_health>0):              #Similar to battle scenario, but you can't flee
        print("The Dragon gives you an intimidating glare!")
        print(f"1) Attack head-on")                                     #Attack will use the player and enemy's Strength stat for dice role
        print(f"2) Attack deftly")                                      #Attack will use the player and enemy's Dex stat for dice role
        print(f"3) Attack cunningly")                                   #Attack will use the player and enemy's Mind stat for dice role
        print(f"4) Throw bomb")

        while attacktype not in (1, 2, 3, 4):                           #Make sure the user inputs a valid number
            try:
                attacktype = int(input("Choose wisely...: "))
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 4.")
                continue
            if (attacktype == 1):
                playerattackstat = stats_dragon_scenario[1]             #Player's attack stat will be their strength stat
            elif(attacktype == 2):
                playerattackstat = stats_dragon_scenario[2]             #Player's attack stat will be their dex stat
            elif(attacktype == 3):
                playerattackstat = stats_dragon_scenario[3]             #Player's attack stat will be their mind stat
            elif(attacktype == 4):
                if(has_bomb(stats_dragon_scenario)):
                    print("You threw a bomb!!")
                    buffer()
                else:
                    print("You do not have a bomb to throw")
                    attacktype = 0
        if attacktype == 4:         #If the player throws a bomb, it has a 50-50 shot of landing, lowering the dragons health by 1
            m_stats(stats_dragon_scenario, return_bomb_slot(stats_dragon_scenario), -6) 
            if(random.randint(1,2)==2):
                print("It Hit!!")
                dragon_health -= 1
            else:
                print("It didn't work...")
                buffer()
                print("The dragon attacked you in retaliation!")
                stats_dragon_scenario[0] += -random.randint(1,2)
            attacktype = 0
            continue
        playerattackrole = random.randint(playerattackstat, 10)         #Runs a attack role, similar to normal battles, but if you fail, subtract 1 or 2 health from the player
        if(playerattackrole>enemystats[attacktype] and attacktype!=0):  #If successful, lower dragon health by 1 point and repeat this until either the player or dragon is dead
            print("You got a hit!!")
            dragon_health += -1
            buffer()
            attacktype = 0
        elif(playerattackrole<=enemystats[attacktype] and attacktype!=0):
            print("Your attack didn't land...")
            buffer()
            print("The dragon attacked you in retaliation!")
            print("\n")
            stats_dragon_scenario[0] += -random.randint(1,2)
            attacktype = 0
    if(stats_dragon_scenario[0]<=0):                    #If the player runs out of health, run this
        print("You were defeated by the Dragon...")
        print("GAME OVER")
        return
    else:
        print("The Dragon has fallen...")               #If the player succeeds run the success messages
        buffer()
        print("You slayed the Dragon!! Now all of its riches are yours to keep!!")
        buffer()
        print("\tConglatueration !!!")                  #Old gamaing reference, spelling mistakes are on purpose
        buffer()
        print("\tYou have complete\n\t a great game")
        buffer()
        print("\tAnd Prooved the Justice \n\tof our culture.")
        print("\tNow go and rest our\n\t heroes !")
            