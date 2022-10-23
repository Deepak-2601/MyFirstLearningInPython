a_file = "Hello.csv"
m1 = open(a_file, "a")
m1.write("Learn Artificial Intelligence")
m1.close()

m1 = open(a_file, "r")
print(m1.read())
m1.close()
