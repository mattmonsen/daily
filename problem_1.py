#!/usr/bin/python

l = [10, 5, 7, 18];
k = 17;
found = False;

while l:
    pop = l.pop(0);
    for i in l:
        if (pop + i) == k:
            found = True;
            break;

print(found);
