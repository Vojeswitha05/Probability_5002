import random as rd

# Defining a function for rolling 2 dice at a time 
def rolling_2_dice(Event_happening):
    count_1=0
    count_2=0
    count_3=0
    n_experiment=1000000
    #repeating the experiment 1000000 times 
    for i in range(n_experiment):
    # dice_1 and dice_2 are outcomes of the two dices 
        dice_1=rd.randint(1,6)
        dice_2=rd.randint(1,6)
        
        #defining event E_1 as 6 facing up only on dice_1
        #defining event E_2 as 6 facing up only on dice_2
        #defining event E_3 as 6 facing up on both dice_1 and dice_2
        if Event_happening=='E_1':
            if dice_1==6 and dice_2 != 6:
                count_1=count_1+1
            
        if Event_happening=='E_2':
            if dice_1 != 6 and dice_2==6:
                count_2=count_2+1  

        if Event_happening=='E_3':
            if dice_1==6 and dice_2==6 :
                count_3=count_3+1
        
        # defining event E as getting atleast one 6 facing up
        #Event_happening E = E_1 + E_2 + E_3            

    return (count_1 + count_2 + count_3 )/n_experiment

print("Simulation  : The probability of atleast one 6 facing up = ",rolling_2_dice('E_1') + rolling_2_dice('E_2') + rolling_2_dice('E_3'))
print("Theoritical : The probability of atleast one 6 facing up = 11/36 =", 11/36)
