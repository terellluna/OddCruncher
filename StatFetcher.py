import statsapi
import BaseballPlayer

class StatFetcher:

    def getPlayerStats(player):
        myPlayer = statsapi.lookup_player(player)
        
        return statsapi.player_stats(myPlayer[0]['id'], 'hitting', 'season')

    def getTeamRoster(team):
        roster = []

        myTeam = statsapi.lookup_team(team)

        teamString = statsapi.roster(myTeam[0]['id'])

        # create dict/enum of mlb teams for lookup
        # use getPlayerStats and array of names to look up stats for entire roster
        # on gameday, use projected pitcher to fetch pitcher data
        # find a way to fetch previous day's game data to determine available releivers

        #turn team string into a list of players
        players = teamString.splitlines()

        for player in players:
            roster.append(BaseballPlayer.BaseballPlayer(player[9:],player[5:7].strip(' ')))

        return roster

team1 = StatFetcher.getTeamRoster('Yankees')
print(StatFetcher.getPlayerStats(team1[0].name))
print(team1[0].position)