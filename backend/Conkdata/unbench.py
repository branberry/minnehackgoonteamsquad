#Import database entry that user inputs
#>function called unbench()
#>append to correct bucket
# def maketime(injurydate):
#     import time
#     from time import mktime
#     import datetime
#     new=injurydate[injurydate.find("-")+1:]
#     #make a time datetime object
#     injurydate=(datetime.datetime(
#     2000+int(new[new.find("-")+1:]),
#     #month
#     [0,'Jan','Feb','Mar','Apr','May','Jun','Jul',
#      'Aug','Sep','Oct','Nov','Dec'].index(new[:new.find("-")]),
#     #year
#     int(injurydate[:injurydate.find("-")]))).timetuple()
#     #Convert to days
#     days=(mktime(time.gmtime())-mktime(injurydate))/86400
#     if days<1:
#         return 13
#     if days<3:
#         return 1
#     if days<7:
#         return 2
#     if days<10:
#         return 3
#     if days<22:
#         return 4
#     else:
#         return 5

def unbench(u,i):
    sypts = [None]*13
    symptomArr = i['symptoms'].split(',')
    for k in range(0,len(symptomArr)):
        sypts[k] = symptomArr[k]
    thisRow=[i["user_id"],
         i["bench_date"],
         u["age"],
         u["height"],
         u["weight"],
         'Male',
         sypts[0],
         sypts[1],
         sypts[2],
         sypts[3],
         sypts[4],
         sypts[5],
         sypts[6],
         sypts[7],
         sypts[8],
         sypts[9],
         sypts[10],
         sypts[11],
         sypts[12],
         "",
         'concussion',
        'head/face',
         i["unbench_date"],
         6,
         '']

    from .learning import userBucket
    bucket=userBucket(u["age"],u["weight"],u["height"],)
    #append to bucket
    import csv
    fields = ['RegID','Q7','Q4','Q5','Q6','Q500','Q21B','Q21C','Q21D','Q21E','Q21F','Q21G','Q21H','Q21I','Q21J','Q21K','Q21L','Q21M','Q21N','Q21O','Q20','Q18','Q22','Q28','Q65']
    print(bucket)
    with open(bucket,'a+') as csvout:
                        spamwriter = csv.writer(csvout,  delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                        spamwriter.writerow(thisRow)
    with open('MasterConcussionData.csv','a+') as csvout:
                        spamwriter = csv.writer(csvout,  delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                        spamwriter.writerow(thisRow)
