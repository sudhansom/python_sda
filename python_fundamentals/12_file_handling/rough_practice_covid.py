class DataTable:

    def __init__(self):
        from collections import OrderedDict
        self.data = OrderedDict()

    def read_csv_file(self, file_path):
        """
        reads a csv file and saves it in data as a dictionary values.
        :param file_path:
        :return:
        """
        with open(file_path, 'r') as file:
            for i, line in enumerate(file):
                line = line.replace("\"", '')
                line = line.replace('Bonaire, Sint Eustatius and Saba', 'Bonaire Sint Eustatius and Saba')
                line = line.replace('Korea, South', 'Korea South')
                line = line.strip().lower().split(",")
                if i == 0:
                    line.pop(0)
                    line.insert(0, 'index')
                if not self.data:
                    for word in line:
                        self.data[word] = []
                else:
                    j = 0
                    for item in self.data:
                        self.data[item].append(line[j])
                        j += 1


    def organize_data(self):

        """ 
        organizing data... from positions to serially...
        """
        key_list, value_list = self.key_value_data()
        new_value = []
        for i in range(len(value_list[1])):
            new_value.append([])
            for value in value_list:
                new_value[i].append(value[i])

        from operator import itemgetter, attrgetter
        new_value.sort(key=itemgetter(1))






    def key_value_data(self):
        """
        takes the dictionary and seperates the keys and the values in lists
        :return:
        """
        key_list = []
        value_list = []
        for key, value in self.data.items():
            key_list.append(key)
            value_list.append(value)
        return key_list, value_list

    def filter_data(self):
        """keeps the given files in proper format and deletes the given column if necessary"""
        key_list, value_list = self.key_value_data()
        for i, item in enumerate(key_list):
            print(f"{i} -- > {item}", end=', ')
        print("")
        user_input = int(input("Which column do you want to delete..? Enter the number :  "))
        key_list.remove(key_list[user_input])
        value_list.remove(value_list[user_input])
        self.data = {}
        for key in key_list:
            self.data[key] = []
        j = 0
        for key in self.data:
            self.data[key].extend(value_list[j])
            j += 1

    def locate_column(self, column):
        """
        returns the given column values....
        :param column:
        :return:
        """
        key_list, value_list = self.key_value_data()
        column = key_list.index(column)
        column_list =[]
        for i in range(len(value_list[column])):
            column_list.append(value_list[column][i])
        return column_list

    def locate_index(self, index_value):
        """Returns the given row value..."""
        key_list, value_list = self.key_value_data()
        value_at_index = []
        for value in value_list:
            value_at_index.append(value[index_value])
        return value_at_index

    def filter_values(self, column, value):
        """" returns the specific column for example column= country and value = "Denmark"  """
        key_list, value_list = self.key_value_data()
        specific_value = {}
        column = key_list.index(column)
        index_value = value_list[column].index(value)
        occurence = value_list[column].count(value)
        for key in key_list:
            specific_value[key] = []

        for i in range(index_value, index_value + occurence):
            j = 0
            for key in specific_value:
                specific_value[key].append(value_list[j][i])
                j += 1
        return specific_value

        # for i in range(index_value, index_value + occurence):
        #     for j in range(len(value_list)):
        #         print(value_list[j][i], end='  ')
        #     print("")

    def value_counts(self, column):
        ''' counts the repetition of values in a given column and returns a dict value'''
        key_list, value_list = self.key_value_data()
        uniq_list_column = set(value_list[key_list.index(column)])
        count_dict = {}
        for item in uniq_list_column:
            count_dict[item] = value_list[key_list.index(column)].count(item)

        return count_dict

    def write_all_data(self):
        ''' writes data to a csv file'''
        list_key, list_value = self.key_value_data()
        with open("textfiles/new_data.csv", 'w') as f:
            for i in list_key:
                if i in [2, 3]:
                    f.write(f"{i:30}")
                else:
                    f.write(f"{i:26}")
            f.write("\n")
            for i in range(len(list_value[1])):
                for j in range(7):
                    if j == 3 or j == 2:
                        f.write(f"{list_value[j][i]:30}")
                    else:
                        f.write(f"{list_value[j][i]:24}")
                f.write("\n")
            f.write("\n")



data_table = DataTable()
data_table.read_csv_file("textfiles/newdata-08.csv")
data_table.filter_data()
#column_list = data_table.locate_column('country')
# print(data_table.locate_index(55))
#specific_value = data_table.filter_values("country", "France".lower())
# count_dict = data_table.value_counts("country")
#print(column_list)
#data_table.write_all_data()
data_table.organize_data()


