 # 4. Write a function to transferal llines starting with a vowel from ORIGIN.txt to NEW.txt.


def transfer(file1, file2):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    with open(file1)as fl1, open(file2,"w") as fl2:
        for lines in fl1.readlines():
            try:
                if lines.rstrip()[0] in vowels:
                    fl2.write(lines)
            except:
                pass

transfer("ORIGIN", "NEW")




