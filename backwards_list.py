data=[10,30,20,100,750,108,65,22,107,105,200,312,110]
min_valid=100
max_valid=200
#for index in range(len(data)-1,-1,-1):
top_index=len(data)-1
for index,value in enumerate(reversed(data)):
    if (value<min_valid) or (value>max_valid):
      print(top_index-index,value)
      del data[top_index-index]
print(data)
