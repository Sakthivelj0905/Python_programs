def missing_no(lst):
    n = len(lst) + 1
    total = n * (n+1) // 2
    return total - sum(lst)

print(missing_no([1,2,4,5,6]))