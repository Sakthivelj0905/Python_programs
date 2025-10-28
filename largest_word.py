def largest_word(s):
    words = s.split()
    return max(words,key=len)

print(largest_word("Welcome to Programming "))