import json

class jsonCreation():

    def __init__(self):
        self.general_url = {
            "url": "https://stats.nba.com/stats/leaguedashplayerstats?"
        }

        self.general_header = {
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
            "x-nba-stats-token": "true"
        }

        self.general_params = (
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
            ("Weight", "")
        ) 
# general_url = {
#     "url": "https://stats.nba.com/stats/leaguedashplayerstats?"
# }

# general_header = {
# "Accept": "application/json, text/plain, */*",
# "Accept-Encoding": "gzip, deflate, br",
# "Accept-Language": "en-US,en;q=0.9",
# "Cache-Control": "no-cache",
# "Connection": "keep-alive",
# "Host": "stats.nba.com",
# "Origin": "https://www.nba.com",
# "Pragma": "no-cache",
# "Referer": "https://www.nba.com/",
# "sec-ch-ua": "'Google Chrome';v='95', 'Chromium';v='95', ';Not A Brand';v='99'",
# "sec-ch-ua-mobile": "?0",
# "sec-ch-ua-platform": "Windows",
# "Sec-Fetch-Dest": "empty",
# "Sec-Fetch-Mode": "cors",
# "Sec-Fetch-Site": "same-site",
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
# "x-nba-stats-origin": "stats",
# "x-nba-stats-token": "true"}

# general_params =(
# ("College", ""),
# ("Conference", ""),
# ("Country", ""),
# ("DateFrom", ""),
# ("DateTo", ""),
# ("Division", ""),
# ("DraftPick", ""),
# ("DraftYear", ""),
# ("GameScope", ""),
# ("GameSegment", ""),
# ("Height", ""),
# ("LastNGames", "0"),
# ("LeagueID", "00"),
# ("Location", ""),
# ("MeasureType", "Advanced"),
# ("Month", "0"),
# ("OpponentTeamID", "0"),
# ("Outcome", ""),
# ("PORound", "0"),
# ("PaceAdjust", "N"),
# ("PerMode", "PerGame"),
# ("Period", "0"),
# ("PlayerExperience", ""),
# ("PlayerPosition", ""),
# ("PlusMinus", "N"),
# ("Rank", "N"),
# ("Season", "2021-22"),
# ("SeasonSegment", ""),
# ("SeasonType", "Regular Season"),
# ("ShotClockRange", ""),
# ("StarterBench", "" ),
# ("TeamID", "0"),
# ("TwoWay", "0"),
# ("VsConference", ""),
# ("VsDivision", ""),
# ("Weight", ""))

    def combine_dic(self, url, header, params):
        return dict(url=url, header=header, params=params)
    
    def create_json(self):
        generalDic = self.combine_dic(url=self.general_url, header=self.general_header, params=self.general_params)
        with open('general_stats.json', 'w') as fp:
            json.dump(generalDic, fp, indent=4)

if __name__ == '__main__':
    jc = jsonCreation()
    jc.create_json()
