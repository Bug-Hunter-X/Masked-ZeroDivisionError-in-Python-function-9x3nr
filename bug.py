def function_with_uncommon_error(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
    else:
        return x / y

result = function_with_uncommon_error(10, 0)
print(result) # ZeroDivisionError

result = function_with_uncommon_error(0, 20)
print(result) # Output: 20

result = function_with_uncommon_error(10, 2)
print(result) # Output: 5.0