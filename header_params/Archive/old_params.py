        self.genURL = {
            "url": "https://stats.nba.com/stats/leaguedashplayerstats?",
            "full_url": "https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2021-22&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight="
        }

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

        self.genParams = (
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
            ("MeasureType", ""), #argument required. Will be defined in Stat_Scraping.py
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
            ("Season", "2021-22"), #argument required. Need to loop through all avaiable seasons 
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

        self.genEstAdvURL = {
            "url": "https://stats.nba.com/stats/playerestimatedmetrics?",
            "full_url": "https://stats.nba.com/stats/playerestimatedmetrics?LeagueID=00&Season=2021-22&SeasonType=Regular+Season"
        }

        self.genEstAdvHeader = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'stats.nba.com',
            'Origin': 'https://www.nba.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.nba.com/',
            'sec-ch-ua': "'Not A;Brand';v='99', 'Chromium';v='96', 'Google Chrome';v='96'",
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'x-nba-stats-origin': 'stats',
            'x-nba-stats-token': 'true'
        }

        self.genEstAdvParams = (
            ("LeagueID", "00"),
            ("Season", "2021-22"),
            ("SeasonType", "Regular Season")
        )