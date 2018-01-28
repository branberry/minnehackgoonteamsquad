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
    #append to main csv
