from tkinter import *
from tkinter import ttk
import pickle as pkl

def callback():
        x = [v1,v2, v3
        ,v4,v5,v6
        ,v7,v8
        ,v9,v10]
        x = [i.get() for i in x]
        X = int(sum(x))
        root.destroy()
        pkl.dump(X,open('ImpulsivityTest.pkl','wb'))
def Question(question):
    v = IntVar()
    v.set(0)
    cbox = Checkbutton(root, text=f'{question}', variable=v,
                       font='Arial 16')

    return v,cbox
if __name__ == "__main__":
        qs = ['Usually I express my opinion freely, without carefully selecting words.'
    ,'I get angry easily.'
    ,'If insulted, I may become physically aggressive.'
    ,'If someone says to me something disrespectful, I may reply in a harsh manner.'
    ,'When I was a child, I ran away from home after a disagreement with my parents.'
    ,'I get upset over small things.'
    ,"When emotions run high, I may say something I will regret later."
    ,"I may break and throw things when angry."
    ,'There were times in my life when I had to pay for my impulsiveness.'
    ,'I often buy on impulse, without proper reflection.']
        root = Tk()

        lbltitle = ttk.Label(text='Select All Statements That Apply To You',font = (('Arial'),22)).pack()
        v1,cbox1 = Question(qs[0])
        v2,cbox2 = Question(qs[1])
        v3,cbox3 = Question(qs[2])
        v4,cbox4 = Question(qs[3])
        v5,cbox5 = Question(qs[4])
        v6,cbox6 = Question(qs[5])
        v7,cbox7 = Question(qs[6])
        v8,cbox8 = Question(qs[7])
        v9,cbox9 = Question(qs[8])
        v10,cbox10 = Question(qs[9])
        cbox1.pack()
        cbox2.pack()
        cbox3.pack()
        cbox4.pack()
        cbox5.pack()
        cbox6.pack()
        cbox7.pack()
        cbox8.pack()
        cbox9.pack()
        cbox10.pack()







        button = ttk.Button(root,text='Enter',command=callback).pack()
        root.title('Impulsivity Metric Survey')
        root.geometry('850x850')
        root.mainloop()
