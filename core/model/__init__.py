from core.database import Database

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
      if result:
        for v in result:
          if v['lastUpdated'] != i['lastUpdated']:
            self.update_one(i)
          else:
            print('League ID: %s, Name: %s is up to date.' % (i['id'], i['caption']))
      else:
        self.insert_one(i)

  def getLeagueIds(self):
    return self.collection.find()

  def setLeagueTeams(self, data):
    ids = self.get_one(data['id'])
    for i in ids:
      if i['id'] != data['id']:
        result = self.insert_one(data)
        if result:
          return result.inserted_id

  def getTeamsId(self):
    return self.collection.find()

  def setTeamPlayers(self, data):
    ids = self.get_one(data['name'])
    for i in ids:
      if i['name'] != data['name']:
        result = self.insert_one(data)
        if result:
          return result.inserted_id
    else:
      result = self.insert_one(data)
      if result:
        return result.inserted_id