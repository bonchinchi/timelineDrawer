from tkinter import *
import tkinter
from subprocess import call
import datetime
import time

bigFontName = ("Arial bold", 15)
fontName = ("Arial", 13)
secondFontName = ("Arial", 12)

class myButton(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self.pressedCounter = 0
        self.representer = 0

class timeLine():
    def __init__(self, root):
        self.root = root
        self.timline()

    def timline(self):
        self.root.rowconfigure([0,1,2], weight=2)
        self.root.columnconfigure([0,1], weight=2)
        thisFrame = Frame(self.root)
        thisFrame.grid(row=0, column=0, sticky=N+S+E+W)
        # 7x7
        thisFrame.rowconfigure([0,1,2,3,4,5,6], weight=1)
        thisFrame.columnconfigure([0,1,2,3,4,5,6], weight=1)
        i = 0
        global btn
        btn = [0 for x in range(49)]
        for row_index in range(7):
            for col_index in range(7):
                # Set card image
                # Create button
                btn[i] = myButton(thisFrame, width=5, height=5, borderwidth=1,bg = "white", command=lambda i=i: self.pressedButton(i))
                btn[i].grid(row=row_index, column=col_index, sticky=N+S+E+W)
                i = i+1

        newFrame = Frame(self.root)
        newFrame.grid(row=0, column=1, sticky=N+S+E+W)
        programName = Label(newFrame, text='Timeline Drawer',font = bigFontName)
        programName.grid(row=0, column=1,padx=10, pady=50)

        label1 = Label(newFrame, text='Enter the day:',font = fontName)
        label1.grid(row=1, column=1,padx=10, pady=10)
        date = tkinter.StringVar()
        entry = tkinter.Entry(newFrame, textvariable=date)
        date.set("")
        entry.grid(row=2, column=1,padx=10, pady=10)

        label2 = Label(newFrame, text='Enter the month:',font = fontName)
        label2.grid(row=3, column=1,padx=10, pady=10)
        date2 = tkinter.StringVar()
        entry2 = tkinter.Entry(newFrame, textvariable=date2)
        date2.set("")
        entry2.grid(row=4, column=1,padx=10, pady=10)

        label3 = Label(newFrame, text='Enter the year:',font = fontName)
        label3.grid(row=5, column=1,padx=10, pady=10)
        date3 = tkinter.StringVar()
        entry3 = tkinter.Entry(newFrame, textvariable=date3)
        date3.set("")
        entry3.grid(row=6, column=1,padx=10, pady=10)

        startDrawer = Button(newFrame, text='Start drawing',borderwidth=1, bg='green',fg='white',font = secondFontName,command=lambda date=date,date2=date2,date3=date3: self.drawer(date,date2,date3))
        startDrawer.grid(row=7, column=1)



    def pressedButton(self, x):
        btn[x].pressedCounter = btn[x].pressedCounter + 1
        if btn[x].pressedCounter%2!=0:
            btn[x]['bg'] = "blue"
            btn[x].representer = 1
        else:
            btn[x]['bg'] = "white"
            btn[x].representer = 0


    def drawer(self,date,date2,date3):
        thisDay = int(date.get())
        thisMonth = int(date2.get())
        thisYear = int(date3.get())
        print(thisDay)
        # representation of our letters
        myList = [[btn[0].representer, btn[1].representer, btn[2].representer, btn[3].representer, btn[4].representer, btn[5].representer, btn[6].representer],
                 [btn[7].representer, btn[8].representer, btn[9].representer, btn[10].representer, btn[11].representer, btn[12].representer, btn[13].representer],
                 [btn[14].representer, btn[15].representer, btn[16].representer, btn[17].representer, btn[18].representer, btn[19].representer, btn[20].representer],
                 [btn[21].representer, btn[22].representer, btn[23].representer, btn[24].representer, btn[25].representer, btn[26].representer, btn[27].representer],
                 [btn[28].representer, btn[29].representer, btn[30].representer, btn[31].representer, btn[32].representer, btn[33].representer, btn[34].representer],
                 [btn[35].representer, btn[36].representer, btn[37].representer, btn[38].representer, btn[39].representer, btn[40].representer, btn[41].representer],
                 [btn[42].representer, btn[43].representer, btn[44].representer, btn[45].representer, btn[46].representer, btn[47].representer, btn[48].representer],]

        finalString=[]
        # setting the beginning date
        thisDay = thisDay + 1
        beginDate = datetime.datetime(thisYear, thisMonth, thisDay)

        finalString.append(myList)

        # array to store dates
        myDates = []

        tempDate = beginDate - datetime.timedelta(days=1)

        for k in range(len(finalString)):
            for j in range(len(finalString[k][0])):
                for i in range(len(finalString[k])):
                    if finalString[k][i][j] == 1:
                        # append the day to myDates
                        myDates.append(tempDate.strftime("%Y-%m-%d"))
                        # increase the day by one
                        tempDate += datetime.timedelta(days=1)
                    else:
                        # increase the day by one
                        tempDate += datetime.timedelta(days=1)

            tempDate += datetime.timedelta(days=7)

        iter = 0
        ###########################                    CHANGE THE FOLLOWING!        ####################################################
        ################################################################################################################################
        # changethe line with the forked repository HTTPS for example: git remote add origin <https://github.com/"username"/"repository".git>
        call('git remote add origin https://github.com/bonchinchi/drawInGitHubTimeline.git', shell=True)
        ################################################################################################################################
        # commiting loop
        while (iter < 6):
            for i in range(len(myDates)):
                call('git commit --date=' + myDates[i] + ' --allow-empty -m "test"', shell=True)
            iter += 1

            # pushing
            call('git push -u origin master', shell=True)



if __name__ == '__main__':
    root = Tk()
    root.geometry("500x500+600+200")
    timeLine(root)
    root.mainloop()