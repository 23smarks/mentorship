from array import *

columnIndex = 0

def getPasswordTime(str):
    password_table = [['Instantly','Instantly','Instantly','Instantly','Instantly','Instantly','Instantly','Instantly','1 sec','5 secs','52 secs','9 mins','1 hour','14 hours','6 days'],
                    ['Instantly','Instantly','Instantly','Instantly','Instantly','Instantly','3 secs','1 min','32 mins','14 hours','2 weeks','1 year','27 years','713 years','18k years','481k years'],
                    ['Instantly','Instantly','Instantly','1 sec','28 secs','24 mins','21 hours','1 month','6 years','332 years','17k years','898k years','46m years','2bn years','126bn years'],
                    ['Instantly','Instantly','Instantly','2 secs','2 mins','2 hours','5 days','10 months','53 years','3k years','202k years','12m years','779m years','48bn years','2tn years'],
                    ['Instantly','Instantly','Instantly','4 secs','5 mins','6 hours','2 weeks','3 years','226 years','15k years','1m years','77m years','5bn years','380bn years','26tn years']]

    password_length = 0

    password = str

    def containsLowercase(password):
        lowercaseCount = 0
        for element in password:
            if (element.islower()==True):
                lowercaseCount +=1
        if lowercaseCount > 0:
            return True
        else:
            return False
            
    def containsUppercase(password):
        uppercaseCount = 0
        for element in password:
            if (element.isupper()==True):
                uppercaseCount +=1
        if uppercaseCount > 0:
            return True
        else:
            return False

    def containsNumbers(password):
        numberCount = 0
        for element in password:
            if (element.isnumeric()==True):
                numberCount +=1
        if numberCount > 0:
            return True
        else:
            return False

    def containsSymbols(password):
        symbolCount = 0
        for element in password:
            if (element.isalnum()==False):
                symbolCount +=1
        if symbolCount > 0:
            return True
        else:
            return False

    if((containsNumbers(password)==True) and (containsLowercase(password)==False) and (containsUppercase(password)==False) and (containsSymbols(password)==False)):
        # Numbers Only
        columnIndex = 0
    elif((containsNumbers(password)==False) and (containsLowercase(password)==True) and (containsUppercase(password)==False) and (containsSymbols(password)==False)):
        # Just Lowercase Letters
        columnIndex = 1
    elif((containsNumbers(password)==False) and (containsLowercase(password)==True) and (containsUppercase(password)==True) and (containsSymbols(password)==False)):
        # Upper and Lowercase Letters
        columnIndex = 2
    elif((containsNumbers(password)==True) and (containsLowercase(password)==True) and (containsUppercase(password)==True) and (containsSymbols(password)==False)):
        # Numbers, Upper and Lowercase Letters
        columnIndex = 3
    elif((containsNumbers(password)==True) and (containsLowercase(password)==True) and (containsUppercase(password)==True) and (containsSymbols(password)==True)):
        # Numbers, Upper and Lowercase Letters, Symbols
        columnIndex = 4
    else:
        columnIndex = 50
        
    if(len(password)==4):
        rowIndex = 0
    elif(len(password)==5):
        rowIndex = 1
    elif(len(password)==6):
        rowIndex = 2
    elif(len(password)==7):
        rowIndex = 3
    elif(len(password)==8):
        rowIndex = 4
    elif(len(password)==9):
        rowIndex = 5
    elif(len(password)==10):
        rowIndex = 6
    elif(len(password)==11):
        rowIndex = 7
    elif(len(password)==12):
        rowIndex = 8
    elif(len(password)==13):
        rowIndex = 9
    elif(len(password)==14):
        rowIndex = 10
    elif(len(password)==15):
        rowIndex = 11
    elif(len(password)==16):
        rowIndex = 12
    elif(len(password)==17):
        rowIndex = 13
    elif(len(password)==18):
        rowIndex = 14
    else:
        rowIndex = 50
    # ADD ELSE STATEMENT
    if ((columnIndex < 50) and (rowIndex < 20)):
        return password_table[columnIndex][rowIndex]
    else:
        return "Not Supported"
   
