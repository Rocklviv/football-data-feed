import logging
from core.database import Database

log = logging.getLogger('root')

class FootballDataModel(Database):

  def setCollection(self, collection):
    self.set_collection(collection)

  def insert_leagues(self, data):
    """

    :param data:
    :return:
    """
    for i in data:
      result = self.get_one(i['id'])
      if result.count() == 1:
        for v in result:
          if v['lastUpdated'] != i['lastUpdated']:
            self.update_one(v['_id'], i)
          else:
            log.info('League ID: %s, Name: %s is up to date.' % (i['id'], i['caption']))
      else:
        self.insert_one(i)

  def getLeagueIds(self):
    return self.collection.find()


  def setLeagueTeams(self, data):
    for i in data:
      result = self.get_one(i['id'])
      if result.count() == 0:
        self.insert_one(i)
      else:
        log.info('Team ID: %s NAME: %s is already in base.' % (i['id'], i['name']))


  def getTeamsId(self):
    return self.collection.find()


  def setTeamPlayers(self, data):
    """

    :param data:
    :return:
    """
    for i in data:
      field = {'name': i['name']}
      result = self.get_one_new(field)
      log.info('Player was found: %s' % result.count())
      if result.count() == 0:
        self.insert_one(i)
      else:
        for v in result:
          if v['name'] == i['name']:
            if v['team_id'] == i['team_id']:
              log.info('Player %s from Team: %s is already in database.' % (i['name'], i['team_id']))
            else:
              log.info('Updating player %s info because of transfer to another team %s' % (v['name'], i['team_id']))
              self.update_one(v['_id'], i)


  def setLeagueFixtures(self, data):
    """

    :param data:
    :return:
    """
    ids = self.get_one(data['id'])
    if ids.count() != 0:
      for i in ids:
        if i['id'] != data['id']:
          result = self.insert_one(data)
          if result:
            return result.inserted_id
    else:
      result = self.insert_one(data)
      if result:
        return result.inserted_id


  def setLeagueResults(self, data):
    """

    :param data:
    :return:
    """
    ids = self.get_one(data['id'])
    if ids.count() != 0:
      for i in ids:
        if i['id'] == data['id']:
          log.info("Result of fixture %s already in database." % i['id'])
    else:
      result = self.insert_one(data)
      return result