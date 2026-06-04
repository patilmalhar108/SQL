import sqlite3
database = 'db_June4.sqlite'
conn = sqlite3.connect(database)
print("Database opened successfully")
import pandas as pd
tables = pd.read_sql('''SELECT * FROM sqlite_master WHERE TYPE = 'table';''', conn)
print(tables)
matches = pd.read_sql('''SELECT * FROM match;''', conn)
matches.head()
result1 = pd.read_sql('''SELECT AVG(Win_Margin), Match_Winner FROM match WHERE Season_Id == 9 GROUP
BY Match_Winner ORDER BY AVG(Win_Margin);''', conn)
print(result1)
result2 = pd.read_sql('''SELECT AVG(Win_Margin), Match_Winner FROM match WHERE Season_Id == 9 GROUP
BY Match_Winner ORDER BY AVG(Win_Margin);''', conn)
print(result2)
result3 = pd.read_sql('''SELECT MIN(Win_Margin), MAX(Win_Margin), AVG(Win_Margin), 
COUNT(DISTINCT(Man_of_the_Match)) FROM match;''', conn)
print(result3)
result4 = pd.read_sql('''SELECT SUM(Win_Margin) FROM match WHERE Season_Id == 9;''', conn)
print(result4)
conn.close()