from core.controller import FootballDataController
from time import time, sleep

df = FootballDataController()

def runApp():
  #print('Getting leagues for 2015 year.')
  #df.getLeagues('2015')
  #print('Waiting 60 sec.')
  #sleep(60)
  #print('Getting teams by league.')
  #df.getTeams()
  #print('Waiting 60 sec.')
  #sleep(60)
  #print('Getting squads by team.')
  #df.getSquads()
  df.getFixtures()

if __name__ == '__main__':
  runApp()