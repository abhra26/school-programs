# 1. Program to append or add employee details(Empno, name, address, salary) to binary file

def add_to(file, data):
    import pickle
    with open(file,"ab") as fl:
        for i in range(data):
            Empno = (input("Empno:"))
            name = input("name:")
            address = input("address:")
            salary = (input("salary:"))
            ls = Empno + ' ' + name + ' ' + address + ' ' + salary + '\n'
            pickle.dump(ls, fl)

add_to("bin_1_file",5)