def check_sequence(lst):
    if sorted(set(lst)) == lst:
        return 1
    if sorted(set(lst), reverse=True) == lst:
        return -1
    return 0

print(check_sequence([3,2,1]))
print(check_sequence([1,2,3]))
print(check_sequence([1,1,1]))
