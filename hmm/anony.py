import os
import sys
print ('what is your name')
name = sys.stdin.readline()
print ('what is your name2')
name1 = sys.stdin.readline()
def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches




print(anagramSolution2(name,name1))
