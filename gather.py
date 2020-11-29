from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.static import players, teams
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

player_info = players.find_players_by_full_name("Stephen Curry")
player_id = player_info[0]['id']
'''201939 for Steph Curry'''
# print(player_id)

team_info = teams.find_team_by_abbreviation("gsw")
team_id = team_info['id']
''' 1610612744 for gsw'''
# print(team_id)

shotChartDetails = shotchartdetail.ShotChartDetail \
    (player_id=player_id, team_id=team_id, context_measure_simple='FGA').get_data_frames()

shotChartDetailsCount = 0
for dataFrame in shotChartDetails:
    dataFrame.to_csv('Data/ShotChartDetails{}.csv'.format(shotChartDetailsCount), index=False, header=True)
    shotChartDetailsCount += 1
