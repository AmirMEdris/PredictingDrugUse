from tkinter import *
from tkinter import ttk
import pickle as pkl

def callback():
        x1=v1.get()
        x2=v2.get()
        x1= 1 if x1 == '18-24' else 2 if x1 == '25-34' else 3 if '35-44' else 4 if x1 == '45-54' else 5 if x1 =='55-64' else 6
        x2 = 0 if x2 == 'Left school before 16 years' else 1 if x2 == 'Left school at 16 years' else 2 if x2 == 'Left school at 17 years' else 3 if x2 =='Left school at 18 years' else 4 if x2 =='Some college or university, no certificate or degree' else 5 if x2 == 'Professional certificate/ diploma' else 6 if x2 == 'University degree' else 7 if x2 =='Masters degree'  else 8
        X=[x1,x2]
        root.destroy()
        pkl.dump(X, open('AgeandEdu.pkl', 'wb'))

def Question(question,corr):
    v = StringVar()
    correlation = corr
    lblq= ttk.Label(root,text=f'{question}')
    if corr == 1:
        combobox = ttk.Combobox(root, textvariable = v,values=('18-24','25-34','35-44','45-54','55-64','65+'),state='readonly')
    else:
        combobox = ttk.Combobox(root, textvariable = v,values=('Left school before 16 years'
                                                               ,'Left school at 16 years'
                                                               ,'Left school at 17 years'
                                                               ,'Left school at 18 years'
                                                               ,'Some college or university, no certificate or degree'
                                                               ,'Professional certificate/ diploma'
                                                               ,'University degree'
                                                               ,'Masters degree'
                                                               ,'Doctorate degree'),state='readonly')

    return v,correlation,lblq,combobox
if __name__ == "__main__":
        qs = ['Age' ,'Education']
        cs = [1,0]
        root = Tk()
        lbltitle = ttk.Label(text='Answer as accurately as possible',font = (('Arial'),17)).pack()

        v1,correlation1,lblq1,combobox1 = Question(qs[0],cs[0])
        v2,correlation2,lblq2,combobox2 = Question(qs[1],cs[1])
        lblq1.pack()
        combobox1.pack()
        lblq2.pack()
        combobox2.pack()

        button = ttk.Button(root,text='Enter',command=callback).pack()


        root.geometry('500x600')
        root.title('Age and Education test')
        root.mainloop()
