# def vowels_consonants(s):
#     v=c=0
#     vowels = "aeiouAEIOU"
#     for ch in s:
#         if ch.isalpha():
#             if ch in vowels:
#                 v += 1
#             else:
#                 c += 1
#     return v,c

# print(vowels_consonants("python"))


def vowel(s):
    v=c=0
    vowels="aeiouAEIOU"
    for i in s:
        if i.isalpha():
            if i in vowels:
                v+=1
            else:
                c+=1
    return(v,c)
print(vowel("python"))