encode = 'UTF-8'


def parseCommand( command ):
  return str(command).encode()

def displayData( data ):
  print(data.decode(encode))