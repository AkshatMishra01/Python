print("here we are playinyg with variable scopes")
x = 2
def variable_func():
    global x
    x= 45
    print(x)
print("x before declaration\n",x)
print("x after declaration")
variable_func()
''' you cannot change the value of a global variable in a function without 
the declaation within a local scope
'''
# code part 2
def scope_func():
    x = 14
    print("value of x after local declaration is:\n",x)
scope_func()
'''nonlocal variable in nested python code'''
# code part 3
def outer():
    y = 6
    print("the value of before non local declaration is\n",y)
    def inner():
        nonlocal y 
        y = 8
        print("the non local variable in python, y is\n",y)
    inner()
outer()
outer()
# code part 4
