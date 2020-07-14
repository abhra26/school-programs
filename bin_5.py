import pickle

class stock:
    def __init__(self,n,p):
        self.Name = n
        self.Price = p

    def show(self):
        print(f'{self.Name}@{self.Price}')


#
# f = open("STOCK.DAT","ab")
# i = 'y'
# while i == 'y':
#     sample = stock(input('enter name:'), int(input('enter price:')))
#     pickle.dump([sample.Name, sample.Price], f)
#     i = input("y/n:")
#
# f.close()

def costly(file_name):
    import pickle
    f = open(file_name,"rb")
    while True:
        try:
            line = pickle.load(f)

            if line[-1]>1000:
                print(line)
            else:
                pass

        except:
            break

costly("STOCK.DAT")


# f = open("STOCK.DAT","rb")
# while True:
#     try:
#         line = pickle.load(f)
#         print(line)
#
#     except:
#         break
#
# f.close()



