# 7. Write a program to copy a textfile “source.txt” onto “target.txt” barring with the lines staring with a “@” sign.


with open("source") as fl1, open("target","w") as fl2:
    for lines in fl1.readlines():
        try:
            if lines.rstrip()[0] != "@":
                fl2.write(lines)
        except:
            pass
        