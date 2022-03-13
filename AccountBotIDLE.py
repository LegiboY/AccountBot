import csv
import os
print("Hi! I am AccountBot, and I speak English.")
print("If this is your first time using,")
print("please ensure that there is a file named")
print('"account.csv" in the same directory or folder')
print("as this python file so the program can work.")
print('Type "help" for list of commands.')


#Read data from csv file
L=[]
with open('account.csv', mode='r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                L.append(row)

#Empty list debug
if L == [[]]:
    L = []


#Start program
while True:
    text = str(input()).lower().split(" ")

    
    #Transaction inputted
    if text[0] == "t":
        try:
            float(text[1])
        except ValueError:
            print("Invalid input, value is not a number")
        else:
            if len(text) == 4:
                newlist = []
                newlist.append(text[1])
                newlist.append(text[2])
                newlist.append(text[3])
                L.append(newlist)
                print("Transaction noted")
            else:
                print("Invalid input, please follow the format")
    

    #Balance requested
    elif text[0] == "b":
        balance = 0
        for i in range (0,len(L)):
            balance += int(L[i][0])
        print("Your balance is: " + str(balance))
        print("Keep it up!")

        
    #Account logs requested
    elif text[0] == "a":       
        counter = 0
        printlength = len(L)-100
        if printlength < 0:
            printlength = 0
        print("Value    Transaction   Date")
        for i in range(printlength,len(L)):
            print(L[i])


    #Undo requested     
    elif text[0] == "u":
        try:
            del L[-1]
        except IndexError:
            print("Account is empty! Input a transaction first.")
        else:
            print("Latest transaction has been removed.")


    #Save requested
    elif text[0] == "save":
        with open('account.csv', 'w', newline = '') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(L)
            print("Changes have been saved.")


    #Stop requested   
    elif text[0] == "stop":
        print("Transactions have been successfully stored.")
        print("Thanks for using my service!")
        break


    #Help requested
    elif text[0] == "help":
        print("Commands:")
        print('1. "t [value] [transaction] [date]"')
        print('For example: "t 300 salary 01/01/2023" will add 300')
        print('to your balance along with the "salary" sidenote,')
        print('along with the date of 01/01/2023.')
        print('Another example: "t -15 lunch 21/06/2023" will subtract 15')
        print('from your balance along with the "lunch" sidenote,')
        print('along with the date of 21/06/2023.')
        print('2. "b" will show your remaining money.')
        print('3. "u" will undo your last input')
        print('4. "a" will display your last 100 balance changes')
        print('5. "stop" will stop running this program.')
        print('6. "help" will open this menu.')
        print('7. "save" will store the changes into the file.')
        print('Please follow the formats precisely.')

    #Message not understood    
    else:
        print("Bot cannot understand input. Please follow the format.")
        

