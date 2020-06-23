# 1. Write a function to open the text file ABC.txt and count the number of words that start with ‘the’, like: the, their, they, them, these etc.

def read_it(file):
    fl = open(file,"r")
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
    return count

print(f'no. of words starting with the : {read_it("ABC")}')

