#!/usr/bin/python

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

def prod_func(l):
    print(l);
    prod = 1;
    new = [];
    for i in l:
        prod = prod * i;

    for i in l:
        new.append(prod/i);

    return new;

ret = prod_func([1,2,3,4,5]);
print(ret);
print("");

ret = prod_func([3,2,1]);
print(ret);
print("");

ret = prod_func([5,4,6,2]);
print(ret);
print("");
