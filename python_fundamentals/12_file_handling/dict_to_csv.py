import csv

dict_data = {'id': ['1', '2', '3'],
             'Column1': [33, 25, 56],
             'Column2': [35, 30, 30],
             'Column3': [21, 40, 55],
             'Column4': [71, 25, 55],
             'Column5': [10, 10, 40], }
csv_file = "textfiles/temp.csv"
try:
    with open(csv_file, 'w') as f:
        fieldnames = [key for key in dict_data]
        print(','.join(fieldnames))
        f.write(','.join(fieldnames))
        f.write("\n")
        # for i in range(len(dict_data)):
        for i in range(len(dict_data[fieldnames[0]])):
            for key, value in dict_data.items():
                if key == fieldnames[-1]:
                    print(value[i], end='')
                    f.write(str(value[i]))
                else:
                    print(value[i], end=',     ')
                    f.write(str(value[i]))
                    f.write(",")
            print()
            f.write("\n")


except IOError:
    print("Error...")