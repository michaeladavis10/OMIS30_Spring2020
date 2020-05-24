# This is a script to test monty hall problem
# author: midavis
# date: 2019-10-19

import random
import pandas as pd
import matplotlib.pyplot as plt
import io

# Get number of doors you want to play with
# n = int(input('How many doors do you want to play the Monty Hall game with?: '))
# switch_strategy = input('What do you want your switch strategy to be? "switch" or "stay": ')
# m = int(input('How many times do you want to play this game?'))

# play the game with 3 doors up to 10
# at each n, play once with switch and once with stay
# at each switch/stay, play m times - m = 10, 100, 1000, 10000
num_doors_power = 5
num_trials_power = 8
switch_strategy = 'switch'

def generateGameData(num_doors_power, num_trials_power, switch_strategy):

    # if num_doors_power > 10:
    
    # else:

    # if num_trials_power > 10:
    # num_doors = [3] + [ 2**x for x in range(2, num_doors_power + 1) ]
    # num_trials = [ 2**x for x in range(1, num_trials_power + 1) ]
    num_doors = list( range(3,num_doors_power+1,1) )
    num_trials = [ 2**x for x in range(1, num_trials_power + 1) ]

    results = list()
    for n in num_doors:

        # for switch_strategy in ['switch', 'stay']:

        for m in num_trials:

            # start counting how many times you won
            num_wins = 0

            for x in range(m):

                ## Set up the game
                # set up n doors
                # get a random number and determine which door holds the prize
                doors = list( range(1, n + 1, 1) )
                winner_door = random.choice(doors)

                # pick 'your' door
                # doens't really matter so just do random input
                a = random.choice(doors)

                # remove the door they chose
                # after this step, they should only have n-1 
                doors2 = doors.copy()
                doors2.remove(a)

                # there are now n-1 doors
                if a == winner_door: 
                    # randomly choose n-2 out of the n-1 remaining doors
                    pass
                else:
                    # remove the winning door, and then show all of them
                    doors2.remove(winner_door)

                # choose n-2 doors out of remaining doors
                dud_doors_to_open = random.sample(doors2, n - 2)

                # list remaining doors
                # put them in a set
                # put the winning door, user-chosen door, and the remaining_door back into a final group
                # that way you always have 2 doors left
                remaining_doors = set(doors2) - set(dud_doors_to_open)
                remaining_doors.add(winner_door)
                remaining_doors.add(a)

                # figure out the door to switch to
                switch_to_doors = list(remaining_doors)
                switch_to_doors.remove(a)
                switch_to_door = switch_to_doors[0]

                # ask the user if they want to switch
                # print(remaining_doors)
                # print('You currently picked door # ' + str(a) )
                # print('Do you want to switch to door # ' + str(switch_to_door) + '?')

                # determine final door based off answer
                if switch_strategy == 'switch':
                    final_door = switch_to_door
                elif switch_strategy == 'stay':
                    final_door = a
                else:
                    print('you messed up')
                    quit()

                # determine if final door is winner
                if final_door == winner_door:
                    # print('You won!')
                    num_wins += 1
                else:
                    # print('You lost :-(')
                    pass

            # save results
            mini_result = dict()
            mini_result['num_doors'] = n
            mini_result['num_runs'] = m
            mini_result['strategy'] = switch_strategy
            mini_result['num_wins'] = num_wins
            results.append(mini_result)



    mydf = pd.DataFrame(results)
    mydf['switch'] = mydf['num_wins'] * 100.0 / mydf['num_runs']
    mydf['stay'] = 100.0 - mydf['switch']
    mydf = mydf.drop(['num_wins','strategy'], axis = 1)
    mydf = mydf.set_index(['num_doors', 'num_runs'])
    return mydf


