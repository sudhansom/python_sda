import time

dict_num = {}


def expensive_function(num):
    if num in dict_num:
        return dict_num[num]

    print("calculating...")
    time.sleep(1)
    result = num * num
    dict_num[num] = result
    return result


print(expensive_function(4))
print(expensive_function(14))
print(expensive_function(40))
print(expensive_function(4))
print(expensive_function(14))
print(expensive_function(4))
print(expensive_function(40))
