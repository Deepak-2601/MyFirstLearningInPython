my_intro = {'Name': "Deepak", 'age': '22', 'address' : "India"}
def search_dict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'Sorry,the value does not exist'


print(search_dict(my_intro, '22'))