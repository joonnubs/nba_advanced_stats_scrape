import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os
import glob
from pathlib import Path
from datetime import datetime 
from dateutil.relativedelta import relativedelta

''' 
references: 
https://towardsdatascience.com/how-scraping-nba-stats-is-cooler-than-michael-jordan-49d7562ce3ef
https://medium.com/@osanchez2323/web-scraping-nba-stats-4b4f8c525994
https://betterprogramming.pub/a-step-by-step-guide-to-web-scraping-nba-data-with-python-jupyter-beautifulsoup-and-pandas-7e2d334d4195
https://stackoverflow.com/questions/5074803/retrieving-parameters-from-a-url
'''

class nba_stats(): 
    
    def __init__(self):
        self.path = str(Path(__file__).parent.resolve())
        self.headerPath = self.path + '/header_params'
        self.fileList = []
        self.allHeadersParams = {}

        self.genMeasureTypes  = ['Base',
                                'Advanced',
                                'Misc',
                                'Scoring',
                                'Usage',
                                'Opponent',
                                'Defense',
                                ]
        
        self.clutchMeasureTypes = ['Base',
                                'Advanced',
                                'Misc',
                                'Scoring',
                                'Usage']

        '''
        Play Types and their Measure Types are named Play Type, but we name it measure type for consistency
        Play Types also include offensive and defensive parameters which should be differentiated
        '''
        self.playtypeMeasureTypes = ['Transition',
                                    'Isolation',
                                    'PRBallHandler',
                                    'PRRollman',
                                    'Postup',
                                    'Spotup',
                                    'Handoff',
                                    '']
        self.playtypeGrouping = ['offensive',
                                'defensive']
        

        self.oldestSeason = {
            'general_stats': 1996,
            'cluth_stats' : 1996
        }
        

    def json_load(self,path):
        for filename in glob.glob(os.path.join(path, '*.json')):
            self.filename = Path(filename).stem
            with open(filename) as currentfile:
                self.allHeadersParams[self.filename]= json.load(currentfile)
                if self.filename not in self.fileList:
                    self.fileList.append(self.filename) 
        return self.allHeadersParams

    def generate_all_seasons(self, dataType):
        currentDate = datetime.now()
        self.season = []
        while not currentDate.year == self.oldestSeason[dataType]:
            self.season.append(str(currentDate.year - 1) + '-' + (currentDate.strftime('%y')))
            currentDate -= relativedelta(years=1)

    def data_extract(self, dataType, measureType='all', season='2021-22'):
        args = self.json_load(path=self.headerPath)
        extDataType = args[dataType]

        if (dataType=='general') & (measureType=='EstAdv'):
            extDataType = args['gen_Est_Adv']
            extDataType['params']['Season'] = season 
        else:
            extDataType['params']['Measure '] = measureType
            extDataType['params']['Season'] = season  

        # extDataType['params']['MeasureType'] = measureType
        # extDataType['params']['Season'] = season 
        extDataTypeResp = requests.get(extDataType['url']['url'], headers=args['header']['header'], params=extDataType['params'], timeout=5)
        if extDataTypeResp.status_code == 200:
            pass 
        else:
            print('Request status code: {}'.format(extDataTypeResp.status_code))
            exit()
        response_json = extDataTypeResp.json()
        dfStats = pd.DataFrame(response_json['resultSets'][0]['rowSet'])
        dfStats.columns = response_json['resultSets'][0]['headers']
        dfStats.to_csv(str(dataType) + '_' + str(measureType) + '_' + str(season) + '.csv')


    # def extract_all(self):


if __name__ == '__main__':
    # path = str(Path(__file__).parent.resolve())
    # headerPath = path + '/header_params'
    ns = nba_stats()
    # jsonDict = ns.json_load(path=headerPath)
    # ns.data_extract(dataType='general', measureType='Base', season='2020-21')
    ns.data_extract(dataType='general', measureType='EstAdv', season='2020-21')
    '''
    Instead of assigning variables to be a dataframe,
        loop through and add dataframes to a list or dictionary
    '''
    # genStats = jsonDict['general_stats'] 
    # genStatsResponse = requests.get(genStats['url']['url'], headers=genStats['header'], params=genStats['params'], timeout=5)
    # # response_json = genStatsResponse.json()
    # # print(response_json)
    # genStatsFrame = pd.DataFrame(genStatsResponse.json()['resultSets'][0]['rowSet'])
    # genStatsFrame.columns = genStatsResponse.json()['resultSets'][0]['headers']
    # print(genStatsFrame)
    # # genStatsFrame.to_csv('stats_test.csv')

    '''
    Testing something
    # req = requests.get('https://stats.nba.com/stats/leaguedashplayerstats', headers=genStats['header'], params=genStats['params'], timeout=5)
    # print(dir(req))
    # print(vars(req).keys())
    '''