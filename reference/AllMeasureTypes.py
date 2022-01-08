import json

genMeasureTypes  = ['Base',
                    'Advanced',
                    'Misc',
                    'Scoring',
                    'Usage',
                    'Opponent',
                    'Defense',
                    ]

clutchMeasureTypes = ['Base',
                    'Advanced',
                    'Misc',
                    'Scoring',
                    'Usage']

#Misc, OffScreen, Cut, and Transition do not have "Defensive" Groupings
playtypeMeasureTypes = ['Transition',
                        'Isolation',
                        'PRBallHandler',
                        'PRRollman',
                        'Postup',
                        'Spotup',
                        'Handoff',
                        'Cut',
                        'OffScreen',
                        'OffRebound',
                        'Misc']
                        

trackingMeasureTypes = ['Drives',
                        'Defense',
                        'CatchShoot',
                        'Passing',
                        ]