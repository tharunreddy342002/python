n=int(input("enter the number to check armstrong or not:"))
temp=n
count=0
sum=0
while temp>0:
    temp=temp//10
    count=count+1
temp=n
while temp>0:
    digit=temp%10
    sum=sum+digit**count
    temp=temp//10
if n==sum:print(n,"number is armstrong") 
else:print(n,"number is not an armstrong")   
    