# def armstrong(num):
#     n = num
#     digits= len(str(num))
#     total = 0
#     while n > 0:
#         digit = n % 10
#         total += digit ** digits
#         n//=10
#     return total==num
    
# print(armstrong(153))


def armstrong(num):
    n = num
    digits = len(str(num))
    total = 0
    while n > 0:
        digit = n%10
        total += digit ** digits
        n//=10
    return total == num

print(armstrong(153))
print(armstrong(256))