import csv
import os
print("If this is your first time using,")
print("please ensure that there is a file named")
print('"account.csv" in same directory or folder')
print("as this python file so the program can work.")
print('Type "help" for list of commands.')


while True:
    text = str(input()).lower().split(" ")
    L = []
    if text[0] == "t":
        with open('account.csv', mode='r') as csvfile:
            try:
                float(text[1])
            except ValueError:
                print("Invalid input, value is not a number")
            else:
                if len(text) == 4:
                    reader = csv.reader(csvfile)
                    L = []
                    for row in reader:
                        L.append(row)
                    newlist = []
                    newlist.append(text[1])
                    newlist.append(text[2])
                    newlist.append(text[3])
                    L.append(newlist)
                    with open('account.csv', 'w', newline = '') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerows(L)
                else:
                    print("Invalid input, please follow the format")
    

    elif text[0] == "b":
        with open('account.csv', mode='r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                L.append(row)
            balance = 0
            for i in range (0,len(L)):
                balance += int(L[i][0])
        print("Your balance is: " + str(balance))
        print("Keep it up!")


    elif text[0] == "a":
        with open('account.csv', mode='r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                L.append(row)          
        counter = 0
        printlength = len(L)-100
        if printlength < 0:
            printlength = 0
        print("Value    Transaction   Date")
        for i in range(printlength,len(L)):
            print(L[i])

            
    elif text[0] == "u":
        with open('account.csv', mode='r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                L.append(row)
            try:
                del L[-1]
            except IndexError:
                print("Account is empty! Input a transaction first.")
            else:
                print(L)
                with open('account.csv', 'w', newline = '') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerows(L)

        
    elif text[0] == "stop":
        print("Transactions have been successfully stored.")
        print("Thanks for using my service!")
        break
    elif text[0] == "help":
        print("Commands:")
        print('1. "t [value] [transaction] [Date]"')
        print('For example: "Income 300 salary 01/01/2023" will add 300')
        print('to your balance along with the "salary" sidenote.')
        print('Another example: "Expense -15 lunch" will subtract 15')
        print('from your balance along with the "lunch" sidenote.')
        print('2. "b" will show your remaining money.')
        print('3. "u" will undo your last input')
        print('4. "a" will display your last 100 balance changes')
        print('5. "stop" will stop running this program.')
        print('6. "help" will open this menu.')
        print('Please follow the formats precisely.')
    else:
        print("Bot cannot understand input. Please follow the format.")
        

