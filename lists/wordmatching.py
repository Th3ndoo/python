# program to print the first and last character same
def count_list(list1):
    count = 0
    new=[]
    for word in list1:
        if len(word) >1:
            if word[0] == word[-1]:
                new.append(word)
                count+=1

    print(new)
    print(f"the eleent which has first and last character same are {count}")


list1 = ['bob' , 'indigo' , 'mom' , 'rise' , 'excuse']

count_list(list1)