d_file = "hello.csv"
l1 = open(d_file, "r")
datas = l1

for i in datas:
    if  'Name' in i:
        print(i)
