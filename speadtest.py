a=int(input("enter your first value"))
b=int(input("enter your second value"))
c=int(input("enter your third value"))
avrage=(a+b+c)/3

print(avrage)

if(avrage>a and avrage>b and avrage>c):
    print(avrage," is greater than all values")
elif(avrage>b and avrage>a):
    print(avrage," is greater than ",b," and ",a)
elif(avrage>c and avrage>a):
    print(avrage," is greater than ",c," and ",a)
elif(avrage>b and avrage>c):
    print(avrage," is greater than ",b," and ",c)
elif(avrage>b):
    print(avrage," is greater than ",b)
elif(avrage>a):
    print(avrage," is greater than ",a)
elif(avrage>c):
    print(avrage," is greater than ",c)

