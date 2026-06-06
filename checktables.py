import pandas as pd
import numpy as np
import sqlite3
database = 'db_June6.sqlite'
conn = sqlite3.connect(database)
print("Database opened successfully")
df = pd.read_sql('''SELECT * FROM sqlite_master WHERE TYPE = 'table';''', conn)
print(df)
player_match = pd.read_sql('''SELECT * FROM Player_Match''', conn)
print(player_match.head())
null_player_match = pd.read_sql('''SELECT * FROM Player_Match WHERE Team_Id IS NULL''', conn)
print(null_player_match)
match_table1 = pd.read_sql('''SELECT * FROM match''', conn)
print(match_table1.head())
null_match = pd.read_sql('''SELECT * FROM match WHERE Match_Winner IS NULL''', conn)
print(null_match)