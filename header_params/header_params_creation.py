import json
from urllib.parse import urlparse
from urllib.parse import parse_qs

class jsonCreation():

    def __init__(self):

        self.header = {
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

        self.genURL = {
            "url": "https://stats.nba.com/stats/leaguedashplayerstats?",
            "full_url": "https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2021-22&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight="
        }

        self.genEstAdvURL = {
            "url": "https://stats.nba.com/stats/playerestimatedmetrics?",
            "full_url": "https://stats.nba.com/stats/playerestimatedmetrics?LeagueID=00&Season=2021-22&SeasonType=Regular+Season"
        }
    

        self.clutchURL = {
            "url": "https://stats.nba.com/stats/leaguedashplayerclutch?",
            "full_url": "https://stats.nba.com/stats/leaguedashplayerclutch?AheadBehind=Ahead+or+Behind&ClutchTime=Last+5+Minutes&College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&PointDiff=5&Rank=N&Season=2021-22&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="
        }

        self.playtypeURL = {
            "url": "https://stats.nba.com/stats/synergyplaytypes?",
            "full_url": "https://stats.nba.com/stats/synergyplaytypes?LeagueID=00&PerMode=PerGame&PlayType=Transition&PlayerOrTeam=P&SeasonType=Regular+Season&SeasonYear=2021-22&TypeGrouping=offensive"
        }

        self.trackingURL = {
            "url": "https://stats.nba.com/stats/leaguedashptstats?",
            "full_url": "https://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Drives&Season=2021-22&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="
        }

    def get_params(self, full_url):

        parsed_url = urlparse(full_url)
        param = parse_qs(parsed_url.query, keep_blank_values=True)

        return dict(param)


    def create_json(self, fileName, **kwargs):
        url = kwargs.get('url', None)
        header = kwargs.get('header', None)
        params = kwargs.get('params', None)

        if params is None: 
            pass
        else:
            params = dict(params)

        typeDic = dict(url=url, header=header, params=params)
        
        '''
        referenced the following link:
        https://stackoverflow.com/questions/33797126/proper-way-to-remove-keys-in-dictionary-with-none-values-in-pythonc
        '''
        def delete_none(_dict):
            for key, value in list(_dict.items()):
                if isinstance(value, dict):
                    delete_none(value)
                elif value is None:
                    del _dict[key]
                elif isinstance(value, list):
                    for v_i in value:
                        if isinstance(v_i, dict):
                            delete_none(v_i)
            return _dict
        
        delete_none(typeDic)

        with open(fileName + '.json', 'w') as fp:
            json.dump(typeDic, fp, indent=4

if __name__ == '__main__':
    jc = jsonCreation()
    # jc.create_json(url=jc.genURL, header=jc.genHeader, params=jc.genParams, fileName='general_stats')
    jc.create_json(header=jc.header, fileName='header')
    jc.create_json(url=jc.genURL, params=jc.get_params(jc.genURL['full_url']), fileName='general')
    jc.create_json(url=jc.genEstAdvURL, params=jc.get_params(jc.genEstAdvURL['full_url']), fileName='gen_Est_Adv')

