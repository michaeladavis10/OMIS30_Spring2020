# ##################
# author: midavis
# date: 2020-05-23
#
# OMIS 30
# World Population Prep Homework
# #####################################

#### Objective ####
## Bring the list into python
## Shuffle the order of the list

#### Strategy #####
## Import the list and random libraries
## Create a new blank list
## Randomly select one element from the list and put it in a new list
## Repeat until all elements gone - requires previous step to be without replacement
## Save the new order as the new list
## Do this the hard, slow way first

import pandas as pd
import random

world_pop = pd.read_csv('/Users/mdavis/dev/OMIS30_Spring2020/world_pop/world_pop.csv')
world_pop_list = []
for row in world_pop.values:
    world_pop_list.append(list(row))

## Create a new blank list
randomized_world_pop_list = list()

## Randomly select one element from the list and put it in a new list, then remove it from the original list
## Repeat until all elements gone - requires previous step to be without replacement
while len(world_pop_list) > 0:
    rand_num = random.randint(0, len(world_pop_list) - 1)
    element_to_move = world_pop_list[rand_num]
    randomized_world_pop_list.append( element_to_move )
    world_pop_list.remove( element_to_move )

## Save the new order as the new list
world_pop_list = randomized_world_pop_list
import pprint
pprint.pprint(world_pop_list)

## The easy way would have been just do
# random.shuffle(world_population)

# Export to CSV
world_pop_df = pd.DataFrame(world_pop_list, columns = ['Country','Continent','Population'])
world_pop_df.to_csv('/Users/mdavis/dev/OMIS30_Spring2020/world_pop/world_pop.csv', index = False)
