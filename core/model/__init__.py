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
      if result.count() == 1:
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
    for i in data:
      result = self.get_one(i['id'])
      if result.count() == 0:
        self.insert_one(i)
      else:
        print('Team ID: %s NAME: %s is already in base.' % (i['id'], i['name']))


  def getTeamsId(self):
    return self.collection.find()


  def setTeamPlayers(self, data):
    for i in data:
      field = {'name': i['name']}
      result = self.get_one_new(field)
      print('Was found: %s' % result.count())
      if result.count() == 0:
        self.insert_one(i)
      else:
        for v in result:
          if v['name'] == i['name']:
            print('Player %s from Team: %s is already in database.' % (i['name'], i['team_id']))
          else:
            self.update_one(i)


  def setLeagueFixtures(self, data):
    ids = self.get_one(data['id'])
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
    ids = self.get_one(data['id'])
    print(ids)
    # if ids:
    #   for i in ids:
    #     if i['id'] != data['id']:
    #       result = self.insert_one(data)
    #       return result.inserted_id
    # else:
    #   result = self.insert_one(data)
    #   print(result, data['id'])
    #   return result