from bs4 import BeautifulSoup
import re

def extract_link(str):
  soup = BeautifulSoup(str, 'lxml')
  link_tabs = []
  for link in soup.find_all('a', href=True):
    if link.get('href') is not None:
      if "https://paris.craigslist.org/apa/d/" in link.get('href'):
        link_tabs.append(link.get('href'))
  return link_tabs

def findTitle(str):
  soup = BeautifulSoup(str, 'lxml')
  balise = soup.find('title')
  return balise.text


def isWordpress(str):
  soup = BeautifulSoup(str, 'lxml')
  for link in soup.find_all('a', href=True):
    if "wordpress" in link.get('href'):
      return True
    else:
      return False

def findForm(str):
  soup = BeautifulSoup(str, 'lxml')
  form = soup.find('form')
  print(form)


def findInputs(str):
  soup = BeautifulSoup(str, 'lxml')
  input_tabs = []
  for singleInput in soup.find_all('input'):
    input_tabs.append(singleInput)
  return input_tabs