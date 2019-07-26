import requests
import time
from .tools import extract as ex

def main():
  url = "https://paris.craigslist.org/search/apa?s=0"

  for page in range(0, 1788, 120):
    time.sleep(1)
    url = "https://paris.craigslist.org/search/apa?s=" + str(page)
    # Tester le site suivant pour un site wordpress
    # url = "https://www.pandat.fr/"
    r = requests.get(url)
    urls = ex.extract_link(r.text)
    print( 'Est un wordpress ?: ', ex.isWordpress(r.text))
    for u in urls:
      time.sleep(1)
      req = requests.get(u)
      title = ex.findTitle(req.text)
      form = ex.findForm(req.text)
      inputs = ex.findInputs(req.text)
      print(title, inputs, form)