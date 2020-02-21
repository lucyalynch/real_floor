def realfloor(x):
    if x<=0:
        result = x
    if x >= 1 and x <=14:
        result = x-1
    if x > 15:
        result = x-2
    return result

print(realfloor(3))
print(realfloor(7))
print(realfloor(20))
print(realfloor(1))
print(realfloor(-6))