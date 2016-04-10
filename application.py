from core.controller import FootballDataController
from time import time, sleep

df = FootballDataController()

def runApp():
  start = time()
  print('Getting leagues for 2015 year.')
  df.getLeagues('2015')
  print('Getting teams by league.')
  df.getTeams()
  print('Getting squads by team.')
  df.getSquads()
  df.getFixtures()
  print ('---------- Executed after: %s seconds. ----------' % (time() - start))

if __name__ == '__main__':
  runApp()