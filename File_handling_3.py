# 3. Write a Python program to count the number of digits in the textfile DIGIT.txt.

with open("DIGIT ") as fl:
    count = 0
    for lines in fl.readlines():
        try:
            for words in lines.rstrip().split():
                for word in words:
                    try:
                        sample = int(word)
                        count += 1

                    except:
                        pass

        except:
            pass

print(f'no.of digits:{count}')