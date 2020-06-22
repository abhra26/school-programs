# 8. Write a program to count the number of special characters like ‘, ? , /,#,%,@,&,*, (),{, etc)in the text file “SPE.txt”

with open("SPE") as fl:
    count = 0
    for line in fl.readlines():
        for word in line.rstrip().split():
            for letter in word:
                if letter.isalpha() == False:
                    if letter.isdigit() == False:
                        if letter.isalnum() == False:
                            count += 1

print(f'no.of special charectars: {count}')
