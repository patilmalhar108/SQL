import pandas as pd
import numpy as np
import sqlite3
database = 'db_June9.sqlite'
conn = sqlite3.connect(database)
tables = pd.read_sql('''SELECT * FROM sqlite_master WHERE type = 'table';''', conn)
print(tables)
team = pd.read_sql('''SELECT * FROM TEAM''', conn)
print(team)
season = pd.read_sql('''SELECT * FROM SEASON''', conn)
print(season)
csk_matches_2015 = pd.read_sql('''SELECT Match_Id, Team_2 AS Away_Team, Toss_Winner, Match_Winner
FROM match WHERE Team_1 = (SELECT Team_1 FROM match WHERE TEAM_1 == 3 AND Season_Id == 8)''', conn)
print("Matches played by Chennaie Super Kings in year 2015")
print(csk_matches_2015)
csk_wins = pd.read_sql('''SELECT * FROM match WHERE Match_Winner == 3 AND Season_Id == 8''', conn )
print("Matches won by CSK as home team in year 2015")
print(csk_wins)
match_runs = pd.read_sql('''SELECT Match_Id, Runs_Scored AS Total_Runs, Innings_No FROM Batsman_Scored
WHERE Total_Runs > 5 AND Match_Id IN(SELECT Match_Id FROM match WHERE Season_Id == 8)''', conn)
print("Matches with scored runs > 5 in year 2015")
print(match_runs)
average_run = pd.read_sql('''SELECT Match_Id, Runs_Scored AS Total_Runs, Innings_No FROM 
Batsman_Scored WHERE Innings_No == 1 AND Runs_Scored > (SELECT AVG(Runs_Scored) FROM Batsman_Scored)
''', conn)
print("Matches with scored runs > average scored runs")
print(average_run)