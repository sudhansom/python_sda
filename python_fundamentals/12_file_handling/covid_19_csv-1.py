import csv


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
        col_value = dict_key_list.index(column_name)
        column_list = []
        for i in range(len(dict_value_list)):
            column_list.append(dict_value_list[i][col_value])
        return column_list

    def locate_index(self, index_number):
        dict_key_list, dict_value_list = data_table.key_value_list()
        list_at_index = []
        for i in range(len(dict_value_list)):
            if i == index_number:
                list_at_index = dict_value_list[i]
        return list_at_index

    def filter_values(self, column='country', value='Nepal'):
        dict_key_list, dict_value_list = data_table.key_value_list()
        data_country = []
        for i in range(len(dict_value_list)):
            if dict_value_list[i][2] == value:
                data_country.append(dict_value_list[i])
        return data_country

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

column_list = data_table.locate_column('country')
value_at_index = data_table.locate_index(1111)
data_of_country = data_table.filter_values('country', 'Nepal')
count_dict = data_table.value_counts('country')

print("1. What is the number of rows in the dataset?", end='    ')
print(len(column_list))
print("2. What is the number of columns in the dataset excluding the index?", end='   ')
print(len(value_at_index))
print("3. What is the number of recovered in Denmark in the dataset altogether?", end='    ')
data_recovered = data_table.filter_values('country', 'Denmark')
total = 0.0
for i in data_recovered:
    total += float(i[6])
print(total)
print("4. How many times is each day present in the dataset (value counts)?")
count_date = data_table.value_counts('date')
for key, value in count_date.items():
    print(f"{key}     presents   {value} times.")
print("4. How many times is each country present in the dataset (value counts)?")
for key, value in count_dict.items():
    print(f"{key}     presents   {value} times.")
print("6. Which country has the most deaths altogether and how many?", end=' ')

print("9. When did number of confirmed cases in the US reach 1000?", end=' ')
data_confirmed = data_table.filter_values('country', 'US')


def get_element(val):
    return val[1]


data_confirmed.sort(key=get_element)
total = 0
date = ""
for i in data_confirmed:
    total += float(i[4])
    if total >= 1000:
        date = i[1]
        break
print(date)

print("7. What is the maximum of new cases confirmed in Scandinavia (Denmark, Sweden, Norway,Finland) on a single day?")
countries_list = ['Denmark', 'Sweden', 'Norway', 'Finland']
new_cases = [[countries_list[i], "", 0.0] for i in range(len(countries_list))]

for i, country in enumerate(countries_list):
    country_details = data_table.filter_values('country', country)
    max_case = 0
    for item in country_details:
        if float(item[4]) > (new_cases[i][2]):
            new_cases[i][2] = float(item[4])
            new_cases[i][1] = item[1]

for i in new_cases:
    print(f"{i[0]} had {i[2]} cases on date {i[1]}")

