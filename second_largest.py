class Second_large:
    def second_largest(lst):
        lst.sort()
        return lst[-2]
    
    def second_largest2(lst):
        first = second = float('-inf')
        for n in lst:
            if n > first:
                second = first
                first = n
            elif first > n > second:
                second = n
        return second

    lst = [2,10,0,100,40,50,90,70]
    print(second_largest(lst))
    print(second_largest2(lst))