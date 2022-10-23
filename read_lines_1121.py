a_file = "file_operation/read"
x = open(a_file, "r")
q = len(x.readlines())
print(q)
x.close()
