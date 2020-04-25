import csv


def filter_values(column='country', value='Nepal'):
    dict_key_list, dict_value_list = data_table.key_value_list()
    data_country = []
    for i in range(len(dict_value_list)):
        if dict_value_list[i][2] == value:
            data_country.append(dict_value_list[i])
    return data_country


def make_temp_csv_file(col_name_list, column_list):
    with open("textfiles/new_temp_csv.csv", 'w') as f:
        for value in col_name_list:
            f.write(value)
            if value != col_name_list[-1]:
                f.write(',')
        f.write('\n')
        for i in range(len(column_list[0])):
            for j, value in enumerate(column_list):
                f.write(column_list[j][i])
                if value != column_list[-1]:
                    f.write(',')
            f.write('\n')


class DataTable:

    def __init__(self):
        self.data = None

    def read_csv(self, path):
        with open(path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            self.data = [row for row in csv_reader]
        # return self  # returns the object of the class...

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

        make_temp_csv_file(col_name_list, column_list)
        obj_dtable = DataTable()
        obj_dtable.read_csv("textfiles/new_temp_csv.csv")

        return obj_dtable

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
        new_column = []
        for i in col_name_list:
            new_column.append(dict_key_list[i])

        make_temp_csv_file(new_column, column_list)
        obj_dtable = DataTable()
        obj_dtable.read_csv("textfiles/new_temp_csv.csv")
        return obj_dtable

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

        new_col = [[] for i in dict_key_list] # formatting the style of data from column_list to new_col
        for row in column_list:
            for i, value in enumerate(row):
                new_col[i].append(value)

        make_temp_csv_file(dict_key_list, new_col)
        obj_dtable = DataTable()
        obj_dtable.read_csv("textfiles/new_temp_csv.csv")
        return obj_dtable

    def value_counts(self, column_name):
        dict_key_list, dict_value_list = data_table.key_value_list()
        column_list = self.locate_column(column_name)
        uniq_item = set(column_list)
        dict_count = {}
        for item in uniq_item:
            dict_count[item] = column_list.count(item)
        return dict_count


data_table = DataTable()
data_table.read_csv('textfiles/newdata.csv')

# column_list = data_table.locate_column(['index', 'country', 'confirmed', 'date', 'recovered', 'deaths'])
# print(data_table is column_list)
# print(len(data_table.data[0]))
# print(len(column_list.data[0]))
# print(type(column_list))

# column_list = data_table.ilocate_column([1, 0, 2])


# column_list = data_table.locate_index([1, 2, 3000])
# for row in column_list.data:
#     print(row)



