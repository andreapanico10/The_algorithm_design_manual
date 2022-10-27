'''There are twenty-five horses. 
At most, five horses can race together at a time. 
You must determine the fastest, second fastest, and third fastest horses.
Find the minimum number of races in which this can be done.

ANDREA_PANICO_note: It's considered only a comparison between horses, not a time rank.
'''

'''


Soluzione 2 
5 corse di base -> Rimangono 15/25
corsa 6 Prendo tutti i primi -> eleggo i primi 3, elimino gli ultimi 2
Dai due eliminati è inutile prendere secondi e terzi perchè sono più lenti dei primi e 
quindi rimangono 9 cavalli (di cui già 3 ordinati)


corsa 7 Faccio corsa tra 2-3 della corsa 6 e i tre secondi rimasti -> 
5 ORDINATI e ne elimino 3 -> rimangono 6 cavalli

corsa 8 -> corrono gli ultimi 5 cavalli (è salvo solo il primo) -> okay 

'''
import numpy as np
import random
from itertools import islice

horses_names = list(map(str,np.arange(1,26)))
horses_times = np.round(np.random.random_sample(size = len(horses_names)),3)

horses = {}
actual_running_horses = {}
first_ranked = {}
second_ranked = {}
third_ranked = {}

for i in range (len(horses_names)):
    horses[horses_names[i]] = horses_times[i]

race_id = 0
for race in range(5): # 5 Starting race
    start = race_id*5 
    end = (race_id+1)*5
    horses_race_battery = list(horses.keys())
    battery = {k: horses[k] for k in list(horses)[start:end]}
    battery = sorted(battery.items(), key=lambda x:x[1]) # is a list
    battery = dict(battery) # convert again in dict

    first_three_winners = {k: battery[k] for k in list(battery)[:3]}

    actual_running_horses.update(first_three_winners)

    i = 0
    for k, v in first_three_winners.items():
        temp = {k:v}
        if(i==0):
            first_ranked.update(temp)
        if(i==1):
            second_ranked.update(temp)
        if(i==2):
            third_ranked.update(temp)
        i += 1
    race_id += 1


##### RACE # 6 #######
# Between all the first ranked #

first_ranked_list = sorted(first_ranked.items(), key=lambda x:x[1]) # is a list
first_ranked = dict(first_ranked_list) # convert again in dict

del actual_running_horses[first_ranked_list[-2][0]]
del actual_running_horses[first_ranked_list[-1][0]]
first_ranked_2_3 = {k: first_ranked[k] for k in list(first_ranked)[1:3]}

print(second_ranked)
