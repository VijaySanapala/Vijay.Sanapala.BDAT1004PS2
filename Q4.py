#!/usr/bin/env python
# coding: utf-8

# In[2]:


### Mortgage class

from tkinter import Tk, Canvas, Frame, BOTH, Button, Entry, END, Label, LEFT, RIGHT, RAISED
import math

class Mortgage(Frame):       #Class to calculate Monthly Mortgage Payments
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
        
        label = Label(self, text='Loan Amount:')
        label.grid(row=0, column=0, padx=10, pady=10)
        
        self.loanEnt = Entry(self)
        self.loanEnt.grid(row=0, column=1, padx=10, pady=10)
        
        label = Label(self, text='Interest Rate:')
        label.grid(row=1, column=0, padx=10, pady=5)
        
        self.interestEnt = Entry(self)
        self.interestEnt.grid(row=1, column=1, padx=10, pady=5)
        
        label = Label(self, text='Loan Terms:')
        label.grid(row=2, column=0, padx=10, pady=5)
        
        self.termsEnt = Entry(self)
        self.termsEnt.grid(row=2, column=1, padx=10, pady=5)
        
        button = Button(self, text='Compute Mortgage:', command=self.compute)
        button.grid(row=3, column=0, padx=10, pady=5)
        
        self.mortgageAmount = Entry(self)
        self.mortgageAmount.grid(row=3, column=1, padx=10, pady=5)
        
    def compute(self):
        self.P = float(self.loanEnt.get())
        self.r = float(self.interestEnt.get())/100
        self.t = float(self.termsEnt.get())
        self.n = 12
        self.M = (self.P*(self.r/self.n)*(1 + (self.r / self.n))**(self.n*self.t))/(((1 + (self.r / self.n))**(self.n*self.t)) - 1)
        self.mortgageAmount.delete(0, END)
        self.mortgageAmount.insert(0, round(self.M, 2))
        
        #referred https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/, https://www.tutorialspoint.com/simple-gui-calculator-using-tkinter-in-python


# In[3]:


# Calculator class

