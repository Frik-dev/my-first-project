# ZERODIVISION ERROR
try:
    division = 10 / 0
except ZeroDivisionError:
    print("frikist u know u can't divide a number by 0")

# ASSERTION ERROR
try:
    num = int(input("enter the number"))
    assert num % 2==0 # it works like if statements
    print("it is even")
except AssertionError:
    print("not even")

# ATTRIBUTE ERROR
try:
    number = 10
    number.apppend(5)
except AttributeError:
    print("failure of attribute assignment")

# GeneratorExit
numbers = [1,2,3,4,5]
def counter(xarray):
    try:
        for num in xarray:
            yield num
    except GeneratorExit:
        print("there was generator exit")
        return

x = counter(numbers)
for all in x:
    print(next(x))
    x.close()

# checking all built-in exceptions in python
print(dir(locals()['__builtins__']))


