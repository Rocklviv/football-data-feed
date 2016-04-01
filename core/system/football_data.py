import requests

class FootballData():

  def __init__(self):
    """

    :return:
    """
    self.server = '''http://api.football-data.org/v1'''
    self.apiKey = '''3c11ec48825a43998874d5b2388f0030'''

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
        self.server = "%s/%s" % (self.server, value)

    try:
      if method == "POST":
        req = requests.post(self.server, headers)
      else:
        req = requests.get(self.server, headers)
      if req.status_code == 200:
        return req.text
      else:
        raise (Exception(req.text))
    except Exception as e:
      print(str(e.message))