import statsapi
import BaseballPlayer
import BaseballStats

class StatFetcher:

    # returns the stats for the first player found given a player name
    def getPlayerSeasonStats(player):
        myPlayer = statsapi.lookup_player(player)
        stats = BaseballStats.BaseballStats(statsapi.player_stats(myPlayer[0]['id'], 'hitting', 'season'),statsapi.player_stats(myPlayer[0]['id'], 'pitching', 'season'),statsapi.player_stats(myPlayer[0]['id'], 'fielding', 'season'))
        
        return stats

    def getPlayerCareerStats(player):
        myPlayer = statsapi.lookup_player(player)
        stats = BaseballStats.BaseballStats(statsapi.player_stats(myPlayer[0]['id'], 'hitting', 'career'),statsapi.player_stats(myPlayer[0]['id'], 'pitching', 'career'),statsapi.player_stats(myPlayer[0]['id'], 'fielding', 'career'))
        
        return stats

    # returns a list of player's names, their position, and their stats
    def getTeamRoster(team):
        roster = []

        searchedTeam = statsapi.lookup_team(team)

        teamRosterAsString = statsapi.roster(searchedTeam[0]['id'])

        players = teamRosterAsString.splitlines()

        # for each player, add that player's name, player's positon, and player's stats to the roster
        for player in players:
            roster.append(BaseballPlayer.BaseballPlayer(player[9:],player[5:7].strip(' '),StatFetcher.getPlayerSeasonStats(player[9:])))

        return roster

team1 = StatFetcher.getTeamRoster('Yankees')
print(team1[0].stats.fielding)
