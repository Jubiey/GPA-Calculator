from tkinter import *

root = Tk()
root.title("CSUEB GPA Calculator")
#root.geometry('400x360')

topFrame = Frame(root, bg="turquoise1")
topFrame.pack()                                             #Creating the frames for the GUI

Label1 = Label(topFrame, text="Full Name: ", bg="turquoise1")                #Full Name
Label2 = Label(topFrame, text="No of classes: ", bg="turquoise1")            #No of classes
Labelclass = Label(topFrame, text="Classes", bg="turquoise1")
Labelunits = Label(topFrame, text="No of units", bg="turquoise1")
Labelgrade = Label(topFrame, text="Grade Letter\n(A-, C+)", bg="turquoise1")


entry1 = Entry(topFrame)                                    
entry2 = Entry(topFrame)
entryclass1 = Entry(topFrame)
entryclass2 = Entry(topFrame)
entryclass3 = Entry(topFrame)
entryclass4 = Entry(topFrame)
entryclass5 = Entry(topFrame)
entryclass6 = Entry(topFrame)

entryunits1 = Entry(topFrame)
entryunits2 = Entry(topFrame)                               #Creating Entry boxes for the Full Name, No of classes, Classes, No of units and Grade Letter
entryunits3 = Entry(topFrame)
entryunits4 = Entry(topFrame)
entryunits5 = Entry(topFrame)
entryunits6 = Entry(topFrame)

entrygrade1 = Entry(topFrame)
entrygrade2 = Entry(topFrame)
entrygrade3 = Entry(topFrame)
entrygrade4 = Entry(topFrame)
entrygrade5 = Entry(topFrame)
entrygrade6 = Entry(topFrame)

Label1.grid(row=0, sticky=E)
Label2.grid(row=1, sticky=E)
Labelclass.grid(row=2, column=0)
Labelunits.grid(row=2, column=1)
Labelgrade.grid(row=2, column=2)

entry1.grid(row=0, column=1, pady=5)
entry2.grid(row=1, column=1, pady=10)
entryclass1.grid(row=3, column=0, pady=5, padx=5)
entryclass2.grid(row=4, column=0, pady=5, padx=5)
entryclass3.grid(row=5, column=0, pady=5, padx=5)
entryclass4.grid(row=6, column=0, pady=5, padx=5)
entryclass5.grid(row=7, column=0, pady=5, padx=5)
entryclass6.grid(row=8, column=0, pady=5, padx=5)                           #Places all the Labels and Entry boxes into their respective frames

entryunits1.grid(row=3, column=1, pady=5, padx=5)
entryunits2.grid(row=4, column=1, pady=5, padx=5)
entryunits3.grid(row=5, column=1, pady=5, padx=5)
entryunits4.grid(row=6, column=1, pady=5, padx=5)
entryunits5.grid(row=7, column=1, pady=5, padx=5)
entryunits6.grid(row=8, column=1, pady=5, padx=5)

entrygrade1.grid(row=3, column=2, pady=5, padx=3)
entrygrade2.grid(row=4, column=2, pady=5, padx=3)
entrygrade3.grid(row=5, column=2, pady=5, padx=3)
entrygrade4.grid(row=6, column=2, pady=5, padx=3)
entrygrade5.grid(row=7, column=2, pady=5, padx=3)
entrygrade6.grid(row=8, column=2, pady=5, padx=3)


def calculateGPA():        
    no_of_classes = entry2.get()
    no_of_classes = int(no_of_classes)
    classes = []
    units = []
    grade = []
    gradevalue = [4,3.7,3.3,3,2.7,2.3,2,1.7,1.3,1,0]
    
    classes.append(entryclass1.get())
    classes.append(entryclass2.get())
    classes.append(entryclass3.get())
    classes.append(entryclass4.get())
    classes.append(entryclass5.get())
    classes.append(entryclass6.get())

    units.append(entryunits1.get())
    units.append(entryunits2.get())
    units.append(entryunits3.get())
    units.append(entryunits4.get())                     #Accepting user input from all entry boxes
    units.append(entryunits5.get())
    units.append(entryunits6.get())

    grade.append(entrygrade1.get())
    grade.append(entrygrade2.get())
    grade.append(entrygrade3.get())
    grade.append(entrygrade4.get())
    grade.append(entrygrade5.get())
    grade.append(entrygrade6.get())

    i = 0
    points = 0
    while(i < (no_of_classes)):
        if (grade[i] == "A"):
            unitsint = int(units[i])
            points = (unitsint*gradevalue[0]) + points
        if (grade[i] == "A-"):
            unitsint = int(units[i])
            points = (unitsint*gradevalue[1]) + points
        if (grade[i] == "B+"):
            unitsint = int(units[i])
            points = (unitsint*gradevalue[2]) + points
        if (grade[i] == "B"):
            unitsint = int(units[i])
            points = (unitsint*gradevalue[3]) + points
        if (grade[i] == "B-"):
            unitsint = int(units[i])
            points = (unitsint*gradevalue[4]) + points
        if (grade[i] == "C+"):
            unitsint = int(units[i])                                    #Converting Grade Letters to their respective grade values
            points = (unitsint*gradevalue[5]) + points
        if (grade[i] == "C"):
            unitsint = int(units[i])
            points = (unitsint*gradevalue[6]) + points
        if (grade[i] == "C-"):
            unitsint = int(units[i])
            points = (unitsint*gradevalue[7]) + points
        if (grade[i] == "D+"):
            unitsint = int(units[i])
            points = (unitsint*gradevalue[8]) + points
        if (grade[i] == "D"):
            unitsint = int(units[i])
            points = (unitsint*gradevalue[9]) + points
        if (grade[i] == "F"):
            unitsint = int(units[i])
            points = (unitsint*gradevalue[10]) + points    
        i = i + 1
    if no_of_classes == 3:
        unitstot = int(units[0])+int(units[1])+int(units[2])
    if no_of_classes == 4:
        unitstot = int(units[0])+int(units[1])+int(units[2])+int(units[3])
    if no_of_classes == 5:
        unitstot = int(units[0])+int(units[1])+int(units[2])+int(units[3])+int(units[4])
    if no_of_classes == 6:
        unitstot = int(units[0])+int(units[1])+int(units[2])+int(units[3])+int(units[4])+int(units[5])          #
        
    global GPA
    GPA = points/unitstot
    #print(GPA)
    GPA = round(GPA, 3)
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)
    GPAtext = "Your weighted GPA for this semester is " + str(GPA) + "."
    LabelGPA = Label(bottomFrame, text=GPAtext)
    LabelGPA.grid(row=0, column=1)

    if GPA >= 3.5:
        Labeldean = Label(bottomFrame, text="Congratulations! You will be included on this semester's Dean's List!")
        Labeldean.grid(row=1, column=1)
     
    def destroyGPA():
        bottomFrame.destroy()

    button2 = Button(topFrame, text="Reset", command=destroyGPA)
    button2.grid(row=9, column=2)    

    

button1 = Button(topFrame, text="Calculate GPA", command=calculateGPA)
button1.grid(row=9, column=0)









root.mainloop()
