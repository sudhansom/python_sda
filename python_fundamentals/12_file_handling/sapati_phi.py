"""
Index    Date    Country    Province    Confirmed    Deaths    Recovered
  0       1         2          3            4          5           6

Note that the province of Netherlands
    "Bonaire, Sint Eustatius and Saba"
contains an additional ',' which might mess up the col if using the split() function

- a solution here is, when reading the file, is to remove this comma:
    ...
    for c in ["Bonaire, Sint Eustatius and Saba"]:
        line = line.replace(c, "Bonaire Sint Eustatius and Saba")

The same with
    "Korea, South"
"""


class DataTable:

    def __init__(self):
        self.data = None

    def read_csv(self, path) -> list:
        with open(path) as f:
            self.data = []
            for i, line in enumerate(f):
                if i == 0:
                    continue
                line = line.rstrip()

                for c in ["Bonaire, Sint Eustatius and Saba"]:
                    line = line.replace(c, "Bonaire Sint Eustatius and Saba")

                for c in ["Korea, South"]:
                    line = line.replace(c, "South Korea")

                line = line.split(",")
                self.data.append(line)
            return self.data

    def locate_column(self, column_name: int) -> list:
        column = []
        for row in self.data:
            column.append(row[column_name])
        return column

    def locate_index(self, index_name):
        for row in self.data:
            if row[0] == str(index_name):
                return row

    def filter_values(self, column_name: int, value: str) -> list:
        lst = []  # new list
        for row in self.data:
            if row[column_name] == str(value):
                lst.append(row)
        return lst

    def value_counts(self, column_name: int) -> dict:
        dictionary = {}
        for row in self.data:
            if row[column_name] not in dictionary:
                dictionary[row[column_name]] = 0
            dictionary[row[column_name]] += 1
        return dictionary


# Tasks: 1. Functionality (1-6)

translate = {
    'index': 0,
    'date': 1,
    'country': 2,
    'province': 3,
    'confirmed': 4,
    'deaths': 5,
    'recovered': 6,
}

mydata = DataTable()
mydata.read_csv("textfiles/covid-19_data.csv")

for i in mydata.data:
    print(i)
    if i[0] == '20':
        break
print()

print(mydata.locate_column(translate['index']))
print(mydata.locate_column(translate['date']))
print()

print(mydata.locate_index(200))
print()

dk_data = mydata.filter_values(translate['country'], 'Denmark')
for i in dk_data:
    print(i)
print()

country_count = mydata.value_counts(translate['country'])
print(country_count)
for i in country_count:
    print(i, country_count[i])
print()
# =========================================================================
# II. Analysis
print("My Solutions", end="")
print("=" * 75)
# ===============================================================================================

# 1. What is the number of rows in the dataset?
print("1. The length of the dataset is:", len(mydata.data))

# ===============================================================================================

# 2. What is the number of columns in the dataset excluding the index?
print("2. The length of the column, excluding the index column, is:", len(mydata.data[0]) - 1)

# ===============================================================================================

# 3. What is the number of recovered in Denmark in the dataset altogether?
result = 0
for i in range(len(dk_data)):
    result += float(dk_data[i][translate['recovered']])
print("3. The number of recovered in Denmark is:", int(result))
print()

# ===============================================================================================

# 4. How many times is each day present in the dataset (value counts)?
print(f"4. Each day is present the following times")
day_count = mydata.value_counts(translate['date'])
for i in day_count:
    print(f"\t{i} is present {day_count[i]} times")
print()

# ===============================================================================================

# 5. How many times is each country present in the dataset?
print("5. Each country is present the following times:")
for i in country_count:
    print(f"\t{i:25} {country_count[i]}")
print()

# ===============================================================================================

# 6. Which country has the most deaths altogether and how many?
# dictionary to store the country-death pair
country_deaths = {}
for i in mydata.data:
    if i[translate['country']] not in country_deaths:
        country_deaths[i[translate['country']]] = 0
    country_deaths[i[translate['country']]] += float(i[translate['deaths']])  # converting to float (so increment works)

# converting the dictionary into a list
death_list = []
for i in country_deaths:
    death_list.append([i, country_deaths[i]])


# a function to return the second element of the two elements passed in the parameter
def sortSecond(val):
    return val[1]


print("6. The country that has the most deaths altogether is:")
death_list.sort(key=sortSecond, reverse=True)
# print('\t', death_list)  # print the whole list (descending order)
print('\t', death_list[0])
print()


# ===============================================================================================
# 7. What is the maximum of new cases confirmed in Scandinavia (Denmark, Sweden, Norway, Finland) on a single day?
# 10.1 - 7.1 (extra) - What are the data for that day?


def max_confirmed_in_1day(new_data: list, value: int, name: str = "Country_name"):
    # create a list of confirmed cases in a country
    confirmed_cases = []
    for i in new_data:
        confirmed_cases.append(float(i[value]))

    # sort the list and find and get the max confirmed case value
    confirmed_cases.sort()
    max_confirmed_in_a_day   = confirmed_cases[-1]  # max value of confirmed cases in a day

    for i in new_data:
        if float(i[value]) == max_confirmed_in_a_day:
            print(f"7./10.1 - {name}, highest confirmed cases in a single day: {int(max_confirmed_in_a_day)}")
            print(f"\t{i}")
            return i  # data


dk_data = mydata.filter_values(translate['country'], 'Denmark')
swe_data = mydata.filter_values(translate['country'], 'Sweden')
nor_data = mydata.filter_values(translate['country'], 'Norway')
fin_data = mydata.filter_values(translate['country'], 'Finland')

max_confirmed_in_1day(dk_data, translate['confirmed'], name='Denmark')
max_confirmed_in_1day(swe_data, translate['confirmed'], name='Sweden')
max_confirmed_in_1day(nor_data, translate['confirmed'], name='Norway')
max_confirmed_in_1day(fin_data, translate['confirmed'], name='Finland')
print()

# ===============================================================================================

# 8. Which country in the dataset had its first confirmed case the latest?
print("8. ________________")






# ===============================================================================================
# 9. When did number of confirmed cases in the US reach 1000?

us_data = mydata.filter_values(translate['country'], 'US')

# the US province is not defined so we can just search in an increased order
for i in us_data:
    if float(i[translate['confirmed']]) > 1000:
        print("9. US confirmed cases reached 1000 on")
        print(f"\t{i}")
        break
print()

# ===============================================================================================
# 10. (optional) Come up with 3 other questions like these and find the answers to them in the data.

# 10.2 How many new cases are there in every country on the latest date?
# convert the list (column) for dates into a unique list (list -> set -> list)
unique_dates = list(set(mydata.locate_column(translate['date'])))
# a set makes the datatype unordered so we must sort it
unique_dates.sort(reverse=True)  # descending order

# print(unique_dates)
# print(len(unique_dates))

print("10.2. How many new cases are there on every country on the latest date:")
latest_date = unique_dates[0]
for i in range(len(mydata.data)):
    # check all data with the latest date, which country had its first confirmed case
    if mydata.data[i][translate['date']] in latest_date and float(mydata.data[i][translate['confirmed']]) > 0:
        print("\t", mydata.data[i])

# ===============================================================================================











