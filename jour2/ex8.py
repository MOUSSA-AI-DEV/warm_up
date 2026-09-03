L = [7, 23, 5, 23, 7, 19, 23, 12, 29, 7, 5]

rept={}

for i in range(len(L)):
    counte=0
    for j in range(len(L)):
        if L[i]==L[j]:
            counte=counte+1
    rept[L[i]]=counte

print (rept)  