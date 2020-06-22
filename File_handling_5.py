# 5. Write a Function to read data from a textfile DATA.TXT, and display those words, which are less than 4 characters.


def read(file):
    with open(file) as fl:
        for lines in fl.readlines():
            try:
                for word in lines.rstrip().split():
                    if len(word)<4:
                        print(word)
            except:
                pass

read("Data")




