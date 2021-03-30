#Zuri ATM mock Exam

name = input('What is your name?\n')
allowedUsers = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']

if(name in allowedUsers):
    Password = input('Your Password?\n')
    userId = allowedUsers.index(name)
    if(Password == allowedPassword[userId]):
        #Current Tate and Time after loggin
        from datetime import datetime
        #datetime object containing current date and time(copied from https://www.programiz.com/python-programming/datetime/current-datetime)
        now = datetime.now()
        print("Current Date and Time:", now)
        print('Welcome %s' %name)
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')
        selectedOption = int(input('Please Select an Option:'))
        if(selectedOption == 1):
            print('You Selected %s' %selectedOption)
            #receiving input from the user and outputing take your cash
            withdrawalAmount = input("How much would you like to Withdraw:")
            print('take your cash %s')
        elif(selectedOption == 2):
            print('You Selected %s' %selectedOption)
            #receiving input from the user on amount to be deposited and current balance
            currentBalance = 5000
            moneyToBeDeposited = input('How much would you like to Deposit:')
            print('Your Current Balance is:%s' %currentBalance)
        elif(selectedOption == 3):
            print('You Selected %s' %selectedOption)
            #Issue reporting from user and thank you for contacting us message to user
            issuesLogger = input('What issue will you like to report:')
            print('Thank you for contacting us')
        else:
            print('Invalid Option Selected, Please try again')
    else:
        print('Password incorrect, Please try again')
else:
    print('Name not found, Please try again')