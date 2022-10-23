menu=[
    ["eggs","bacon"],
    ["eggs","sausage","bacon"],
    ["eggs","spam"],
    ["eggs","bacon","spam"],
    ["eggs","bacon","sausage","spam"],
    ["spam","sausage","bacon","spam"],
    ["spam","sausage","bacon","spam""tomato","spam",],
    ["spam","eggs","spam","spam","bacon","spam"],
]
for meal in menu:
    for item in meal:
        if item != "spam":
            print(item,end=", ")
    print()
