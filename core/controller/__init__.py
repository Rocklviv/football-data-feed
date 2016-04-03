import os
import json
from platform import platform
from time import sleep

from core.system.football_data import FootballData
from core.model import FootballDataModel

class FootballDataController():

  def __init__(self):
    self.dataApi = FootballData()
    self.model = FootballDataModel()


  def getLeagues(self, season):
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
    data = {}
    count = 0
    self.model.setCollection('teams')
    result = self.model.getTeamsId()
    for i in result:
      count += 1
      if count == 30:
        sleep(60)
        print('Squads: Waiting 60 sec due to %s requests overdue.' % count)
        data = json.loads(self.dataApi.api_call('GET', 'teams/%s/players' % i['id']))
        count = 0
      else:
        data = json.loads(self.dataApi.api_call('GET', 'teams/%s/players' % i['id']))
      self.__process_squads(i['id'], data)

  def __process_teams(self, league_id, data):
    """

    :param league_id: Id of league.
    :param data: League data
    :return:
    """
    self.model.setCollection('teams')
    pattern = 'http://api.football-data.org/v1/teams/'

    for i in data['teams']:
      teams = {}
      teams['id'] = int(i['_links']['self']['href'].replace(pattern, ''))
      teams['league_id'] = league_id
      teams['name'] = i['name']
      teams['code'] = i['code']
      teams['shortName'] = i['shortName']
      teams['squadMarketValue'] = i['squadMarketValue']
      teams['crestUrl'] = i['crestUrl']
      self.model.setLeagueTeams(teams)


  def __process_squads(self, team_id, data):
    self.model.setCollection('squads')

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
      self.model.setTeamPlayers(players)