def plot_clustered_stacked(axe, dfall, labels = None, title = "multiple stacked bar plot",  H = "/", true_pct = 0, **kwargs):
    """Given a list of dataframes, with identical columns and index, create a clustered stacked bar plot. 
        labels is a list of the names of the dataframe, used for the legend title is a string for the title of the plot
        H is the hatch used for identification of the different dataframe"""

    n_df = len(dfall)
    n_col = len(dfall[0].columns) 
    n_ind = len(dfall[0].index)

    for df in dfall : # for each data frame
        axe = df.plot(kind = "bar", linewidth = 0, stacked = True, ax = axe, legend = False, grid = False, **kwargs)  # make bar plots

    h,l = axe.get_legend_handles_labels() # get the handles we want to modify
    for i in range(0, n_df * n_col, n_col): # len(h) = n_col * n_df
        for j, pa in enumerate( h[i:i+n_col] ):
            for rect in pa.patches: # for each index
                rect.set_x( rect.get_x() + 1 / float(n_df + 1) * i / float(n_col) )
                rect.set_hatch( H * int(i / n_col) ) #edited part     
                rect.set_width( 1 / float(n_df + 1) )

    # Add horizontal line for diamond as % of total bookings
    axe.axhline(y = true_pct, linestyle = ':', color = 'black')
    axhline_annotation = str( round(true_pct, 1)) + '%'
    axe.text(-0.25, true_pct + 0.5, axhline_annotation, fontsize = 6, ha = 'left', color = 'black')
    
    increment = 0.05
    # Add x ticks
    axe.set_xbound( -0.30, rect.get_x() + 2 / float(n_df + 1) )
    # axe.set_xticks( (np.arange(-0.25, 0.625, 0.125) ) , minor = True )
    axe.set_xlabel('')
    axe.set_xticklabels('')
    axe.set_ylabel('Win Percentage')
    axe.set_title(title)

    # Add invisible data to add another legend
    n=[]        
    for i in range(n_df):
        n.append(axe.bar(0, 0, color="grey", hatch=H * i))

    if labels is not None:
        l1 = plt.legend(h[:n_col], l[:n_col], loc=[1.01, 0.7], title = 'Strategy')
        l2 = plt.legend(n, labels, loc=[1.01, 0.1], title = 'Num Trials') 
        plt.gca().add_artist(l1)

    return axe


def plotThings(mydf):

    # Figure out the dimensions
    graph_rows = [1]
    graph_cols = sorted( list( mydf.index.get_level_values('num_doors').unique() ) )
    box_cols = sorted( list( mydf.index.get_level_values('num_runs').unique() ) )

    # Start plotting
    plt.close('all')
    fig, axes = plt.subplots(nrows = len(graph_rows), ncols = len(graph_cols), sharex = True, sharey = 'row', figsize = (10, 10) )

    # Switch this based off the values
    if len(graph_rows) == 1 and len(graph_cols) == 1:
        axes_list = [axes]
    elif len(graph_rows) == 1 or len(graph_cols) == 1:
        axes_list = [item for item in axes]
    else:
        axes_list = [item for sublist in axes for item in sublist] 

     # Make a separate df for each set of num_trials for matplotlib groups
    for doors in graph_cols:
        df_dict = {}
        for trials in box_cols:
            # subset the data
            mydf2 = mydf.copy()
            d = mydf2.loc [ (mydf2.index.get_level_values('num_doors') == doors) & (mydf2.index.get_level_values('num_runs') == trials) ]
            df_dict[trials] = d 
            d2 = d.reset_index(drop = False)
            true_pct = 100.0 - (100.0 / d2['num_doors'][0])

        # Plot
        ax = axes_list.pop(0)
        plot_clustered_stacked(ax, 
            list( df_dict.values() ), 
            list( df_dict.keys() ), 
            title = 'Doors = ' + str(doors), 
            H = '/', 
            true_pct = true_pct
            )

    # plt.show()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    plt.close()
    bytes_image.seek(0)
    return bytes_image

# plotThings(mydf)