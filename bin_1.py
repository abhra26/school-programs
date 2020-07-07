# 1. Program to append or add employee details(Empno, name, address, salary) to binary file
import pickle

def add_to(file, data):
    import pickle
    with open(file,"ab") as fl:
        for i in range(data):
            Empno = int(input("Empno:"))
            name = input("name:")
            address = input("address:")
            salary = int(input("salary:"))
            ls = [Empno,name,address,salary]
            pickle.dump(ls, fl)

# add_to("bin_1_file",3)

f = open("bin_1_file","rb")
while True:
    try:
        line = pickle.load(f)
        print(line)

    except:
        break

f.close()
