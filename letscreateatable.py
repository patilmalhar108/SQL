import sqlite3
conn = sqlite3.connect('db_June6.sqlite')
print("Opened data base successfully")
conn.execute('''CREATE TABLE class_10(
            SNO INT PRIMARY KEY NOT NULL, 
            NAME TEXT NOT NULL,
            AGE INT DEFAULT(15),
            GENDER TEXT NOT NULL,
            EMAIL_ID TEXT NOT NULL,
            CONTACT_NUM REAL NOT NULL
             );''')
print("Table created successfully")
conn.execute("Insert into class_10(SNO, NAME, AGE, GENDER, EMAIL_ID, CONTACT_NUM) VALUES(1, 'JOHN'," \
"14, 'MALE', 'JOHN@GMAIL.COM',6302259100 )");
conn.execute("Insert into class_10(SNO, NAME, AGE, GENDER, EMAIL_ID, CONTACT_NUM) VALUES(2, 'JACK'," \
"16, 'MALE', 'JACK@GMAIL.COM',8472196667 )");
conn.execute("Insert into class_10(SNO, NAME, AGE, GENDER, EMAIL_ID, CONTACT_NUM) VALUES(3, 'JANE'," \
"15, 'FEMALE', 'JANE@GMAIL.COM',2248871256 )");
conn.commit()
import pandas as pd
tables = pd.read_sql('''SELECT * FROM sqlite_master WHERE TYPE = 'table';''', conn)
print(tables)
class_10_a = pd.read_sql('''SELECT * FROM class_10;''', conn)
print(class_10_a.head())