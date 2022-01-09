import pandas as pd

# dataset in this code is from cricsheets.org

# create DataFrame
# from a Dictionary
pl_teams = {
    "team": ['Arsenal', 'Chelsea', 'Man Utd', 'Tottenham', 'Liverpool'],
    "stadium": ['Emirates', 'Stamford Bridge', 'Old Trafford', 'White Hart Lane', 'Anfield'],
    "known_as": ['Gunners', 'Blues', 'Red Devils', 'Lilywhites', 'Reds'],
    "captain": ['Lacazette', 'Azpilicueta', 'Maguire', 'Loris', 'Henderson']
}

# create a dataframe with the above dictionary
pl_df = pd.DataFrame(pl_teams)
# head displays the first 5 items in the dataframe
# adding a numeric parameter to head will display that number of records
print(pl_df.head())

# when the df is created we see a column named 'index' has been created.
# this is the row index. by default the index is started at 0
# so last index is df length-1
# we can add a custom index values when creating the DatFrame

# below creates a DF with index as set in the list idx
idx = [100, 101, 102, 103, 104]
new_df = pd.DataFrame(data=pl_teams, index=idx)
# if we just print the df without head/tail then the entire df is printed
print(new_df)
# tail displays the last 5 items
# similar to head, adding a numeric param to tail will display that number of items
# below tail will display last 2 items
pl_df.tail(2)

# to access any column in a df we can access it same way as a dictionary
# this displys all the values of stdium column
print(pl_df['stadium'])

# another way to print the values of a column is with dot notation
# this prints the team column
print(new_df.team)
