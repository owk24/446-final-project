import time
import pandas as pd
# NOTE DO NOT RUN THIS, it will take roughly 3-4 hours to complete
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

from nba_api.stats.endpoints import shotchartdetail, CommonAllPlayers

seasonsToQuery = ["2018-19"]
columnHeaders = ["GRID_TYPE", "GAME_ID", "GAME_EVENT_ID", "PLAYER_ID", "PLAYER_NAME", "TEAM_ID", "TEAM_NAME",
                 "PERIOD", "MINUTES_REMAINING", "SECONDS_REMAINING", "EVENT_TYPE", "ACTION_TYPE", "SHOT_TYPE",
                 "SHOT_ZONE_BASIC" ,"SHOT_ZONE_AREA", "SHOT_ZONE_RANGE", "SHOT_DISTANCE", "LOC_X", "LOC_Y",
                 "SHOT_ATTEMPTED_FLAG", "SHOT_MADE_FLAG", "GAME_DATE", "HTM", "VTM"]


playersInfo = CommonAllPlayers(is_only_current_season=0).get_data_frames()[0]
playersAfter2018 = playersInfo[(playersInfo.TO_YEAR >= "2018") & (playersInfo.GAMES_PLAYED_FLAG == "Y")]
playerAfter2018Ids = playersAfter2018["PERSON_ID"]

dataFrameWithAllShootingStats = pd.DataFrame(columns=columnHeaders)

def GetPlayerShootingStats(season, playerID):
    time.sleep(3) # to avoid TIMEOUTs from the endpoint
    try:
        shotChartDetails = shotchartdetail.ShotChartDetail \
            (player_id=playerID, team_id=0, season_nullable=season, context_measure_simple='FGA').get_data_frames()
    except:
        return pd.DataFrame(columns=columnHeaders)

    return shotChartDetails[0]

for season in seasonsToQuery:
    for playerId in playerAfter2018Ids:
        dataFrameWithAllShootingStatsForAPlayerInASeason = GetPlayerShootingStats(season, playerId)
        dataFrameWithAllShootingStats = pd.concat([dataFrameWithAllShootingStats, dataFrameWithAllShootingStatsForAPlayerInASeason], axis=0)
        print(dataFrameWithAllShootingStats)

dataFrameWithAllShootingStats.to_csv('Data/shootingSets2019-2020.csv', index=False, header=True)
