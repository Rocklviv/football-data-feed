import logging
from core.controller import FootballDataController
from time import time, sleep
from core.logger import LogHandler

log = logging.getLogger('root')
log.setLevel(logging.DEBUG)
log.addHandler(LogHandler())

df = FootballDataController()

def startApplication():
  start = time()
  log.info('Getting leagues for 2015 year.')
  df.getLeagues('2015')
  log.info('Getting teams by league.')
  df.getTeams()
  log.info('Getting squads by team.')
  df.getSquads()
  log.info('Getting fixtures and results.')
  df.getFixtures()
  log.info('---------- Executed after: %s seconds. ----------' % (time() - start))

if __name__ == '__main__':
  startApplication()