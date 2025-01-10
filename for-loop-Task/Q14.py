# Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.

list=[1,2,3,4,"a","b"]
integer=[]
string=[]
for i in list:
    if isinstance(i,int):
        integer.append(i)
    else:

        string.append(i)
print(f'Integer:{integer}')
print(f'String:{string}')