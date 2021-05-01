from tkinter import *
from tkinter import ttk
import pickle as pkl

def callback():
        x = [v1.get() *correlation1,v2.get() * correlation2, v3.get()* correlation3
        ,v4.get()* correlation4]
        root.destroy()
        pkl.dump(x, open('Consumption.pkl', 'wb'))

def Question(question,corr):
    v = IntVar()
    correlation = corr
    lblq= ttk.Label(root,text=f'{question}')
    combobox = ttk.Combobox(root, textvariable = v,values=(0,1,2,3,4,5,6),state='readonly')
    return v,correlation,lblq,combobox
if __name__ == "__main__":
        qs = ['Nicotine' ,'Caffeine'
            ,'Chocolate','Alcohol']
        cs = [1,1,1,1]
        root = Tk()
        lbltitle = ttk.Label(text='Select most accurate option for time last consumed \nwhere 6 is last 24 hours \n5 is last week \n4 is last month \n3 is last year \n2 is last decade \n1 is over a decade \nand 0 is never used',font = (('Arial'),17)).pack()

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

        button = ttk.Button(root,text='Enter',command=callback).pack()


        root.geometry('500x600')
        root.title('Relative Consumption Survey')
        root.mainloop()
