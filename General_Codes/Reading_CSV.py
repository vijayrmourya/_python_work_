import csv
import pandas as pd

signal = "Rte_VehStatus_In_100_V_x_RCarHMIManagementSensorInput_V_x_RCarHMIManagementSensorInput.V_x_MasterObjDataModified[0].V_m_ObjectPosX"
case = ['zero', 'nine']
value = ['0', '9']
ind = 0
# opening the CSV file
with open('G:\Z_Python\BOOK.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)
    flag = 0
    # displaying the contents of the CSV file
    for lines in csvFile:
        for i in lines:
            if i == signal:
                print("signal found")
                ind = lines.index(i)
                flag = 1
                break
        print(lines[ind])
        if flag == 1:
            break

    for lines in csvFile:
        for i in range(len(value)):
            # print(type(lines[ind]))
            if value[i] == lines[ind]:
                lines[ind] = case[i]
                print('updated')
    file.close()
