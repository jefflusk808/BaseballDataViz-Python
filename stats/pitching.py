import pandas as pd
import matplotlib.pyplot as plt
from data import games

#creating new df with only the play data lines, filtering with explicit criterion
plays = games[games.type == 'play']


#finding all the plays that have the event of K, filtering with a contains function
strike_outs = plays[plays['event'].str.contains('K')]
strike_outs = strike_outs.groupby(['year', 'game_id']).size()

strike_outs = strike_outs.reset_index(name='strike_outs')

#converting the year and strike_outs columns to numeric
strike_outs = strike_outs.loc[:, ['year', 'strike_outs']].apply(pd.to_numeric)

#configuring the plot parameters of the df and showing the it
strike_outs.plot(x='year'
                 , y='strike_outs'
                 , kind='scatter'
                 , title='Strikeouts by Year'
                 ).legend(['Strike Outs'])

plt.xlabel('Year')
plt.ylabel('Strike Outs')


plt.show()