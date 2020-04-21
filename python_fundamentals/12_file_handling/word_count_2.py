sp_chars = '.!?,'
new_list = []
with open('textfiles/sudhan.txt', 'r') as f:
    for line in f:
        line = line.lower().strip()
        for chars_ in sp_chars:
            if chars_ in line:
                line = line.replace(chars_, '')
        line = line.split(" ")
        new_list.append(line)

new_dict = {}
print(new_dict['sudhan'] in new_dict)
# for line in new_list:
#     for word in line:
#         if new_dict[word] in new_dict:
#             new_dict[word] = 0
#         else:
#             new_dict[word] += 1
#
# for item, value in new_dict.items():
#     print(f"{item} presents {value} times")