class Calculator(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
        
        self.displayArea = Entry(self, bg = 'gray75')
        self.displayArea.grid(row=0, column=1, padx=5, pady=5)
        self.displayArea.focus_set()
        
        buttonMC = Button(self, text='MC', bg ='white', command=self.clearall, height=1, width=3, relief=RAISED)
        buttonMC.grid(row=1, column=0, padx=5, pady=5)
        
        buttonMP = Button(self, text='M+', bg ='white', command=self.clearall, height=1, width=3, relief=RAISED)
        buttonMP.grid(row=1, column=1, padx=5, pady=5)
        
        buttonMM = Button(self, text='M-', bg ='white', command=self.clearall, height=1, width=3, relief=RAISED)
        buttonMM.grid(row=1, column=2, padx=5, pady=5)
        
        buttonMR = Button(self, text='MR', bg ='white', command=self.clearall, height=1, width=3, relief=RAISED)
        buttonMR.grid(row=1, column=3, padx=5, pady=5)
        
        ##
        
        
        buttonC = Button(self, text='C', bg ='white', height=1, width=3, relief=RAISED, command=self.clearall)
        buttonC.grid(row=2, column=0, padx=5, pady=5)
        
        buttonSquareRoot = Button(self, text='SqR', bg ='white', height=1, width=3, relief=RAISED, command=self.squareRoot)
        buttonSquareRoot.grid(row=2, column=1, padx=5, pady=5)
        
        buttonSquare = Button(self, text='x^2', bg ='white', height=1, width=3, relief=RAISED, command=self.square)
        buttonSquare.grid(row=2, column=2, padx=5, pady=5)
        
        buttonPlus = Button(self, text='+', bg ='white', height=1, width=3, relief=RAISED, command=lambda:self.action('+'))
        buttonPlus.grid(row=2, column=3, padx=5, pady=5)
        
        ##
        
        button7 = Button(self, text='7', bg ='white', height=1, width=3, relief=RAISED, command=lambda:self.action(7))
        button7.grid(row=3, column=0, padx=5, pady=5)
        
        button8 = Button(self, text='8', bg ='white', height=1, width=3, relief=RAISED, command=lambda:self.action(8))
        button8.grid(row=3, column=1, padx=5, pady=5)
        
        button9 = Button(self, text='9', bg ='white', height=1, width=3, relief=RAISED, command=lambda:self.action(9))
        button9.grid(row=3, column=2, padx=5, pady=5)
        
        buttonMinus = Button(self, text='-', bg ='white', width=3, relief=RAISED, command=lambda:self.action('-'))
        buttonMinus.grid(row=3, column=3, padx=5, pady=5)
        
        ##
        
        button4 = Button(self, text='4', bg ='white', height=1, width=3, relief=RAISED, command=lambda:self.action(4))
        button4.grid(row=4, column=0, padx=5, pady=5)
        
        button5 = Button(self, text='5', bg ='white', height=1, width=3, relief=RAISED, command=lambda:self.action(5))
        button5.grid(row=4, column=1, padx=5, pady=5)
        
        button6 = Button(self, text='6', bg ='white', height=1, width=3, relief=RAISED, command=lambda:self.action(6))
        button6.grid(row=4, column=2, padx=5, pady = 5)
        
        buttonMinus = Button(self, text='*', bg ='white', width=3, relief=RAISED, command=lambda:self.action('*'))
        buttonMinus.grid(row=4, column=3, padx=5, pady=5)
        
        ##
        
        button1 = Button(self, text='1', bg ='white', height=1, width=3, relief=RAISED, command=lambda:self.action(1))
        button1.grid(row=5, column=0, padx=5, pady=5)
        
        button2 = Button(self, text='2', bg ='white', height=1, width=3, relief=RAISED, command=lambda:self.action(2))
        button2.grid(row=5, column=1, padx=5, pady=5)
        
        button3 = Button(self, text='3', bg ='white', height=1, width=3, relief=RAISED, command=lambda:self.action(3))
        button3.grid(row=5, column=2, padx=5, pady=5)
        
        buttonDivide = Button(self, text='/', bg ='white', height=1, width=3, relief=RAISED, command=lambda:self.action('/'))
        buttonDivide.grid(row=5, column=3, padx=5, pady=5)
        ##
        button0 = Button(self, text='0', bg ='white', height=1, width=3, relief=RAISED, command=lambda:self.action(0))
        button0.grid(row=6, column=0, padx=5, pady=5)
        
        buttonPoint = Button(self, text='.', bg ='white', height=1, width=3, relief=RAISED, command=lambda:self.action('.'))
        buttonPoint.grid(row=6, column=1, padx=5, pady=5)
        
        buttonPlusMinus = Button(self, text='+-', bg ='white', height=1, width=3, relief=RAISED, command=lambda:self.action('-'))
        buttonPlusMinus.grid(row=6, column=2, padx=5, pady=5)
        
        buttonEquals = Button(self, text='=', bg ='white', height=1, width=3, relief=RAISED, command=lambda:self.equals())
        buttonEquals.grid(row=6, column=3, padx=5, pady=5)
        
    def action(self,argi): 
        'pressed button value is inserted into the end of the text area'
        self.displayArea.insert(END,argi) 
                
    def getandreplace(self): 
        'replace x with *'
        self.expression = self.displayArea.get()  
        self.newtext=self.expression.replace('x','*') 
  
  
    def equals(self): 
        """when the equal button is pressed"""
        self.getandreplace() 
        try: 
            # evaluate the expression using the eval function 
            self.value= eval(self.newtext)  
        except SyntaxError or NameError: 
            self.displayArea.delete(0,END) 
            self.displayArea.insert(0,'Invalid Input!') 
        else: 
            self.displayArea.delete(0,END) 
            self.displayArea.insert(0,self.value)
            
    def clearall(self): 
        """when clear button is pressed,clears the text input area"""
        self.displayArea.delete(0,END) 
        
    def squareRoot(self): 
        """squareroot method"""
        self.getandreplace() 
        try: 
            # evaluate the expression using the eval function 
            self.value= eval(self.newtext)  
        except SyntaxError or NameError: 
            self.displayArea.delete(0,END) 
            self.displayArea.insert(0,'Invalid Input!') 
        else: 
            self.sqrtval=math.sqrt(self.value) 
            self.displayArea.delete(0,END) 
            self.displayArea.insert(0,self.sqrtval) 
  
    def square(self): 
        """square method"""
        self.getandreplace() 
        try: 
            #evaluate the expression using the eval function 
            self.value= eval(self.newtext)  
        except SyntaxError or NameError: 
            self.displayArea.delete(0,END) 
            self.displayArea.insert(0,'Invalid Input!') 
        else: 
            self.sqval=math.pow(self.value,2) 
            self.displayArea.delete(0,END) 
            self.displayArea.insert(0,self.sqval) 


# In[4]:


#App Class
class App(Frame):  # Mortgage and Calculator classes'
    
    def __init__(self, master):
        Frame.__init__(self, master)
        mortgage = Mortgage(self)
        mortgage.pack(side=LEFT)
        calculator = Calculator(self)
        calculator.pack(side=RIGHT)


# In[5]:


from tkinter import Tk
root = Tk()
app = App(root)
app.pack()
root.mainloop()


# In[ ]:




