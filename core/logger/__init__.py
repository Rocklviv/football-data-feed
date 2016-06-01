import logging

class LogHandler(logging.StreamHandler):
  def __init__(self):
    logging.StreamHandler.__init__(self)
    format = '%(asctime)s %(filename)-18s method: %(funcName)s line: %(lineno)-5s %(levelname)-8s: %(message)s'
    format_date = '%Y-%m-%dT%T%Z'
    formatter = logging.Formatter(format, format_date)
    self.setFormatter(formatter)
