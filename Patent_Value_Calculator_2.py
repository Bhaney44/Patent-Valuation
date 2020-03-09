#Patent Value Calculator

# Widgets:
from tkinter import *
from tkinter.messagebox import *

master = Tk()
label1 = Label(master, text = 'Patent Number', relief = 'groove', width = 15)
label2 = Label(master, text = 'Year Granted', relief = 'groove', width = 15)
label3 = Label(master, text = 'Domestic Ownership', relief = 'groove', width = 15)
label4 = Label(master, text = 'Ownership Size', relief = 'groove', width = 15)
label5 = Label(master, text = 'Prior Art Cited', relief = 'groove', width = 12)
label6 = Label(master, text = 'Citations as Prior Art', relief = 'groove', width = 15)
label7 = Label(master, text = 'Number of Claims', relief = 'groove', width = 15)
label8 = Label(master, text = 'Patent Value', relief = 'groove', width = 15)

entry1 = Entry(master, relief = 'groove', width = 12)
entry2 = Entry(master, relief = 'groove', width = 12)
entry3 = Entry(master, relief = 'groove', width = 12)
entry4 = Entry(master, relief = 'groove', width = 12)
entry5 = Entry(master, relief = 'groove', width = 12)
entry6 = Entry(master, relief = 'groove', width = 12)
entry7 = Entry(master, relief = 'groove', width = 12)

blank1 = Entry(master, relief = 'groove', width = 12)


def patent_value():
    
    def date_value():
        date = int(entry1.get())
        start_value = date - 2020
        date_score = 1/start_value
        return date_score
    
    def domestic_value():
        domestic = int(entry2.get())
        if domestic is 1:
            domestic_score = 1
        else:
            domestic_score = 0.5
        return domestic_score
    
    def owner_size_value():
        owner_size = int(entry3.get())
        if owner_size > 500:
            owner_size_score = 0.5
        elif owner_size > 100:
            owner_size_score = 0.75
        elif owner_size > 5:
            owner_size_score = 0.5
        else:
            owner_size_score = 0.2
        return owner_size_score
    
    def prior_art_value():
        prior_art = int(entry4.get())
        if prior_art > 25:
            prior_art_score = 1.0
        elif prior_art > 15:
            prior_art_score = 0.75
        elif prior_art > 10:
            prior_art_score = 0.5
        else:
            prior_art_score = 0.2
        return prior_art_score
    
    def prior_art_cite_value():
        prior_art_cite = int(entry5.get())
        if prior_art_cite > 25:
            prior_art_cite_score = 1.0
        elif prior_art_cite > 15:
            prior_art_cite_score = 0.75
        elif prior_art_cite > 10:
            prior_art_score = 0.5
        else:
            prior_art_cite_score = 0.25
        return prior_art_cite_score
    
    def claim_value():
        claims = int(entry6.get())
        if claims > 25:
            claim_score = 1.0
        elif claims > 15:
            claim_score = 0.75
        elif claims > 10:
            claim_score = 0.5
        else:
            claim_score = 0.25
        return claim_score
            
    def calculate():
        claim_score = claim_value()
        prior_art_cite_score = prior_art_cite_value()
        prior_art_score = prior_art_value()
        date_score = date_value()
        owner_size_score = owner_size_value()
        domestic_score = domestic_value()
        b = 1/6
        Ans1 = float(prior_art_cite_score) * float(claim_score) *float(date_score) * float(prior_art_score) *float(owner_size_score)  * float(domestic_score)
        Ans11 = Ans1**b
        Ans111 = Ans11 * 1000000
        blank1.insert(0, Ans111)
    calculate()

 
button1 = Button(master, text = 'Calculate Patent Value', relief = 'groove', width = 20, command =patent_value)


#Geometry
label1.grid( row = 1, column = 1, padx = 10 )
label2.grid( row = 1, column = 2, padx = 10 )
label3.grid( row = 1, column = 3, padx = 10 )
label4.grid( row = 1, column = 4, padx = 10 )
label5.grid( row = 1, column = 5, padx = 10 )
label6.grid( row = 1, column = 6, padx = 10 )
label7.grid( row = 1, column = 7, padx = 10 )
label8.grid( row = 1, column = 8, padx = 10 )

entry1.grid( row = 2, column = 1, padx = 10 )
entry2.grid( row = 2, column = 2, padx = 10 )
entry3.grid( row = 2, column = 3, padx = 10 )
entry4.grid( row = 2, column = 4, padx = 10 )
entry5.grid( row = 2, column = 5, padx = 10 )
entry6.grid( row = 2, column = 6, padx = 10 )
entry7.grid( row = 2, column = 7, padx = 10 )
blank1.grid( row = 2, column = 8, padx = 10 )

button1.grid( row = 3, column = 4, columnspan = 2)

#Static Properties
master.title('AI Patent Value Calculator')
