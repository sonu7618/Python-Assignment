# Given list is [1,2,3,4,5] separate the elements into odd and even categories.

list=[1,2,3,4]
even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(f'Even:{even}')
print(f'Odd:{odd}')
