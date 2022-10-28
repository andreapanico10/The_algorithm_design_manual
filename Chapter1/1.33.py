'''There are twenty-five horses. 
At most, five horses can race together at a time. 
You must determine the fastest, second fastest, and third fastest horses.
Find the minimum number of races in which this can be done.

ANDREA_PANICO_note: It's considered only a comparison between horses, not a time rank.
''' 
import numpy as np
import random

class Horse:
    first_race_id = 0
    second_race_id = 0
    third_race_id = 0

    first_position = 0
    second_position = 0
    third_position = 0

    def __init__(self, name, time):
        self.name = name
        self.time = time

def print_horses_list(horses): # Utility print function
    for obj in horses:
        print( 'name:{}, time:{}, 1r_id: {}, position_1r: {}, 2r_id: {}, position_2r: {}, 3r_id: {}, position_3r: {}'.format(obj.name, obj.time, obj.first_race_id, obj.first_position,  obj.second_race_id, obj.second_position, obj.third_race_id, obj.third_position), sep =' ' )

def print_rank(horses): # Utility final print function 
    official_first = list(filter(lambda x: x.first_position == 1 and x.second_position == 1, horses))[0]
    official_second = list(filter(lambda x: (x.second_race_id == 7 and x.second_position == 1) or (x.third_race_id == 7 and x.third_position == 1) , horses))[0]
    official_third = list(filter(lambda x: (x.second_race_id == 7 and x.second_position == 2) or (x.third_race_id == 7 and x.third_position == 2) , horses))[0]

    print('First classified: Horse {}, time: {}'.format(official_first.name, official_first.time))
    print('Second classified: Horse {}, time: {}'.format(official_second.name, official_second.time))
    print('Third classified: Horse {}, time: {}'.format(official_third.name, official_third.time))


horses_names = list(map(str,np.arange(1,26))) # Generate horse names
horses_times = np.round(np.random.random_sample(size = len(horses_names)),3) # Randomly generate horse times
horses = [] # List of horse object
for i in range(len(horses_names)):
    new_horse = Horse(horses_names[i],horses_times[i])
    horses.append(new_horse)

actual_running_horses = []
print()
print('********* STARTING GRID ************')
print()
sorted_horses = horses.sort(key=lambda x: x.time) # This is the final grid ordered 
print_horses_list(horses)
print()

print('********* ALGORITHM RESULTS ************')
print('Reached in 7 races')
print()

print()
race_id = 0
for race in range(5): # 5 Starting race
    start = race_id*5 
    end = (race_id+1)*5
    for horse in horses[start:end]:
        horse.first_race_id = race_id+1
    battery = horses[start:end]

    battery.sort(key=lambda x: x.time) # RACE
    first_three_winners = battery[:3]
    for i in range(len(first_three_winners)):
        first_three_winners[i].first_position = i + 1 
        
    actual_running_horses.extend(first_three_winners) # How to append all the element of a list to another list
    race_id += 1


##### RACE # 6 #######
# Between all the first ranked #
battery_6 = list(filter(lambda x: x.first_position == 1, actual_running_horses)) # Filtering all the 1st classified in their own race

for horse in battery_6:
    horse.second_race_id = 6
battery_6.sort(key=lambda x: x.time) # RACE
first_three_winners = battery_6[:3]
for i in range(len(first_three_winners)):
    first_three_winners[i].second_position = i + 1 

# Two eliminated: slowest first

fourth_ranked = battery_6[-2]
fifth_ranked = battery_6[-1]

# It's useless take the second and third because they are slower than the first (eliminate yet)

race_to_delete_fourth = fourth_ranked.first_race_id
race_to_delete_fifth = fifth_ranked.first_race_id

actual_running_horses.remove(fourth_ranked)
actual_running_horses.remove(fifth_ranked)

actual_running_horses = list(filter(lambda x: (x.first_race_id!= race_to_delete_fourth and x.first_race_id!= race_to_delete_fifth) or x.first_position == 1, actual_running_horses))

# So it remains 9 horses, 3 of which yet ordered

# race # 7 
# Participants:
# Second and third of race # 6, the two second referred to 1st and 2nd of race #6 
# and the third referred to the all_time 1st... at this moment the official 1st could be elected -> 

first_classified = list(filter(lambda x: x.second_position > 1, actual_running_horses))
official_first = list(filter(lambda x: x.first_position == 1 and x.second_position == 1, actual_running_horses)) # Official All time 1st

third_first_race_id = first_classified[-1].first_race_id
first_first_race_id = official_first[0].first_race_id

second_classified = list(filter(lambda x: x.first_position == 2 and x.first_race_id != third_first_race_id, actual_running_horses))
third_classified = list(filter(lambda x: x.first_position == 3 and x.first_race_id == first_first_race_id, actual_running_horses))

battery_7 = []
battery_7.extend(first_classified)
battery_7.extend(second_classified)
battery_7.extend(third_classified)


for horse in battery_7:
    if(horse.second_race_id == 0):
        horse.second_race_id = 7
    else:
        horse.third_race_id = 7

battery_7.sort(key=lambda x: x.time) # RACE

for i in range(len(battery_7)):
        if(battery_7[i].second_position == 0):
            battery_7[i].second_position = i + 1 
        else:
            battery_7[i].third_position = i + 1 

# Two eliminated: slowest

fourth_ranked = battery_7[-2]
fifth_ranked = battery_7[-1]

# DROP ALL THE SLOWEST IN THE PREVIOUS BATTERIES

race_to_delete_fourth = fourth_ranked.first_race_id
race_to_delete_fifth = fifth_ranked.first_race_id

pos = fourth_ranked.first_position
pos_2 = fourth_ranked.second_position

pos_3 = fifth_ranked.first_position
pos_4 = fifth_ranked.second_position


race_to_delete_fourth_2 = fourth_ranked.second_race_id
race_to_delete_fifth_2 = fifth_ranked.second_race_id

actual_running_horses.remove(fourth_ranked)
actual_running_horses.remove(fifth_ranked)

to_delete = []

for horse in actual_running_horses:
    if(horse.first_race_id == race_to_delete_fourth):
        if(horse.first_position > pos):
            to_delete.append(horse)
    if(horse.second_race_id == race_to_delete_fourth_2):
        if(horse.second_position > pos_2):
            to_delete.append(horse)

    if(horse.first_race_id == race_to_delete_fifth):
        if(horse.first_position > pos_3):
            to_delete.append(horse)
    if(horse.second_race_id == race_to_delete_fifth_2):
        if(horse.second_position > pos_4):
            to_delete.append(horse)   
    
for horse in to_delete:
    actual_running_horses.remove(horse)

print_rank(actual_running_horses)
