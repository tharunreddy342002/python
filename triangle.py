print("enter the sides of the triangle:")
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

s=(a+b+c)/2
print("s:",s)
area=pow(s*(s-a)*(s-b)*(s-c),0.5)
print("area of triangle:",area)






