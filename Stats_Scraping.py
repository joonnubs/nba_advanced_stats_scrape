import requests
from bs4 import BeautifulSoup
import pandas as pd

''' 
references: 
https://towardsdatascience.com/how-scraping-nba-stats-is-cooler-than-michael-jordan-49d7562ce3ef
https://medium.com/@osanchez2323/web-scraping-nba-stats-4b4f8c525994
https://betterprogramming.pub/a-step-by-step-guide-to-web-scraping-nba-data-with-python-jupyter-beautifulsoup-and-pandas-7e2d334d4195
https://stackoverflow.com/questions/5074803/retrieving-parameters-from-a-url
'''

class nba_stats(): 
    
    def __init__(self):
        pass

    def
url = 'https://stats.nba.com/stats/leaguedashplayerstats?'
header = {
"Accept": "application/json, text/plain, */*",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.9",
"Cache-Control": "no-cache",
"Connection": "keep-alive",
"Host": "stats.nba.com",
"Origin": "https://www.nba.com",
"Pragma": "no-cache",
"Referer": "https://www.nba.com/",
"sec-ch-ua": "'Google Chrome';v='95', 'Chromium';v='95', ';Not A Brand';v='99'",
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-site",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
"x-nba-stats-origin": "stats",
"x-nba-stats-token": "true"}


params =(
("College", ""),
("Conference", ""),
("Country", ""),
("DateFrom", ""),
("DateTo", ""),
("Division", ""),
("DraftPick", ""),
("DraftYear", ""),
("GameScope", ""),
("GameSegment", ""),
("Height", ""),
("LastNGames", "0"),
("LeagueID", "00"),
("Location", ""),
("MeasureType", "Advanced"),
("Month", "0"),
("OpponentTeamID", "0"),
("Outcome", ""),
("PORound", "0"),
("PaceAdjust", "N"),
("PerMode", "PerGame"),
("Period", "0"),
("PlayerExperience", ""),
("PlayerPosition", ""),
("PlusMinus", "N"),
("Rank", "N"),
("Season", "2021-22"),
("SeasonSegment", ""),
("SeasonType", "Regular Season"),
("ShotClockRange", ""),
("StarterBench", "" ),
("TeamID", "0"),
("TwoWay", "0"),
("VsConference", ""),
("VsDivision", ""),
("Weight", ""))

response = requests.get(url, headers=header, params = params)
response_json = response.json()
frame = pd.DataFrame(response_json['resultSets'][0]['rowSet'])
frame.columns = response_json['resultSets'][0]['headers']
print(frame)

if __name__ == '__main__':
    