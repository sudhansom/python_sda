class DataTable:
    data_dict = {}

    def __init__(self):
        pass


    def read_csv(self, file_path):
        with open(file_path, 'r') as file:
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
        list_key =[]
        list_value = []
        for key, value in self.data_dict.items():
            list_key.append(key)
            list_value.append(value)
        for i in list_key:
            print(f"{i:30}", end="")
        print("")
        for i in list_value:
            # for j in range(len(i)):
            print(f"{i[19165]:30}", end="")
            #    break
        print(f"value is : \n {list_value[2][19165]}")
        print(f"{list_key[2]}")



data1 = DataTable()
data1.read_csv("textfiles/covid-19_data.csv")


"""
 a = 0
        occurrence = 0
        while len(column_list) > 0:
            country = column_list[0]
            while column_list and column_list[occurrence:].count(column_list[0]):
                occurrence = column_list.count(country)
                del column_list[0:occurrence]
                if column_list:
                    country = column_list[0]
                if not new_value:
                    for j, value in enumerate(value_list):
                            new_value.append(value_list[j][a: a + occurrence])

                else:
                    for j, value in enumerate(value_list):
                        new_value[j].extend(value[a: a + occurrence])
                a += occurrence
                occurrence = 0
                
                
                 key_list, value_list = self.key_value_data()
        column_list = self.locate_column("country")
        new_dict = {}
        new_value = []
        for key in key_list:
            new_dict[key] = []
            
            -----------------------------------------------------------------------------
             # llist = []
        # value_list = []
        # for i in range(len(new_value)):
        #     for value in new_value:
        #         if not value_list:
        #             for j in value:
        #                 #llist.append(j)
        #                 value_list.append(j)
        #         else:
        #             for j in value:
        #                 value_list.extend(llist)
        #                 llist = []
        #
        # print(value_list[0])
        #







        # occurrence

        # self.data = {}
        # if not self.data:
        #     for key in key_list:
        #         self.data[key] = []
        # j = 0
        # for item in self.data:
        #     self.data[item].extend(new_value[j])
        #     j += 1
        # for item, key in self.data.items():
        #     print(f"{key} ::    {value}")

"""