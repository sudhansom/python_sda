import csv


def filter_values(column='country', value='Nepal'):
    dict_key_list, dict_value_list = data_table.key_value_list()
    data_country = []
    for i in range(len(dict_value_list)):
        if dict_value_list[i][2] == value:
            data_country.append(dict_value_list[i])
    return data_country


class DataTable:

    def __init__(self):
        self.data = None

    def read_csv(self, path):
        with open(path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            self.data = [row for row in csv_reader]
        return self.data  # returns list of dictionaries

    def key_value_list(self):
        dict_key_tolist = [key for key in self.data[0]]
        dict_value_tolist = [[] for key in range(len(self.data))]
        for index, items in enumerate(self.data):
            for j in range(len(dict_key_tolist)):
                dict_value_tolist[index].append(self.data[index][dict_key_tolist[j]])
        return dict_key_tolist, dict_value_tolist

    def locate_column(self, column_name):
        dict_key_list, dict_value_list = data_table.key_value_list()
        col_name_list = []
        if type(column_name).__name__ == 'list':
            col_name_list.extend(column_name)
        else:
            col_name_list = [column_name]
        column_list = [[] for col in col_name_list]
        for i in range(len(dict_value_list)):
            for j in range(len(col_name_list)):
                column_list[j].append(dict_value_list[i][dict_key_list.index(col_name_list[j])])
        return column_list

    def ilocate_column(self, col_num):
        dict_key_list, dict_value_list = data_table.key_value_list()
        col_name_list = []
        if type(col_num).__name__ == 'list':
            col_name_list.extend(col_num)
        else:
            col_name_list.append(col_num)
        column_list = [[] for col in col_name_list]
        for i in range(len(dict_value_list)):
            for k, j in enumerate(col_name_list):
                    column_list[k].append(dict_value_list[i][j])
        return column_list

    def locate_index(self, index_number):
        dict_key_list, dict_value_list = data_table.key_value_list()
        list_at_index = []
        if type(index_number).__name__ == 'list':
            list_at_index.extend(index_number)
        else:
            list_at_index.append(index_number)
        column_list = [[] for col in list_at_index]
        for i in range(len(dict_value_list)):
            for k, j in enumerate(list_at_index):
                if i == j:
                    column_list[k].extend(dict_value_list[i])
        return column_list

    def value_counts(self, column_name):
        dict_key_list, dict_value_list = data_table.key_value_list()
        column_list = self.locate_column(column_name)
        uniq_item = set(column_list)
        dict_count = {}
        for item in uniq_item:
            dict_count[item] = column_list.count(item)
        return dict_count


data_table = DataTable()
data_table.read_csv('textfiles/covid-19_data.csv')

# column_list = data_table.locate_column(['index', 'country', 'confirmed', 'date', 'recovered', 'deaths'])

# column_list = data_table.ilocate_column([1, 0, 2])
# for value in column_list:
#     print(value)


# column_list = data_table.locate_index([1, 2, 3000])
# for row in column_list:
#    print(row)
