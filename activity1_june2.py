import sqlite3
database = 'db_June2.sqlite'
conn = sqlite3.connect(database)
print("Database opend successfully")
import pandas as pd
tables = pd.read_sql('''SELECT * FROM sqlite_master WHERE TYPE = 'table';''', conn)
tables
matches = pd.read_sql('''SELECT * FROM match;''', conn)
matches.info()