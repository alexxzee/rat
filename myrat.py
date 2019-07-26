import os
import os.path
from os import listdir
from os.path import isfile, join
import time

from tools import Menu

from crawler import craigList
from keylogger import keylogger
from clientServer import client, server
from ransom import ransomeware
from myshodan import shodanscript
from register import register
from scanPort import scanPort


def clear(): return os.system('cls')

menu = Menu.Menu().menu

choice = int(input(menu))

clear()
if choice == 1:
  ransomeware.main()
elif choice == 2:
  craigList.main()
elif choice == 3:
  keylogger.main()
elif choice == 4:
  server.main()
elif choice == 5:
  client.main()
elif choice == 6:
  shodanscript.main()
elif choice == 7:
  register.main()
elif choice == 8:
  scanPort.main()
elif choice == 9:
    exit()
else:
    print("Please select a valid option!")