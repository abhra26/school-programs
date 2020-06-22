# 1. Write a function to open the text file ABC.txt and count the number of words that start with ‘the’, like: the, their, they, them, these etc.


fl = open("ABC","r")
count = 0
lis = ['the', 'The', 'THE']
for line in fl.readlines():
    try:
        for word in line.rstrip().split():
            if word[:3] in lis:
                count += 1
    except:
        pass



fl.close()

print(f'no. of words starting with the : {count}')

