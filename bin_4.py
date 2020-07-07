
import pickle

def bin_file(file_name, data):
    import pickle
    with open(file_name,"ab") as fl:
        for i in range(data):
            s_adno = input('enter admission no:')
            s_name = input('enter name:')
            percent = float(input('enter percent:'))
            ls = [s_adno,s_name,percent]
            pickle.dump(ls, fl)

bin_file("STUDENT.DAT", 3)

def show_rec(file_name):
    import pickle
    f = open(file_name,"rb")
    while True:
        try:
            line = pickle.load(f)
            if line[2] > 75:
                print(line)
            else:
                pass

        except:
            break


show_rec("STUDENT.DAT")

f = open("STUDENT.DAT","rb")
while True:
    try:
        line = pickle.load(f)
        print(line)

    except:
        break

f.close()