
import pickle

def bin_file(file_name, data):
    import pickle
    with open(file_name,"ab") as fl:
        for i in range(data):
            roll = int(input("enter roll_no:"))
            name = input("enter name:")
            cl = int(input("enter class:"))
            sec = input("enter section:")
            mob = int(input("enter mobile_no.:"))
            ls = [roll,name,cl,sec,mob]
            pickle.dump(ls, fl)

# bin_file("student.dat",3)


def delete_rec(roll,file_name):
    import pickle
    import os
    lis = []
    f = open(file_name, "rb")
    while True:
        try:
            line = pickle.load(f)
            if line[0]!=roll:
                lis.append(line)
            else:
                pass
        except:
            break

    f.close()

    os.remove(file_name)

    f = open(file_name,"ab")
    for i in lis:
        pickle.dump(i, f)

    f.close()

delete_rec(2, "student.dat")

f = open("student.dat","rb")
while True:
    try:
        line = pickle.load(f)
        print(line)

    except:
        break

f.close()