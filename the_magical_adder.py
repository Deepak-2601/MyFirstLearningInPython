user_input = input("please enter any three numbers: ")
split_tokens = user_input.split(",")
int_tokens = []
for string in split_tokens:
    int_tokens.append(int(string))
a, b, c = int_tokens
results = a + b - c
print(results)
