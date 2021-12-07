from tkinter import *

class MyWindow:
  def __init__(self, win):
    self.lbl1=Label(win, text='First name')
    self.lbl2=Label(win, text='Last name')
    self.lbl3=Label(win, text='StudentID')
    self.lbl4=Label(win, text='Age')
    self.t1=Entry(bd=3)
    self.t2=Entry(bd=3)
    self.t3=Entry(bd=3)
    self.t4=Entry(bd=3)
    self.lbl1.place(x=100, y=30)
    self.t1.place(x=200, y=30)
    self.lbl2.place(x=100, y=80)
    self.t2.place(x=200, y=80)
    self.lbl3.place(x=100, y=180)
    self.t3.place(x=200, y=180)
    self.lbl4.place(x=100, y=130)
    self.t4.place(x=200,y=130)
    self.b1=Button(win, text="Add to database")
    self.b1.place(x=100, y=210)
        
  def details(self):
    Fname=(self.t1.get)
    Lname=(self.t2.get)
    StudentID=(self.t3.get)
    Age=(self.t4.get)
    f=open("Students.txt","w")
    f.write(Fname,Lname,Age,StudentID)
    
window=Tk()
mywin=MyWindow(window)
window.title('Student GUI')
window.geometry("400x300+10+10")
window.mainloop()