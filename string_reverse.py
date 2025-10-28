class reverse:
    def rev_string(s):
        ch =""
        for i in s:
            ch = i + ch
        return ch

    def rev_string2(s):
        return s[::-1]

    def rev_string3(s):
        s = reversed(s)
        a = "".join(s)
        return a

    print(rev_string("hello"))
    print(rev_string2("Hello"))
    print(rev_string3("Hello"))

