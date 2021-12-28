import json

f = open(r'C:\Users\justinkim2\Documents\GitHub\nba_advanced_stats_scrape\general_stats.json', 'r')
test = json.loads(f)

with open(r'C:\Users\justinkim2\Documents\GitHub\nba_advanced_stats_scrape\general_stats.json') as f:
  data = json.load(f)

data['header']