# Day 12 of 100 Days Of Code

A variable is only available from inside the region it is created. This is called scope.

## Local Scope:
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

## Global Scope:
A variable created in the main body of the Python code is a global variable and belongs to the global scope. Global variables are available from within any scope, global and local.

There is no Block scope in python.  

## Change Global variable inside a function:

You can change the value of global variable inside a function using `global` keyword.

```buildoutcfg
count = 1
def updateCount():
    global count
    count += 1
    print(count)
updateCount()
print(count)

Output:
2
2
```

It's a good to avoid changing global variable inside function.  

You can use `return` keyword instead of using `global` to change global variable inside function.
```buildoutcfg
count = 1
def updateCount():
    print(count)
    return count + 1
count = updateCount()
print(count)

Output:
1
2
```

## Python Constants:

Global scopes are used when declaring constants in python.
Naming for constants will be UPPERCASE separated by underscore('_')
```buildoutcfg
PI = 3.1459
URL = "https://www.google.com"
```