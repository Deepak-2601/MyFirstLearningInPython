avilable_parts=["mouse","monitor","keyboard","mouse mat","hdmi cable"]
valid_choice= []
for i in range(1,len(avilable_parts) + 1):
    valid_choice.append(str(i))
    print(valid_choice)
    current_choice="-"
    computer_parts=[]
while current_choice != "0":
      if current_choice in valid_choice:
          print("Adding {}".format(current_choice))
          index=int(current_choice)-1
          chosen_parts=avilable_parts[index]
          computer_parts.append(chosen_parts)
      else:
          print("Please choose the option from the given list")
          for number,part in enumerate(avilable_parts):
              print("{0}: {1}".format(number + 1,part))
      current_choice=input()
print(computer_parts)
