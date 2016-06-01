import time
import requests
import logging

log = logging.getLogger('root')

class FootballData():
  # TODO: Make all API calls with timeouts.

  def __init__(self):
    """

    :return:
    """
    self.server = '''http://api.football-data.org/v1'''
    self.apiKey = '''e5c181096e7944b2af6fbdbe91eadf3b'''
    self.cooldown = 60
    self.maxRPM = 50
    self.timeout = float(self.cooldown / self.maxRPM)

  def set_api_key(self, key):
    """
    Sets API Key
    :param key: String
    :return:
    """
    self.apiKey = key

  def set_server(self, server):
    """
    Sets API Server Url
    :param server: String
    :return:
    """
    self.server = server

  def api_call(self, method=None, *args, **kwargs):
    """
    Makes API Call to football data service.
    :param method: String
    :param args: Arguments
    :param kwargs: Arguments
    :return: JSON data.
    """
    headers = {
      "X-Auth-Token": self.apiKey,
      "X-Response-Control": "full"
    }
    if args:
      for value in args:
        server = "%s/%s" % (self.server, value)

    try:
      time.sleep(self.timeout)
      req = requests.request(method, server, headers=headers)
      if req.status_code == 200:
        return req.text
      else:
        raise (Exception(req.text))
    except Exception as e:
      log.exception(str(e.message))