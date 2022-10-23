a_file = "hello.csv"
with open(a_file,"w") as write_file:
    write_file.write("About Pearson")
    write_file.close()
with open(a_file,"r") as read_file:
    print(read_file.read())
    read_file.close()