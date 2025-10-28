def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    return sorted(s1) == sorted(s2)

a= "listen"
b = "silent"
if anagram(a,b):
    print("It is anagram")
else:
    print("It is not anagram")