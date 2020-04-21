from itertools import islice
def file_read(fname):
    with open(fname, 'r') as txt:
        txt = txt.readlines()
        txt[0].strip()
        print(txt[0])
        # for i, line in enumerate(txt):
        #     if i > len(txt) - 5:
        #         print(f"{i: }  {line}", end='')


file_read('textfiles/abc.csv')