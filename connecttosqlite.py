import sqlite3
database = 'database1.sqlite'
conn = sqlite3.connect(database)
print("Opened database succesfully")
import pandas as pd
tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE TYPE = 'table';""", conn)
print(tables)