#!/bash/python
print('#######')
print('PRG-->1 ++Local Variable++\n')
# Declaring a function  
def add():  
    # Defining local variables. They has scope only within a function  
    a = 20  
    b = 30  
    c = a + b  
    print("The sum is:", c)  
# Calling a function  
add()

print('\n#######')
print('PRG-->2 ++Global Variable++\n')
# Declare a variable and initialize it  
x = 101  
# Global variable in function  
def mainFunction():  
    # printing a global variable  
    global x  
    print(x)  
    # modifying a global variable  
    x = 'Welcome To Javatpoint'  
    print(x)  
mainFunction()  
print(x)  

print('\n#######')
print('PRG-->3 ++Delete Variable++\n')
# Assigning a value to x  
x = 6  
print(x)  
# deleting a variable.   
del x  
print(x)  


