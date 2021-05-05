from tkinter import *
from tkinter import ttk
import os
import pickle as pkl
import numpy as np

import Impulsivitytest
import SStest

import PersonalitytestAscore
import PersonalitytestCscore
import PersonalitytestExtraversion
import PersonalitytestNscore
import PersonalitytestOscore

import AgeandEdu
import ConsumptionSurvey
import sklearn


def predict(data):
    stimmodel = pkl.load(open('../Models/stimvtc.pkl', 'rb'))
    depmodel = pkl.load(open('../Models/depvtc.pkl', 'rb'))
    halumodel = pkl.load(open('../Models/haluvtc.pkl', 'rb'))
    stimproba = stimmodel.predict_proba(data.reshape(1,-1))
    stimprediction = stimmodel.predict(data.reshape(1,-1))
    depproba = depmodel.predict_proba(data.reshape(1,-1))
    depprediction = depmodel.predict(data.reshape(1,-1))
    haluproba = halumodel.predict_proba(data.reshape(1,-1))
    haluprediction = halumodel.predict(data.reshape(1,-1))
    return stimproba,stimprediction,depproba,depprediction,haluproba,haluprediction
def callback():
    
    X = pkl.load(open('AgeandEdu.pkl','rb'))
    age,education = X[0],X[1]
    Nscore = pkl.load(open('NscoreTest.pkl', 'rb'))
    Ascore = pkl.load(open('AscoreTest.pkl', 'rb'))
    Oscore = pkl.load(open('CscoreTest.pkl', 'rb'))
    Cscore = pkl.load(open('OscoreTest.pkl', 'rb'))
    Escore = pkl.load(open('EscoreTest.pkl', 'rb'))
    Impulse = pkl.load(open('ImpulsivityTest.pkl', 'rb'))
    Sensationseeking = pkl.load(open('SensationSeekingTest.pkl', 'rb'))
    X =  pkl.load(open('Consumption.pkl','rb'))
    print(X)
    Nicotine,Caffeine,Chocolate,Alcohol = X[0],X[1],X[2],X[3]
    #Age,Education,Nscore,Escore,Oscore,Ascore,Cscore
    #Impulsive,SensationSeeking,Alchol,Caff,Chocalate,Nicotine
    data=[age,education,Nscore,Escore,Oscore,Ascore,Cscore,Impulse
        ,Sensationseeking,Alcohol,Caffeine,Chocolate,Nicotine]
    data=np.array(data)
    print(data)
    strdata = ['age','education','Nscore','Escore','Oscore','Ascore','Cscore','Impulse'
        ,'Sensationseeking','Alcohol','Caffeine','Chocolate','Nicotine']
   
    stimproba,stimprediction,depproba,depprediction,haluproba,haluprediction = predict(data)
    stimlbl2 = ttk.Label(root, text=f'{list(zip(strdata,data))}').pack()
    stimlbl3 = ttk.Label(root, text=f'Patient with above inputs is projected as a {stimprediction} risk for abuse of stimulant drugs whith a confidence of {max(stimproba[0])}, \n{depprediction} for depressants with a confidence of {max(depproba[0])}, and {haluprediction} for depressants with a confidence of {max(haluproba[0])}').pack()
    
def taketests():
    os.system('python SStest.py')
    os.system('python ImpulsivityTest.py')
    os.system('python PersonalitytestAscore.py')
    os.system('python PersonalitytestCscore.py')
    os.system('python PersonalitytestExtraversion.py')
    os.system('python PersonalitytestNscore.py')
    os.system('python PersonalitytestOscore.py')
    os.system('python AgeandEdu.py')
    os.system('python ConsumptionSurvey.py')
    print()
'''
SA/DLJFBASDLFN/A
'''
if __name__ == "__main__":
	root = Tk()
	root.geometry('850x850')
	lbl1 = ttk.Button(root,text='Take Personality tests',command=taketests).pack()
	button = ttk.Button(root,text = 'Submit!', command = callback)
	button.pack()
	root.title('Stimulant Abuse Risk Prediction (High Risk - Low Risk)')
    
	root.mainloop()
