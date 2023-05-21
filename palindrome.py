def isPalindrome(s):
    return s == s[::-1]


# Driver code
s = input("enter anything")
ans = isPalindrome(s)

if ans:
    print("This is a Palindrome")
else:
    print("This is not a Palindrome")
