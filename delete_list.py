data=[10,20,120,220,310,400,300,545,600,550,765,760,100,500,320,600,755,250,180,290,900]
min_valid=100
max_valid=200
stop=0
for index,value in enumerate(data):
   if value>=min_valid:
       stop=index
       break
print(stop)
del data[:stop]
print(data)
start=0
for index in range(len(data)-1,-1,-1):
    if data[index]<=max_valid:
        start=index+1
        break
print(start)
del data[start:]
print(data)