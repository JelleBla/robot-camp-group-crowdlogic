import pandas as pd

def solution_station_5(observations):
    teams = pd.read_csv(r'teams.csv')
    teams = pd.DataFrame(teams)

    teamnum = teams[teams.isin([observations]).any(axis=1)]
    return int(teamnum['Team Number'])


#print(solution_station_5('Luca'))