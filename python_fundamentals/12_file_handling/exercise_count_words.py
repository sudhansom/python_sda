all_words = []
sp_chars = ".?!,"
with open('textfiles/sudhan.txt', 'r') as file:
    for line in file:
        clean_line = line.strip().lower().split(" ")
        for word in clean_line:
            for i in word:
                if i in sp_chars:
                    word = word.replace(i, '')
            all_words.append(word)


unique_words = set(all_words)
new_dict = {}
with open('textfiles/abc.csv', 'w') as f:
    for word in unique_words:
        print(f"{word}:: {all_words.count(word)}")
        new_dict[word] = all_words.count(word)
        f.write(f" {word}:: {all_words.count(word)} \n")

print(new_dict)






