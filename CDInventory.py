#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# ormerodl, 2020-Aug-11, Updated File for Module05 Homework
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of dictionaries to hold data
# TODO replace list of lists with list of dicts
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

# 5. Exit the program if the user chooses so
    if strChoice == 'x':
        break

# TODO Add the functionality of loading existing data
    if strChoice == 'l':
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID':lstRow[0],'CD Title':lstRow[1], 'Artist':lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        pass

# 2. Add data to the table (2d-list) each time the user wants to add data
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'CD Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
        print('\n')

# 3. Display the current data to the user each time the user wants to display the data
    elif strChoice == 'i':
        print('{:<5} {:<35} {:<35}'. format('ID', 'CD Title', 'Artist'))
        print('-'*75)
        for row in lstTbl:
            print('{:<5} {:<35} {:<35}'. format(row['ID'], row['CD Title'], row['Artist']))
        print('\n')

# TODO Add functionality of deleting an entry
    elif strChoice == 'd':
        delInput = input('Enter ID you want to delete: ')
        for i in range(len(lstTbl)):
            if lstTbl[i]['ID'] == delInput:
                del lstTbl[i]
                break
        pass

    # 4. Save the data to a text file CDInventory.txt if the user chooses so
    elif strChoice == 's':
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

