#!/usr/bin/python

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

def sum_func(l, k):
    print(l);
    print(k);
    found = False;

    while l:
        pop = l.pop(0);
        for i in l:
            if (pop + i) == k:
                found = True;
                break;
    
    return found;

#l = [10, 5, 7, 18];
#k = 17;

ret = sum_func([10,5,7,18], 17);
print(ret);
print("");

ret = sum_func([10,5,7,18], 16);
print(ret);
print("");

ret = sum_func([10,5,7,18,75,1,15], 16);
print(ret);
print("");

ret = sum_func([], 16);
print(ret);
print("");

ret = sum_func([1,2,3,4,5], 9);
print(ret);
