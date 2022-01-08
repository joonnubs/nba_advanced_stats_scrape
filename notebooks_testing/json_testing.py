import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os
import glob
from pathlib import Path

f = open(r'C:\Users\justinkim2\Documents\GitHub\nba_advanced_stats_scrape\general_stats.json', 'r')
test = json.loads(f)

with open(r'C:\Users\justinkim2\Documents\GitHub\nba_advanced_stats_scrape\general_stats.json') as f:
  data = json.load(f)

data['header']

'''
testing paramesters
'''
path = str(Path(__file__).parent.resolve())
headerPath = path + '/header_params'
ns = nba_stats()
jsonDict = ns.json_load(path=headerPath)