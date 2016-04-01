from pymongo import MongoClient

class Database():

  def __init__(self):
    self.mongoHost = '192.168.99.100' # Windows docker toolbox have IP: 192.168.99.100
    self.mongoPort = 27017
    self.client = MongoClient(self.mongoHost, self.mongoPort)
    self.db = self.client['football_data']

  def set_collection(self, collection):
    self.collection = self.db[collection]

  def get_one(self, id):
    result = self.collection.find({'id': id})
    return result

  def get_many(self):
    pass

  def update_one(self, data):
    pass

  def insert_one(self):
    pass

  def insert_many(self, data):
    try:
      if self.get_one(data['id']):
        self.update_one(data)
      else:
        print(data)
    except Exception as e:
      print(str(e))
