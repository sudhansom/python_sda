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

    def ilocate_column(self, icolumn):
        dict_key_list, dict_value_list = data_table.key_value_list()
        col_name_list = []
        if type(icolumn).__name__ == 'list':
            col_name_list.extend(icolumn)
        else:
            col_name_list = [icolumn]
        column_list = [[] for col in col_name_list]
        for i in range(len(dict_value_list)):
            for j in range(len(col_name_list)):
                column_list[j].append(dict_value_list[i][j])
        return column_list

    def locate_index(self, index_number):
        dict_key_list, dict_value_list = data_table.key_value_list()
        list_at_index = []
        for i in range(len(dict_value_list)):
            if i == index_number:
                list_at_index = dict_value_list[i]
        return list_at_index

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

column_list = data_table.ilocate_column([0, 1, 2, 3])
for i in range(20):
    for value in column_list:
        if column_list[-1] == value:
            print(value[i], end='')
        else:
            print(value[i], end=', ')
    print()
