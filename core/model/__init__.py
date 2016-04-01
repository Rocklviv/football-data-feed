from core.database import Database

class FootballDataModel(Database):

  def insert_leagues(self):
    self.insert_many()
