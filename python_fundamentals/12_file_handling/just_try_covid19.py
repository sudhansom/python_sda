my_dict = {}
with open("textfiles/covid-19_data.csv", 'r') as file:
    k = 0
    for line in file:
        if k > 10:
            break
        line = line.strip().split(",")
        if not my_dict:
            for word in line:
                my_dict[word] = []
        else:
            j = 0
            for i in my_dict:
                my_dict[i].append(line[j])
                j += 1
        k += 1



print(my_dict)
