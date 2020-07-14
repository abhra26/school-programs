
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
            marks = int(input("enter marks:"))
            ls = [roll,name,cl,sec,mob,marks]
            pickle.dump(ls, fl)

# bin_file("Student.dat", 3)


def update_rec(roll,file_name):
    import pickle
    import os
    lis = []
    f = open(file_name, "rb")
    while True:
        try:
            line = pickle.load(f)
            if line[0]==roll:
                print('please update record')
                roll = int(input("enter roll number:"))
                name = input("enter name:")
                cl = int(input("enter class:"))
                sec = input("enter section:")
                mob = int(input("enter mobile_no.:"))
                marks = int(input("enter marks:"))
                lis.append([roll, name, cl, sec, mob, marks])
                continue
            else:
                lis.append(line)


        except:
            break

    f.close()
    os.remove(file_name)

    f = open(file_name,"ab")
    for i in lis:
        pickle.dump(i, f)

    f.close()

update_rec(3, "Student.dat")

f = open("Student.dat","rb")
while True:
    try:
        line = pickle.load(f)
        print(line)

    except:
        break

f.close()
