list = [1,2,3,6,8]
print("The largest no in list :", max(list))

list1 = [2,4,3,7,5]   #using for loop
largest=list1[0]
for large in list1:
    if large > largest:
        largest=large
print("The largest no in list : ",largest)

list3 = [23,45,34,27,12]   #sorting
list3.sort()
smallest=min(list3)
largest=max(list3)
print("largest no:",largest)
print("smallest no:",smallest)