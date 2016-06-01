import logging
from pymongo import MongoClient

log = logging.getLogger('root')

class Database():

  def __init__(self):
    self.mongoHost = 'localhost' # Windows docker toolbox have IP: 192.168.99.100
    self.mongoPort = 27017
    self.client = MongoClient(self.mongoHost, self.mongoPort)
    self.db = self.client['football_data']
    self.collection = None

  def set_collection(self, collection):
    self.collection = self.db[collection]

  def get_one(self, id):
    """

    @deprecated
    :param id:
    :return:
    """
    result = self.collection.find({'id': id})
    return result

  def get_one_new(self, string):
    result = self.collection.find(string)
    return result

  def get_many(self):
    pass

  def update_one(self, data):
    pass

  def insert_one(self, data):
    res = self.collection.insert_one(data)
    if res:
      log.info("[INFO][insert_one] %s" % res.inserted_id)

  def insert_many(self, data):
    self.collection.insert_many(data)