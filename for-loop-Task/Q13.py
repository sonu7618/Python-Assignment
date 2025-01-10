# Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types

list=[1,2,3,"d",4,5,"a"]
integer=[]
string=[]
for i in list:
    if isinstance(i,int):
        integer.append(i)
    else:
        string.append(i)
print(f'Integer:{integer}')
print(f'String:{string}')