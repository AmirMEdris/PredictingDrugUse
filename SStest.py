from tkinter import *
from tkinter import ttk
import pickle as pkl
def callback():
        x = [v1,v2, v3
        ,v4,v5,v6
        ,v7,v8
        ,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18]
        x = [i.get() for i in x]
        X = int(sum(x)/2)+1
        root.destroy()
        pkl.dump(X, open('SensationSeekingTest.pkl', 'wb'))
def Question(question):
    v = IntVar()
    v.set(0)
    cbox = Checkbutton(root, text=f'{question}', variable=v,
                       font='Arial 16')

    return v,cbox
if __name__ == "__main__":
        qs = ['I can become almost painfully bored in some conversations.'
            ,' I would rather go to a new place I may not like than go back again to a place I know I like'
            ,'I would like to try a sport that creates a physical thrill, like skiing, rock climbing, or surfing.'
            ,'I get restless if I stay home for long.'
            ,'I don’t like waiting with nothing to do.'
            ,'I rarely watch a movie more than once.'
            ,"I enjoy the unfamiliar."
            ,"If I see something unusual, I will go out of my way to check it out."
            ,'I get bored spending time with the same people everyday.'
            ,'My friends say it is hard to predict what I will want to do.'
            ,'I like to explore a new areas.'
            ,'I avoid having a daily routine.'
            ,'I am drawn to art that gives me an intense experience.'
            ," I prefer friends who are unpredictable."
            ,'I look forward to being in a place that is new and strange to me.'
            ,'To me, if I am spending the money to travel, the more foreign the country the better.'
            ,'I would like to be an explorer.'
            ,'I enjoy it when someone makes an unexpected sexual joke or comment that starts everyone laughing a little nervously.']
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
        v11,cbox11 = Question(qs[10])
        v12,cbox12 = Question(qs[11])
        v13,cbox13 = Question(qs[12])
        v14,cbox14 = Question(qs[13])
        v15,cbox15 = Question(qs[14])
        v16,cbox16 = Question(qs[15])
        v17,cbox17 = Question(qs[16])
        v18,cbox18 = Question(qs[17])
        cbox1.pack()
        cbox2.pack()
        cbox3.pack()
        cbox4.pack()
        cbox5.pack()
        cbox6.pack()
        cbox7.pack()
        cbox8.pack()
        cbox9.pack()
        cbox9.pack()
        cbox10.pack()
        cbox11.pack()
        cbox12.pack()
        cbox13.pack()
        cbox14.pack()
        cbox15.pack()
        cbox16.pack()
        cbox17.pack()
        cbox18.pack()






        button = ttk.Button(root,text='Enter',command=callback).pack()

        root.geometry('750x600')
        root.title('Sensation Seeking Survey')

        root.mainloop()

