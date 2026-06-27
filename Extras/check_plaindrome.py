def check_palindrome(st,s,e):
    if e < s:
        return True
    if st[e] == st[s]:
        return check_palindrome(st,s+1,e-1)
    return False