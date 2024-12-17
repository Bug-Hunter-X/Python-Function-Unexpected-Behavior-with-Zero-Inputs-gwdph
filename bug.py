def function_with_uncommon_error(a, b):
    if a == 0:
        return b  # Correct handling of a == 0
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error(0, 0)
print(result)  # This will return 0, which might not always be expected