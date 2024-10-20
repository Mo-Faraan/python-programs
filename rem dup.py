""" Python code that removes duplicate elements from an array and returns the length of the remaining array without using sets or any built-in libraries like set(): """
n = list(map(int,input().split(" ")))
n.sort()
ui=0
for i in range(1,len(n)):
    if n[i]!=n[ui]:
        ui+=1
        n[ui]=n[i]
print(ui+1)

