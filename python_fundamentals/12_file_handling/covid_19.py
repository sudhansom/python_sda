class DataTable:
    data_dict = {}

    def __init__(self):
        # self.data_dict = {}
        pass

    def read_csv(self, path):
        """ Reads the content from the file of the given path."""
        with open(path, 'r') as file:
            for line in file:
                line = line.strip().split(",")
                if not self.data_dict:
                    for word in line:
                        self.data_dict[word] = []
                else:
                    j = 0
                    for i in self.data_dict:
                        self.data_dict[i].append(line[j])
                        j += 1

    def locate_column(self, column_name):
        """ Returns the values of the given column_name."""
        list_column_name = []
        for key, value in self.data_dict.items():
            if key == column_name:
                list_column_name.extend(value)
        return list_column_name

    def locate_index(self, index_number=0):
        """ Returns the list of data  of one specefic row"""
        list_index_number = []
        list_key, list_value = self.key_value_data()
        for i in list_key:
            print(f"{i:30}", end='')
        print("")
        for i in list_value:
            list_index_number.append(i[index_number])
            print(f"{i[index_number]:30}", end='')
        print("")
        return list_index_number

    def value_counts(self, column_name):
        """Returns the key-value pair dictionary of the given column name"""
        list_column_name = []
        dict_column_name = {}
        list_key, list_value = self.key_value_data()
        i = list_key.index(column_name)
        for j in list_value[i]:
            list_column_name.append(j)
        uniq_values = set(list_column_name)
        for i in uniq_values:
            dict_column_name[i] = list_column_name.count(i)

        return dict_column_name

    def find_index_of_country(self, value):
        """Returns the index of a particular value"""
        occur_times = 0
        column_value = self.locate_column('country')
        start_index = column_value.index(value)
        for i in column_value:
            if i == value:
                occur_times += 1
        # occur_times = column_value.count(value) - 1
        return start_index, occur_times

    def find_total(self, country, status):
        """ gives the total numbes of cases for either 'confirmed cases' or 'deaths' or 'recovered' """
        total = 0.0
        list_key, list_value = self.key_value_data()
        start_index, occur_times = self.find_index_of_country(country)
        col_index = list_key.index(status)

        for i in range(start_index, start_index + occur_times):
            total += float(list_value[col_index][i])
        return total


    def key_value_data(self):
        """ returns the column-list and the value-list  """
        list_key = []
        list_value = []
        for key, value in self.data_dict.items():
            list_key.append(key)
            list_value.append(value)

        return list_key, list_value

    def specific_day_country(self, date, country):
        """ Returns a set of values of specific day of any country"""
        list_key, list_value = self.key_value_data()
        one_day_list = []
        date_column = list_key.index("date")
        country_column = list_key.index("country")
        for i in range(len(list_value[0])):
            if list_value[date_column][i] == date and list_value[country_column][i] == country:
                break
        for j in range(7):
            one_day_list.append(list_value[j][i])
        return one_day_list

    def write_all_data(self):
        list_key, list_value = self.key_value_data()
        with open("textfiles/new_data", 'w') as f:
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

    def filter_data(self):
        """Filters data by deleting some columns"""
        list_key, list_value = self.key_value_data()
        value_list = []
        key_list = ['index', 'date', 'country', 'province/state', 'confirmed', 'deaths', 'recovered']
        list_key.pop(0)
        list_key.insert(0, "index")
        for i, item in enumerate(list_key):
            item = item.lower()
            if item in key_list:
                value_list.append(list_value[i])
        list_key = key_list

        value_list[1], value_list[3] = value_list[3], value_list[1]
        self.data_dict = {}
        for i, keys in enumerate(list_key):
            self.data_dict[keys] = value_list[i]






data1 = DataTable()
data1.read_csv("textfiles/covid-19_data.csv")
# data1.write_all_data()
print(data1.locate_column("index"))
data1.locate_index(74 + 73)
print(data1.value_counts('country'))
print(data1.find_index_of_country("Albania"))
print(data1.find_total("Australia", "recovered"))
print(data1.specific_day_country('2020-02-03', 'Nepal'))

# data2 = DataTable()
# data2.read_csv(("textfiles/newdata.csv"))
# data2.filter_data()
# data2.write_all_data()
