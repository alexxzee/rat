import shodan

def main():

  API_KEY = 'c0dNQsRE5mjf7fF4bhJNC9NIZr53Jz36'
  api = shodan.Shodan(API_KEY)

  try:
    results = api.search('Apache/2.4.18')
    print('Result found: {}'.format(results['total']))
    for result in results['matches']:
      print('IP: {} '.format(result['ip_str']))
      print(result['data'])
  except(shodan.APIError, e):
    print('Error: {}'.format(e))
