# dictionary

student = {
    "id1":
    {
        "name":"Sara",
        "age": 12,
        "subject":[ 'maths' ,'science' ,"CS"]
    },
    "id2": 
    {   "name":"Kenyatta",
        "age": 14,
        "subject": ['maths', 'science', 'english']
    },
    "id3":
    {
        "name":"Sara",
        "age": 12,
        "subject":[ 'maths' ,'science' ,"CS"]
    },
    "id4": 
    {   "name":"Kenyatta",
        "age": 14,
        "subject": ['maths', 'science', 'english']
    }
  
}

new_dic = {}
for key,value in student.items():
    if value not in new_dic.values():
        new_dic[key] = value

print("the dictionart without duplicates")
print(new_dic)