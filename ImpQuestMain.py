"""
    Imp Quest is a short text-based game where you make decisions for an Imp character by entering numerical inputs
    The Imp has health, and 4 types of stats that will dictate how well it will do against certain enemies
    Battles play out choosing 1 of 4 different actions, each action corrisponding to the Imp's stats
    The higher the stat the higher the chance of success against the enemy
    If you run out of health, it's game over and the program exits
"""

import ImpQuestFunctions as iqf         #All the functions are in the ImpQuestFunctions file to keep the main file a bit cleaner
                                        #These are the 11 values that make up the player character, they are initalized as seperate values before being put into a list simply to make it easier to know what I'm changing
IMPHEALTH: int = 5                      #Health value, if this hits 0 it's game over. Can get lowered by battles
IMPSTR: int = 1                         #Strength value, makes 'head-on attacks' more effective
IMPDEX: int = 1                         #Dex Value, makes 'deft attacks' more effective
IMPMIND: int = 1                        #Mind Value, makes 'cunning attacks' more effective
IMPSPEED: int = 1                       #Speed Value, makes running away more likely to succeed
IMPWEP: int = 0                         #Weapon, the value that corrisponds with 1 of 9 different weapons, 0 means no weapon is equipped
IMPGOLD: int = 30                        #The gold value that you have, gain gold from defeating foes
IMPINV0: int = 1                        #Inventory slot 0-3, these slots can hold a number of different items, usually healing items that can be used to recover health and increase stats
IMPINV1: int = 1
IMPINV2: int = 1
IMPINV3: int = 1

tally_scenarios: int =0                 #Keeps track of the current amount of scenarios there are 
tally_encounters: int =1                #Keeps track of how many battles you've had
MAX_SCENARIOS: int =20                  #The maximum amount of scenarios that can accure before the game ends

IMPSTATS = [IMPHEALTH,IMPSTR,IMPDEX,IMPMIND,IMPSPEED,IMPWEP,IMPGOLD,IMPINV0,IMPINV1,IMPINV2,IMPINV3]

print("***********************")
print("WELCOME TO IMP QUEST!! ")
print("***********************")

iqf.buffer()

while(IMPSTATS[0]>0 and tally_scenarios<MAX_SCENARIOS):                       #Main program loop, currently only have battle scenarios, but more are planned
    iqf.d_stats(IMPSTATS)                                                     #Displays the Imp's current stats
    iqf.buffer()
    iqf.create_scenario(IMPSTATS,tally_encounters)                            #Randomly generate a scenario
    tally_encounters += 1                                                     #Adds 1 to the tally encounter
    if(IMPSTATS[0]>0):                                                        #If the player falls to an enemy, it will skip the between scenario function
        iqf.buffer()
        iqf.between_scenario(IMPSTATS)
    tally_scenarios +=1

if(IMPSTATS[0]<=0):                                                         #If you lose all your health it's game over
    print("\nGAME OVER\n")
    print("Try Again?")