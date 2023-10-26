num1 = 11
num2 = num1

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

# num2 points to the same address as num1
# num2 is not creating a separate variable with the same value as num1
print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))


# num2, when updated to 22, creates a new var w/ new value
# This can happen because integers are immutable
num2 = 22

print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)
print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))



dict1 = {
    'value':11
}

dict2 = dict1

print("Before value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)
print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict2['value'] = 22

print("After value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)
print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

# This happens because the value of dict2 was changed. Strings are muteable.
# dict2 is still = to dict1, so if that is the case and the value in dict2 was changed, then dict1 must also change.
# that's why it's still pointing to the same address as before.

dict3 = {
    'value': 33
}

dict2=dict3

dict1 = dict2

# all 3 are now pointing to dict 3
# the original value of dict1 is collected via garbage collection
