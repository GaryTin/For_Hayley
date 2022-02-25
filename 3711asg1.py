def get_min(A,start,end)->int:
    m = int ((start +end)/2)

    if (m+1>len(A)-1 or (A[m]<A[m+1] ) and (m-1<1 or A[m-1]>A[m] )):
        return A[m]
    elif (A[m-1]<A[m]):
        return get_min(A,start,m-1)
    else:
        return get_min(A, m+1, end)

if __name__== "__main__":
    A=[9,5,4,6,8,12,14]
    print(get_min(A,0,len(A)-1))
    A = [1,2,3,4,5]
    print(get_min(A, 0, len(A) - 1))
    A = [6,5,4,3,2]
    print(get_min(A, 0, len(A) - 1))
    A = [4,3,5,6,7]
    print(get_min(A, 0, len(A) - 1))