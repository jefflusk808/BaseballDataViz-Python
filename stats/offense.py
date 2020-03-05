import pandas as pd
import matplotlib.pyplot as plt
from data import games

#creating the plays dataframe and renaming the columns
plays = games[games.type == 'play']
plays.columns = ["type", "inning", "team", "player", "count", "pitches", "event", "game_id", "year"]


#filtering the data set to just data that shows "hits"
hits = plays.loc[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)'), ['inning', 'event']]

#converting innings column to numeric data
hits.loc[:, 'inning'] = pd.to_numeric(hits.loc[:, 'inning'])

#dictionary to create consistent buckets
replacements = {
                r'^S(.*)': 'single'
                , r'^D(.*)': 'double'
                , r'^T(.*)': 'triple'
                , r'^HR(.*)': 'hr'
            }

#creating dataframe of cleansed event types
hit_type = hits['event'].replace(replacements, regex=True)

#assins new column to the hits df, since the indexs are the same it lines up.
hits = hits.assign(hit_type=hit_type)

#example of chaining methods on one line.
hits = hits.groupby(['inning', 'hit_type']).size().reset_index(name='count')

#changing the hit_type to categorical to reduce memory size, passing it the second arg gives order to the items
hits['hit_type'] = pd.Categorical(hits['hit_type'], ['single', 'double', 'triple', 'hr'])

#sorting the df by inning and hit_type
hits = hits.sort_values(['inning', 'hit_type'])

#pivoting the df to be able to plot
hits = hits.pivot(index='inning', columns='hit_type', values='count')

hits.plot.bar(stacked=True)

plt.show()

print(hits.head(n=15))
print(hits.dtypes)