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



def callback():
    model = pkl.load(open('Models/vtc.pkl', 'rb'))
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
    strdata = ['age','education','Nscore','Escore','Oscore','Ascore','Cscore','Impulse'
        ,'Sensationseeking','Alcohol','Caffeine','Chocolate','Nicotine']
    print(list(zip(strdata,data)),model)
    prediction = model.predict(data.reshape(1,-1))
    lbl2 = ttk.Label(root, text=f'{list(zip(strdata,data))}').pack()
    lbl3 = ttk.Label(root, text=f'Patient with above inputs is projected as a {prediction} risk for abuse of stimulant drugs').pack()
def taketests():
    os.system('python SStest.py')
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

	lbl1 = ttk.Button(root,text='Take Personality tests',command=taketests).pack()
	button = ttk.Button(root,text = 'Submit!', command = callback)
	button.pack()
	root.title('Stimulant Abuse Risk Prediction (High Risk - Low Risk)')

	root.mainloop()
