#!/bash/python
print('#######')
print('PRG--> ++To check types++\n')

a=10
b="Hi Python"
c = 10.5
print(type(a))
print(type(b))
print(type(c))

print('\n#######')
print('PRG--> ++Numbers(Integer, Fload and Complex)++\n')

a=5  
print("The type of a", type(a))  
b=40.5  
print("The type of b", type(b))  
c = 1+3j
print("The type of c", type(c))  
print("C is a complex number:", isinstance(1+3j,complex))  

