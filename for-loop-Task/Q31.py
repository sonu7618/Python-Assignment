# Write a for loop using an if statement, that appends each number to the new list if it's positive. given lst1=[111, 32, -9, -45, -17, 9, 85, -10]

lst=[111,32,-9,-45,-17,9,85,-10]
new_lst=[]
for i in lst:
    if i>0:
        new_lst.append(i)
print(new_lst)