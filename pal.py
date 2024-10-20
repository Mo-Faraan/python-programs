""" A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise. """
a = input()
i=0
j=len(a)-1
f=0
if len(a)==0:
    print("pal")
else:
    while i<=j :
        if a[i].isalnum()!=True:
            i+=1
        elif a[j].isalnum()!=True :
            j-=1
        else:
            if a[i].lower()!=a[j].lower():
                print("not pal")
                f=1
                break
            i+=1
            j-=1
if f==0:
    print("pal")