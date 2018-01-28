import numpy as np
import pandas as pd
from sklearn import preprocessing
import os
#path = '/Conkdata/'

bucket_to_CSV = {
    0:"15_short_light.csv",
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
    23:"18_tall_heavy.csv"
}
outcome_to_benchtime = {
    0 : "Can return in less than 1 day",
    1 : "Bench for 1-2 days",
    2 : "Bench for 3-6 days",
    3 : "Bench for 7-9 days",
    4 : "Bench for 10-21 days",
    5 : "Bench for 22 or more days",
    6 : "Bench for season",
    7 : "Serious medical attention required!",
}

def getBucket(thisRow):
    #Function to determine original dataset object's classification
    #based on thisRow = [age, height, weight]
    if thisRow[0] >= 15 and thisRow[0] < 16:
        if thisRow[1] >= 48 and thisRow[1] < 60:
            if thisRow[2] >= 100 and thisRow[2] < 200:
                return 0
            if thisRow[2] >= 200 and thisRow[2] < 300:
               return 1
        if thisRow[1] >= 60 and thisRow[1] < 72:
            if thisRow[2] >= 100 and thisRow[2] < 200:
               return 2
            if thisRow[2] >= 200 and thisRow[2] < 300:
                return 3
        if thisRow[1] >= 72 and thisRow[1] < 84:
            if thisRow[2] >= 100 and thisRow[2] < 200:
                return 4
            if thisRow[2] >= 200 and thisRow[2] < 300:
                return 5
    if thisRow[0] >= 16 and thisRow[0] < 17:
        if thisRow[1] >= 48 and thisRow[1] < 60:
            if thisRow[2] >= 100 and thisRow[2] < 200:
                return 6
            if thisRow[2] >= 200 and thisRow[2] < 300:
                return 7
        if thisRow[1] >= 60 and thisRow[1] < 72:
            if thisRow[2] >= 100 and thisRow[2] < 200:
                return 8
            if thisRow[2] >= 200 and thisRow[2] < 300:
                return 9
        if thisRow[1] >= 72 and thisRow[1] < 84:
            if thisRow[2] >= 100 and thisRow[2] < 200:
                return 10
            if thisRow[2] >= 200 and thisRow[2] < 300:
                return 11
    if thisRow[0] >= 17 and thisRow[0] < 18:
        if thisRow[1] >= 48 and thisRow[1] < 60:
            if thisRow[2] >= 100 and thisRow[2] < 200:
                return 12
            if thisRow[2] >= 200 and thisRow[2] < 300:
                return 13
        if thisRow[1] >= 60 and thisRow[1] < 72:
            if thisRow[2] >= 100 and thisRow[2] < 200:
                return 14
            if thisRow[2] >= 200 and thisRow[2] < 300:
                return 15
        if thisRow[1] >= 72 and thisRow[1] < 84:
            if thisRow[2] >= 100 and thisRow[2] < 200:
                return 16
            if thisRow[2] >= 200 and thisRow[2] < 300:
                return 17
    if thisRow[0] >= 18:
        if thisRow[1] >= 48 and thisRow[1] < 60:
            if thisRow[2] >= 100 and thisRow[2] < 200:
                return 18
            if thisRow[2] >= 200 and thisRow[2] < 300:
                return 19
        if thisRow[1] >= 60 and thisRow[1] < 72:
            if thisRow[2] >= 100 and thisRow[2] < 200:
                return 20
            if thisRow[2] >= 200 and thisRow[2] < 300:
                return 21
        if thisRow[1] >= 72 and thisRow[1] < 84:
            if thisRow[2] >= 100 and thisRow[2] < 200:
                return 22
            if thisRow[2] >= 200 and thisRow[2] < 300:
                return 23

def userBucket(UAge, UHeight, UWeight):
    # load all data from our injuries file

    data = pd.read_csv("MasterConcussionData.csv")
    # set X and Y where X is our data classifiers (age, weight and height) and Y (return time) is the predition
    X_raw = data.iloc[:, 2:5].values
    Xlist = []
    Ylist = []
    for x in range(0, len(X_raw)):
        bucket = getBucket(X_raw[x])
        if bucket is not None:
            Ylist.append(bucket)
            Xlist.append(X_raw[x])

    X = np.array(Xlist)
    Y = np.array(Ylist)

    #Create dataframe to perform regression with
    df = pd.DataFrame(X,columns=['Age','Height', 'Weight'])
    df['Buckets'] = pd.Series(Y)

    from mpl_toolkits.mplot3d import Axes3D
    import statsmodels.formula.api as smf
    import matplotlib.pyplot as plt
    model = smf.ols(formula='Buckets ~ Age + Height + Weight', data=df)
    results_formula = model.fit()

    #We have our model, lets predict!
    x = [[UAge, UHeight, UWeight]]
    target = pd.DataFrame(x,columns=['Age','Height', 'Weight'])
    myBucket = int(round(results_formula.predict(target)))
    if myBucket < 0:
        myBucket = 0
    if myBucket > 23:
        myBucket = 23
    return bucket_to_CSV[myBucket]

def getBenchTime(age, height, weight, symptoms):
    bucket = userBucket(age, height, weight)
    #load all data from our injuries file
    symptomArr = symptoms.split(',')
    numSymptoms = len(symptomArr)
    if os.stat(bucket).st_size==0:
        return "Sorry, we don't have enought data to make a safe recommendation"
    data = pd.read_csv(bucket)
    X_raw_np = data.iloc[:, 6:19].values

    Y_raw = data.iloc[:, 23].values
    doc_raw = data.iloc[:, 23].values
    X_raw_list = X_raw_np.tolist()
    Xlist = []
    Ylist = []
    #Cleanse this array to match regression goal
    for row in Y_raw:
        if row == 14:
            #if season ended before person could return, TODO: use doctors opinion
            Ylist.append(3)
        elif row == 13:
            Ylist.append(0)
        else:
            Ylist.append(row)
    #count up number of symptoms
    for row in X_raw_list:
        symptom_count = 0
        for item in row:
            if item != "#NULL!":
                symptom_count = symptom_count + 1
        Xlist.append(symptom_count)
    Y = np.array(Ylist)
    X = np.array(Xlist)
    from mpl_toolkits.mplot3d import Axes3D
    import statsmodels.api as sm
    import matplotlib.pyplot as plt
    model = sm.OLS(Y,X).fit()
    myBenchTime = int(round(model.predict(numSymptoms)[0]))
    return outcome_to_benchtime[myBenchTime]

# def runSimulation():
#     run = True
#     while(run):
#         age = int(input("Please enter age: "))
#         height = int(input("Please enter height: "))
#         weight = int(input("Please enter weight: "))
#         symp = int(input("Please enter num symptoms: "))
#         if 14 < age < 19 and 48 <= height < 84 and 100 <= weight < 300:
#             print(getBenchTime(age,height,weight, symp))
#             cont = input("Want to check another? (y/n): ")
#             if cont == 'n':
#                 run = False
#             elif cont != 'y':
#                 print('Could not determine intentions... exiting.')
#                 run = False
#         else:
#             print("Please check your inputs and try again.")
