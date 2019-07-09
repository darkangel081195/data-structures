//Implementation of KMP algorithms for doing string search in O(n)
def fail(p):
    length = len(p)
    fail = [0]*length
    k = 0
    j = 1
    while(j<length):
        if p[j]==p[k]:
            fail[j]= k+ 1
            j = j + 1
            k = k + 1
        elif k>0:
            k = fail[k-1]
        else:
            j = j + 1
    return fail

p = input()
t = input()
n,m = len(t),len(p)
j = 0
k = 0
fail = fail(p)
res = 0
while(j<n):
    if(t[j]==p[k]):
        if(k==m-1):
            res = res + 1
            j = j -1
            k = fail[k]
        j = j + 1
        k = k + 1

    elif k>0:
        k = fail[k-1]
    else:
        j = j + 1

print(res)


