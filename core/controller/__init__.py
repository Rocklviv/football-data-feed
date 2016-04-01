import os
import json
from core.system.football_data import FootballData
from core.model import FootballDataModel

class FootballDataController():

  def __init__(self):
    self.dataApi = FootballData()
    self.model = FootballDataModel()


  def getLeagues(self, season):
    leagues = {}
    data = json.loads(self.dataApi.api_call('GET', 'soccerseasons/?season=%s' % season))

    for i in data:
      leagues['league'] = i['league']
      leagues['numberOfMatchdays'] = i['numberOfMatchdays']
      leagues['lastUpdated'] = i['lastUpdated']
      leagues['numberOfGames'] = i['numberOfGames']
      leagues['caption'] = i['caption']
      leagues['currentMatchday'] = i['currentMatchday']
      leagues['year'] = i['year']
      leagues['numberOfTeams'] = i ['numberOfTeams']
      leagues['id'] = i['id']
      self.model.insert_many(leagues)
