#2. Write a Python program to count all lines in the file ABC.txt having ‘a’ as the last character.

with open("ABC") as fl:
    count = 0
    for lines in fl.readlines():
        try:
            if lines.rstrip().split().pop() == 'a':
                count += 1
        except:
            pass


print(f' no. of lines ending with a :{count}')


