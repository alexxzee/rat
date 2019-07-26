class Menu:

  attaques = [
    'to use a RansomWare',
    'to crawl craiglist',
    'to use keylogger',
    'to set a server',
    'to connect a client to the server',
    'to use Shodan',
    'to use Register',
    'to make a Port Scan',
    'to exit'
  ]

  menu = ""

  def __init__(self):
    for index, words in enumerate(self.attaques):
      self.menu = self.menu + str(index + 1) + '.' + ' Press ' + "'" + str(index + 1) + "' " + words + '.\n'
  
  def _get_menu():
    return self.menu

  
