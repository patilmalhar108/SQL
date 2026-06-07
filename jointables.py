import sqlite3
import pandas as pd
import numpy as np
database = 'db_June7.sqlite'
conn = sqlite3.connect(database)
tables = pd.read_sql('''SELECT * FROM sqlite_master WHERE TYPE = 'table';''', conn)
print(tables)

join_city = pd.read_sql('''SELECT c.Country_Id, c.Country_Name, ci.City_Name FROM country c INNER
JOIN city ci ON c.Country_Id == ci.Country_Id''', conn)
print(join_city)

joined_left = pd.read_sql('''SELECT * FROM player LEFT JOIN season ON player.Player_Id == 
season.Man_of_the_Series''', conn)
print(joined_left)

joined_cross = pd.read_sql('''SELECT c.Country_Id, c.Country_Name, ci.City_Name FROM country c CROSS
JOIN city ci''', conn)
print(joined_cross)

players = pd.read_sql("""
SELECT Player_Name
FROM player
""", conn)
print(players.head())

teams = pd.read_sql("""
SELECT Team_Name
FROM team
""", conn)

union = pd.read_sql('''SELECT Player_Name FROM player UNION Team_Name FROM team''', conn)
print(union)