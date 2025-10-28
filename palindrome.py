def is_palindrome(s):
    s=s.lower()
    return s == ''.join(reversed(s))

def is_palindrome_slice(s):
    s=s.lower()
    return s == s[::-1]

print(is_palindrome('Madam'))
print(is_palindrome_slice('Madam'))