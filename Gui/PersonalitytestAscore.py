from tkinter import *
from tkinter import ttk
import pickle as pkl

def callback():
        x = [mapvalue(v1.get()) *correlation1,mapvalue(v2.get()) * correlation2, mapvalue(v3.get())* correlation3
        ,mapvalue(v4.get())* correlation4,mapvalue(v5.get())* correlation5,mapvalue(v6.get())* correlation6
        ,mapvalue(v7.get())* correlation7,mapvalue(v8.get())* correlation8
        ,mapvalue(v9.get())* correlation9,mapvalue(v10.get())* correlation10]
        X = sum(x)+30
        print(X)
        root.destroy()
        pkl.dump(X, open('AscoreTest.pkl', 'wb'))
def mapvalue(number):
    values= {1:-2,2:-1,3:0,4:1,5:2}
    return values[number]
def Question(question,corr):
    v = IntVar()
    correlation = corr
    lblq= ttk.Label(root,text=f'{question}')
    combobox = ttk.Combobox(root, textvariable = v,values=(1,2,3,4,5),state='readonly')
    return v,correlation,lblq,combobox
if __name__ == "__main__":
        qs = ['Feel little concern for others' ,'Am interested in people'
    ,'Insult people.','Sympathize with others feelings.'
    ,'Am not interested in other peoples problems.','Have a soft heart.'
    ,'Am not really interested in others.',"Take time out for others."
    ,"Feel others' emotions",'Make people feel at ease.']
        cs = [-1,1,-1,1,-1,1,-1,1,1,1]
        root = Tk()
        lbltitle = ttk.Label(text='Select How well a statement describes you\nwhere 5 is accurate and 1 is innacurate',font = (('Arial'),22)).pack()

        v1,correlation1,lblq1,combobox1 = Question(qs[0],cs[0])
        v2,correlation2,lblq2,combobox2 = Question(qs[1],cs[1])
        lblq1.pack()
        combobox1.pack()
        lblq2.pack()
        combobox2.pack()
        v3,correlation3,lblq3,combobox3 = Question(qs[2],cs[2])
        v4,correlation4,lblq4,combobox4 = Question(qs[3],cs[3])
        lblq3.pack()
        combobox3.pack()
        lblq4.pack()
        combobox4.pack()
        v5,correlation5,lblq5,combobox5 = Question(qs[4],cs[4])
        v6,correlation6,lblq6,combobox6 = Question(qs[5],cs[5])
        lblq5.pack()
        combobox5.pack()
        lblq6.pack()
        combobox6.pack()
        v7,correlation7,lblq7,combobox7 = Question(qs[6],cs[6])
        v8,correlation8,lblq8,combobox8 = Question(qs[7],cs[7])
        lblq7.pack()
        combobox7.pack()
        lblq8.pack()
        combobox8.pack()
        v9,correlation9,lblq9,combobox9 = Question(qs[8],cs[8])
        v10,correlation10,lblq10,combobox10 = Question(qs[9],cs[9])
        lblq9.pack()
        combobox9.pack()
        lblq10.pack()
        combobox10.pack()
        button = ttk.Button(root,text='Enter',command=callback).pack()


        root.geometry('850x850')
        root.title('Ocean Survey: Agreeableness')
        root.mainloop()
