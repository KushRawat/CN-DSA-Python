def checkPalindrome(s, si, ei):
    if si <= ei:
        return
    
    checkPalindrome(s, si + 1, ei - 1)
    while si <= ei:
        if s[si] != s[ei]:
            return "false"
        if s[si] == s[ei]:
            si = si + 1
            ei = ei - 1
        
        