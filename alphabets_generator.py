
import sys
import os
dict = {0 : " _+", 1 : "1", 2 : "abc", 3 : "def", 4 : "ghi",
        5 : "jkl", 6 : "mno", 7 : "pqrs", 8 : "tuv", 9 : "wxyz"}
lis = [list(dict.get(x)) for x in range(0, 10)]
"""
the above line generate the list of values
eg: [[' ', '_', '+'], ['1'], ['a', 'b', 'c']....['w', 'x','y', 'z']]
"""
mob_num = list(input("enter mobile number: "))
num = [int(x) for x in mob_num]#convert list of strings to list of integers
phonekey = [lis[x] for x in num]#re-arranging the list as per phone number
res = ["".join([a,b,c,d,e,f,g,h,i,j]) for a in phonekey[0] for b in phonekey[1]
 for c in phonekey[2] for d in phonekey[3] for e in phonekey[4]
 for f in phonekey[5] for g in phonekey[6] for h in phonekey[7]
 for i in phonekey[8] for j in phonekey[9]]

for x in res:
    print(x)
