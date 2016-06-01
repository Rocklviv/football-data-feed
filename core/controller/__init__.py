import logging
import json

from core.system.football_data import FootballData
from core.model import FootballDataModel

log = logging.getLogger('root')

class FootballDataController():

  def __init__(self):
    self.dataApi = FootballData()
    self.model = FootballDataModel()


  def getLeagues(self, season):
    """

    :param season:
    :return:
    """
    leaguesToStore = []
    data = json.loads(self.dataApi.api_call('GET', 'soccerseasons/?season=%s' % season))

    for i in data:
      leagues = {}
      leagues['league'] = i['league']
      leagues['numberOfMatchdays'] = i['numberOfMatchdays']
      leagues['lastUpdated'] = i['lastUpdated']
      leagues['numberOfGames'] = i['numberOfGames']
      leagues['caption'] = i['caption']
      leagues['currentMatchday'] = i['currentMatchday']
      leagues['year'] = i['year']
      leagues['numberOfTeams'] = i ['numberOfTeams']
      leagues['id'] = i['id']
      leaguesToStore.append(leagues)

    self.model.setCollection('leagues')
    self.model.insert_leagues(leaguesToStore)

  def getTeams(self):
    data = {}
    self.model.setCollection('leagues')
    result = self.model.getLeagueIds()
    for i in result:
      data = json.loads(self.dataApi.api_call('GET', 'soccerseasons/%s/teams?season=2015' % i['id']))
      self.__process_teams(i['id'], data)


  def getSquads(self):
    """

    :return:
    """
    self.model.setCollection('teams')
    result = self.model.getTeamsId()
    for i in result:
      data = json.loads(self.dataApi.api_call('GET', 'teams/%s/players' % i['id']))
      self.__process_squads(i['id'], data)

  def getFixtures(self):
    self.model.setCollection('leagues')
    result = self.model.getLeagueIds()
    for i in result:
      data = json.loads(self.dataApi.api_call('GET', 'soccerseasons/%s/fixtures?season=2015' % i['id']))
      self.__process_fixtures(i['id'], data)
      self.__process_results(data)

  def getTeamById(self):
    """
    Debugging function
    :return:
    """
    self.model.setCollection('teams')
    result = self.model.get_one(254)
    for i in result:
      print(i)

  def __process_teams(self, league_id, data):
    """

    :param league_id: Id of league.
    :param data: League data
    :return:
    """
    self.model.setCollection('teams')
    pattern = 'http://api.football-data.org/v1/teams/'
    teamsList = []

    for i in data['teams']:
      teams = {}
      teams['id'] = int(i['_links']['self']['href'].replace(pattern, ''))
      teams['league_id'] = league_id
      teams['name'] = i['name']
      teams['code'] = i['code']
      teams['shortName'] = i['shortName']
      teams['squadMarketValue'] = i['squadMarketValue']
      teams['crestUrl'] = i['crestUrl']
      teamsList.append(teams)

    self.model.setLeagueTeams(teamsList)


  def __process_squads(self, team_id, data):
    """

    :param team_id:
    :param data:
    :return:
    """
    self.model.setCollection('squads')
    squadsList = []

    for i in data['players']:
      players = {}
      players['team_id'] = team_id
      players['name'] = i['name']
      players['position'] = i['position']
      players['jerseyNumber'] = i['jerseyNumber']
      players['dateOfBirth'] = i['dateOfBirth']
      players['nationality'] = i['nationality']
      players['contractUntil'] = i['contractUntil']
      players['marketValue'] = i['marketValue']
      squadsList.append(players)
    self.model.setTeamPlayers(squadsList)


  def __process_fixtures(self, league_id, data):
    self.model.setCollection('fixtures')
    fix_id_pattern = 'http://api.football-data.org/v1/fixtures/'
    team_id_pattern = 'http://api.football-data.org/v1/teams/'

    for i in data['fixtures']:
      fixtures = {}
      fixtures['league_id'] = league_id
      fixtures['id'] = int(i['_links']['self']['href'].replace(fix_id_pattern, ''))
      fixtures['date'] = i['date']
      fixtures['status'] = i['status']
      fixtures['matchday'] = i['matchday']
      fixtures['homeTeamName'] = i['homeTeamName']
      fixtures['homeTeamId'] = int(i['_links']['homeTeam']['href'].replace(team_id_pattern, ''))
      fixtures['awayTeamName'] = i['awayTeamName']
      fixtures['awayTeamId'] = int(i['_links']['awayTeam']['href'].replace(team_id_pattern, ''))
      self.model.setLeagueFixtures(fixtures)


  def __process_results(self, data):
    self.model.setCollection('fixture_results')
    fix_id_pattern = 'http://api.football-data.org/v1/fixtures/'

    for i in data['fixtures']:
      results = {}
      results['id'] = int(i['_links']['self']['href'].replace(fix_id_pattern, ''))
      results['result'] = i['result']
      self.model.setLeagueResults(results)