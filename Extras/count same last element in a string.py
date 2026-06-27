def count_same_element(s,i,j,n):
    count = 0
    if n == 0:
        return 0
    if n == 1:
        return 1

    ans = count_same_element(s,i,j-1,n-1) + count_same_element(s,i+1,j,n-1) + count_same_element(s,i+1,j-1,n-2)

    if s[i] == s[j]:
        count += 1
    print(ans)