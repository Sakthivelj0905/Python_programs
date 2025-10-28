# without using set
def remove_duplicates(lst):
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    return res

print(remove_duplicates([1,2,2,3,3,3,4,4,4,4]))

def remove_duplicates(s):
    res=[]
    for i in s:
        if i not in res:
            res.append(i)
            ch ="".join(res)
    return ch

print(remove_duplicates("hello"))

def remove_duplicates1(s):
    ch = set(s)
    return "".join(ch)

print(remove_duplicates1("hello"))