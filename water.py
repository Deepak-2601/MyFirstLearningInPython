c=""
a=int(input("Please enter the input "))
for m in  range(2,a):
    if(a%m==0):
      c="found"
      break
if (c=="found"):
    print(a,"is not answer prime")
else:
    print(a," is  answer prime")