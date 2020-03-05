import os
import glob
import pandas as pd

##list of all the files in the "games" folder. Glob puts the file in a list from the * wild card on EVE
game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))
game_files.sort()

#reading in each datafile then unioning them all together.
game_frames = []
for game_file in game_files:
    game_frame = pd.read_csv(game_file, names=['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event'])
    game_frames.append(game_frame)

#need to ignore the index to avoid duplicative indices. Games is the df
games = pd.concat(game_frames)


#Cleaning up the data
games.loc[games['multi5'] == '??', 'multi5'] = ''

#finding all valid "game ids, then filling down the game identifier to the next valid game_id"
identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')
identifiers = identifiers.fillna(method='ffill')
identifiers.columns = ["game_id", "year"]

#unioning on identifers with Games to add in valid game ID's.
games = pd.concat([games, identifiers], axis=1, sort=False)
games = games.fillna(' ')

#converting the 'type' column to categorical to reduce memory taken up by data column
games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type'])

if __name__ == '__main__':
    print(games.head())

#for (columnName, columnData) in games.iteritems():
#    print(columnName)
#    print(columnData.unique())