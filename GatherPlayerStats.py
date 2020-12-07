import time
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

from nba_api.stats.endpoints import CommonAllPlayers, PlayerDashboardByYearOverYear
from nba_api.stats.static import players

seasonsToQuery = ["2018-19"]
columnHeaders = ['GROUP_SET', 'GROUP_VALUE', 'TEAM_ID', 'TEAM_ABBREVIATION',
                   'MAX_GAME_DATE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT',
                   'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB',
                   'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS',
                   'PLUS_MINUS', 'NBA_FANTASY_PTS', 'DD2', 'TD3', 'GP_RANK', 'W_RANK',
                   'L_RANK', 'W_PCT_RANK', 'MIN_RANK', 'FGM_RANK', 'FGA_RANK',
                   'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'FTM_RANK',
                   'FTA_RANK', 'FT_PCT_RANK', 'OREB_RANK', 'DREB_RANK', 'REB_RANK',
                   'AST_RANK', 'TOV_RANK', 'STL_RANK', 'BLK_RANK', 'BLKA_RANK', 'PF_RANK',
                   'PFD_RANK', 'PTS_RANK', 'PLUS_MINUS_RANK', 'NBA_FANTASY_PTS_RANK',
                   'DD2_RANK', 'TD3_RANK', 'CFID', 'CFPARAMS', 'PLAYER_NAME']

playersInfo = CommonAllPlayers(is_only_current_season=0).get_data_frames()[0]
playersAfter2018 = playersInfo[(playersInfo.TO_YEAR >= "2018") & (playersInfo.GAMES_PLAYED_FLAG == "Y")]
playersAfter2018Ids = playersAfter2018["PERSON_ID"]

dataFrameWithAllPlayersStats = pd.DataFrame(columns=columnHeaders)

# for test in playersAfter2018Ids[:2]:
#     print(players.find_player_by_id(test)["full_name"])
# print(players.find_player_by_id(playersAfter2018Ids))
# playerDash = PlayerDashboardByYearOverYear(player_id="2544", season="2018-19").get_data_frames()
# print(playerDash[0].columns)


def GetPlayerDash(playerID):
    time.sleep(1) # to avoid TIMEOUTs from the endpoint
    try:
        playerDashDetails = PlayerDashboardByYearOverYear \
            (player_id=playerID, season="2018-19").get_data_frames()
        playerName = players.find_player_by_id(playerID)["full_name"]
        playerDashDetails[0]['PLAYER_NAME'] = playerName
    except:
        return pd.DataFrame(columns=columnHeaders)

    return playerDashDetails[0]
#
for playerId in playersAfter2018Ids:
    dataFrameWithPlayerStats = GetPlayerDash(playerId)
    dataFrameWithAllPlayersStats = pd.concat([dataFrameWithAllPlayersStats, dataFrameWithPlayerStats], axis=0)
    print(dataFrameWithAllPlayersStats)

dataFrameWithAllPlayersStats.to_csv('Data/PlayersStats.csv', index=False, header=True)
