#Import database entry that user inputs
#>function called unbench()
#>append to correct bucket
sys.path.append(minnehackgoonteamsquad/deepLearning/learning.py)

def unbench(userid):
    def maketime(injurydate):
        import time
        from time import mktime
        import datetime
        returnTime=time.gmtime()[:3]+(0,0,0,0,0,0)
        new=injurydate[injurydate.find("-")+1:]
        #make a time datetime object
        injurydate=(datetime.datetime(
        #Day
        2000+int(new[new.find("-")+1:]),
        #month
        [0,'Jan','Feb','Mar','Apr','May','Jun','Jul',
         'Aug','Sep','Oct','Nov','Dec'].index(new[:new.find("-")]),
        #year
        int(injurydate[:injurydate.find("-")]))).timetuple()
        #Convert to days
        days=(mktime(returnTime)-mktime(injurydate))/86400
        if days<1:
            return 13
        if days<3:
            return 1
        if days<7:
            return 2
        if days<10:
            return 3
        if days<22:
            return 4
        else:
            return 5

    thisRow=['RegID',
             'Q7',
             'Q4',
             'Q5',
             'Q6',
            'Q500',
             'Q21B',
             'Q21C',
             'Q21D',
            'Q21E',
             'Q21F',
             'Q21G',
             'Q21H',
            'Q21I',
             'Q21J',
             'Q21K',
             'Q21L',
            'Q21M',
             'Q21N',
             'Q21O',
             'Q20',
            'Q18',
             'Q22',
             maketime(injurydate),
             'Q65']
    
    import getBucket from learning.py
    bucket=getBucket(thisRow)
    #append to bucket
    bucketDict=[0:"15_short_light.csv",
    1:"15_short_heavy.csv",
    2:"15_medium_light.csv",
    3:"15_medium_heavy.csv",
    4:"15_tall_light.csv",
    5:"15_tall_heavy.csv",
    6:"16_short_light.csv",
    7:"16_short_heavy.csv",
    8:"16_medium_light.csv",
    9:"16_medium_heavy.csv",
    10:"16_tall_light.csv",
    11:"16_tall_heavy.csv",
    12:"17_short_light.csv",
    13:"17_short_heavy.csv",
    14:"17_medium_light.csv",
    15:"17_medium_heavy.csv",
    16:"17_tall_light.csv",
    17:"17_tall_heavy.csv",
    18:"18_short_light.csv",
    19:"18_short_heavy.csv",
    20:"18_medium_light.csv",
    21:"18_medium_heavy.csv",
    22:"18_tall_light.csv",
    23:"18_tall_heavy.csv"]
    with open(bucketDict[bucket],'a+') as csvout:
                        spamwriter = csv.DictWriter(csvout, fieldnames=fields)
                        spamwriter.writerow(thisRow)
    with open('MasterConcussionData.csv','a+') as csvout:
                        spamwriter = csv.DictWriter(csvout, fieldnames=fields)
                        spamwriter.writerow(thisRow)
