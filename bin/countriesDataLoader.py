import pandas as pd
import fileinput
from pprint import pprint
from csv import DictReader
import re

class countriesDataLoader:
  def __init__(self):
    self.file = '../data/countries.tsv'
    self.countryKey2population = { }
    self.langs = []

  def loadCountries(self):
    self.countryKey2countryName = {}
    location2lang = {}
    with open(self.file) as rfh:
      line_cnt = 0
      countryKeyLocation = 0
      populationLocation = 0
      for line in rfh:
        items = line.strip().split("\t")
        # Location is fixed
        country_name = items[0]
        countryKey = items[3]
        location_cnt = 0
        if line_cnt == 0:
          for item in items:
            matches = re.findall(r'^lang:([a-z][a-z])/(.*)$', item)
            if matches:
              lang_code = matches[0][0]
              lang_desc = matches[0][1]
              location2lang[location_cnt] = lang_code
              self.countryKey2countryName[lang_code] = { }
              self.langs.append(lang_code)
            elif item == "Top Level Domain":
              countryKeyLocation = location_cnt
            elif item == "population":
              populationLocation = location_cnt
            location_cnt += 1
        else:
          for item in items:
            if location_cnt == countryKeyLocation:
              self.lcCountryName2countryKey[country_name.lower()] = item
            elif location_cnt == populationLocation:
              if item:
                self.countryKey2population[countryKey] = int(item.replace(",", "").strip())
            elif location_cnt in location2lang:
              self.countryKey2countryName[location2lang[location_cnt]][countryKey] = item
            location_cnt += 1
        line_cnt += 1

  def run(self):
    self.loadCountries()

if __name__ == '__main__':
  countriesDataLoader = countriesDataLoader()
  countriesDataLoader.run()
