__author__ = 'Lothilius'

import numpy as np
import csv
import sys
import datetime
import json


current_time = datetime.datetime.now().strftime('%H_%M_%Y_%m_%d')

print 'hello world!'
#Create file from array with finaldata.csv as the name and append.
def dataTofile(fname):
    with open(fname) as f:
        content = f.readlines()

    return content


def check_call_number(some_string):
    if some_string[0] == ' ':
        return True
    else:
        return False


def prep_list(some_array):
    ready_array = []
    try:
        call_number = some_array[0].split('          ')
        call_numbers = call_number[0].rstrip()
        ready_array.append(call_numbers)
    except TypeError as e:
        print 'error', sys.exc_info()[0], e, ' ', call_numbers

    title = ' '.join(some_array[1].split())
    ready_array.append(title)
    location_array = some_array[2].split()

    for each in location_array:
        ready_array.append(each)

    return ready_array


#write an array to a file.
def arrayTofile(dataArray, fileName):
    if sys.argv[1] == False:
        fileName = 'reports/' + fileName + '_' + current_time + '.csv'
    else:
        fileName = 'Out/' + fileName + current_time + '.csv'
    print fileName
    with open(fileName, 'w+') as csvfile:
        linewriter = csv.writer(csvfile, delimiter=",")
        for each in dataArray:
            linewriter.writerow(each)
    # print("done")


file_name = sys.argv[1]

content = dataTofile(file_name)
#print content
# for each in content:
#     print [each]

missing_data = np.array([[0, 0, 0, 0, 0, 0]])
item = np.array([])

for each in content:
    if each == '\n':
        pass
    elif check_call_number(each):
        if each[:18] == '               Pro':
            pass
        if each[:17] == '              Pro':
            pass
        elif each[:9] == '      Per':
            pass
        elif each[:33] == '                                M':
            pass
        elif each[:4] == ' cop':
            item = np.append(item, each)
            # i = 0
            # for each in item:
            #     if each[:17] == '              Pro':
            #         print each
            #         item = np.delete(item, i)
            #     i = 1 + i
            #
            # print item

            item = prep_list(item)
            missing_data = np.append(missing_data, [item], axis=0)
            item = np.array([])
        else:
            if each[:22] == '                Title:':
                item = np.append(item, each)
            else:
                try:
                    item = np.append(item[-2], item[-1] + each)
                except IndexError:
                    if each[:18] == '               Pro':
                        pass
                    else:
                        item = np.append(item, each)
    else:
        item = np.append(item, each)

missing_data = np.delete(missing_data, 0, axis=0)

missing_data = missing_data[missing_data[:, 5].argsort()]

def main():
    # while True:
    try:
        if len(sys.argv) <= 1:
            directory = 'inventory_report_'
            arrayTofile(missing_data, directory)
        elif sys.argv[1] == False:
            directory = raw_input('Where would you like to save the data? ')
            arrayTofile(missing_data, directory)
        else:
            directory = 'inventory_report_'
            arrayTofile(missing_data, directory)
    except TypeError as e:
        print 'error', sys.exc_info()[0], e

if __name__ == '__main__':
    main()