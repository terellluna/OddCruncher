import statsapi

class StatFetcher:

    def getPlayerStats(player):
        myPlayer = statsapi.lookup_player(player)
        
        return statsapi.player_stats(myPlayer[0]['id'], 'hitting', 'season')

    def getTeamRoster(team):
        myTeam = statsapi.lookup_team(team)

        teamString = statsapi.roster(myTeam[0]['id'])

        #for team in myTeam:
        #    print(team)

        # will have to parse the text to return individual player names
        # create array for home/away team based on player names
        # create dict/enum of mlb teams for lookup
        # use getPlayerStats and array of names to look up stats for entire roster
        # on gameday, use projected pitcher to fetch pitcher data
        # find a way to fetch previous day's game data to determine available releivers

        #turn team string into a list of players
        players = teamString.splitlines()

        for player in players:
            players[players.index(player)] = player[9:]

        return players

team1 = StatFetcher.getTeamRoster('Yankees')
print(StatFetcher.getPlayerStats(team1[0]))
#print(StatFetcher.getTeamRoster('White Sox'))