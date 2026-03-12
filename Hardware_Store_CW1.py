masterList = []
data = open('data_file.txt', 'r')
def main():
    option = 1
    while option != 0:
        print('There are 6 options (1-6). Entering 0 exits the code.')
        option = input('which option do you want to run?')

        if option ==1:
            option1()
        elif option ==2:
            option_2()
        elif option ==3:
            option_3()
        elif option == 4:
            option_4()
        elif option== 5:
            option_5()
        elif option== 6:
            option_6()
        else:
            print('Goodbye then.')
        

def option1():
    totalUnits = 0
    totalCost = 0
    masterList = read_Data()
    for x in range(len(masterList)):
        totalUnits += int(masterList[x][3]) + int(masterList[x][4])*2 + int(masterList[x][5])*4
        material = str(masterList[x][0])
        headType = str(masterList[x][1])
        length = int(masterList [x][2])
        costPer50 = float(masterList[x][6])
        totalCost += (totalUnits * float(masterList[x][6]))
        print ('Material:', material,',','headType:',headType,',','Length:',length,',','The total number of units (Per box of 50) are:' ,totalUnits,',','The total value of the stock is:',totalCost)

def option_2():
    masterList = read_Data()
    screwLength60 = 0
    screwLength40 = 0
    screwLength20 = 0

    for x in range(len(masterList)):
        if(int(masterList[x][2]) == 20):
           screwLength20 += int(masterList[x][3]) + int(masterList[x][4]) * 2 + int(masterList[x][5]) * 4
        elif (int(masterList[x][2]) == 40):
              screwLength40 += int(masterList[x][3]) + int(masterList[x][4]) * 2 + int(masterList[x][5]) * 4
        elif (int(masterList[x][2]) == 60):
              screwLength60 += int(masterList[x][3]) + int(masterList[x][4]) * 2 + int(masterList[x][5]) * 4
    print(screwLength60,'\n',screwLength40,'\n',screwLength20)

def option_3():
    list60 = []
    list20 = []
    list40 = []
    length_screw = int(input('Please enter the screw length you wish to purchase (60, 20 or 40)'))
    for x in range(len(masterList)):
        if(int(masterList[x][2]) == 20):
            list20.append(masterList[x])
        elif (int(masterList[x][2]) == 40):
              list40.append(masterList[x])
        elif (int(masterList[x][2]) == 60):
              list60.append(masterList[x])
    if length_screw == 20:
        for x in range(len(list20)):
            print(list20[x])
    elif length_screw == 40:
        for x in range(len(list40)):
            print(list40[x])
    elif length_screw == 60:
        for x in range(len(list60)):
            print(list60[x])
    else:
        print('Please enter a valid screw length!')

        
def option_4():
    print('This is option 4')

def option_5():
    print('This is option 5')

def option_6():
    print('This is option 6')


def read_Data():
        with open("data_file.txt", "r") as dataFile:
            list = []
            for line in dataFile:
                if not line.startswith("#"):
                    line = line.replace("\n", "")
                    list.append(line.split(","))
        return list
main()
