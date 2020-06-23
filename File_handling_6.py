# 6. Write a program to copy all lines that do not start with a lower case letter from the first file to the second file.

def copy(file1,file2):
    with open(file1) as fl1, open(file2,"w") as fl2:
        for lines in fl1.readlines():
            try:
                if lines.rstrip()[0].isupper():
                    fl2.write(lines)

            except:
                pass

copy("ORIGIN", "CHILD_FILE")





