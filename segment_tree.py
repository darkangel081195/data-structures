""" Segment tree is used mainly for providing answer to range queries, for example lets take an array [1 5 2 4 3]
  suppose you want to find the sum between index 0-4 you can find it throug looping from 0 to 4 and adding each 
  value. This will take at most O(n) time and for updating a particular index to a certain value it will take O(1)
  time since you can directly change the value using index. But if the number of range queries very high then the 
  total complexity is O(QN) which is very high if Q is near 10^5. This is where segment tree comes into picture.
  Using segment tree you can do both query and update in logN time"""

def construct(node,start,end):
    if(start==end):
        tree[node] = arr[start]
        return 
    
    mid = (start+end)//2
    construct(2*node,start,mid)
    construct(2*node+1,mid+1,end)
    tree[node] = tree[2*node] + tree[2*node+1]

def update(node,start,end,idx,val):
    if(start==end):
        arr[idx] = val
        tree[node] = val
        return
    mid = (start+end)//2
    if(start <= idx and idx<=mid):
        update(2*node,start,mid,idx,val)
    else:
        update(2*node+1,mid+1,end,idx,val)
    tree[node] = tree[2*node] + tree[2*node+1]


def query(node,start,end):
    if(r<start or l> end):
        return 0

    if (l==start and r==end):
        return(tree[node])
    
    mid = (start+end)//2
    p1 = query(2*node,start,mid)
    p2 = query(2*node+1,mid+1,end)
    return(p1+p2)    

    





n = int(input())
arr = list(map(int,input().split()))
tree=[0]*(2*n+2)
construct(1,0,n-1)
print(tree)
for _ in range(int(input())):
    q = input().strip().split()
    if q[0] == 'q':
        l = int(q[1])
        r = int(q[2])
        print(query(1,0,n-1))
    else:
        idx = int(q[1])
        val = int(q[2])
        update(1,0,n-1,idx,val)
        print(arr)
    