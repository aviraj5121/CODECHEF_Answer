A=[]
for i in range(0,10):
    z=int(input())
    A.append(z)
for i in range(1,len(A)):
    Key = A[i]
    j=i-1
while(j>=0 and Key<A[j]):
    j=j-1
    A[j+1] = Key

for i in range(len(A)):
    print(A[i])