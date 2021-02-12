#!/bash/python
print('#######')
print('PRG-->1 ++Sum of all the items in a list++')
num=[1,2,3]
tot=0
for i in num:
    tot += i
print(tot)

print('\n#######')
print('PRG-->2 ++Sum of all the items in a list++')
num=[1,2,3]
tot=0
print (len(num))
for i in range(len(num)):
    tot +=num[i]
print(tot)

print('\n#######')
print('PRG-->3 ++Smallest number from list++')
num=[1,0,2,3]
out=num[0]
print (len(num))
for i in range(1,len(num)):
    if out<=num[i]:
        continue
    else:
        out=num[i]
print(out)

