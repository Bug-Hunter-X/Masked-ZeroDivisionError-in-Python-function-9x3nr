def function_with_uncommon_error_fixed(x, y):
    if y == 0:
        return float('inf') if x > 0 else float('-inf') if x < 0 else 0 
    else:
        return x / y

result = function_with_uncommon_error_fixed(10, 0)
print(result) # Output: inf

result = function_with_uncommon_error_fixed(0, 20)
print(result) # Output: 0.0

result = function_with_uncommon_error_fixed(10, 2)
print(result) # Output: 5.0