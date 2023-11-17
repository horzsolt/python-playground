def isPalindrome(s):
    return s == s[::-1]

def isPalindrome_iterative(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True