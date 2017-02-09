principle=int(input(“enter the principle amount:”))
rate=int(input(“enter the rate:”))
time=int(input(“enter the time:”))
n=int(input(“enter the N:”))
def  compound_interest(principle,time,rate,n):
   r=(rate/100)
P=principle*(1+r/n)**(n*time)
Print(“total compound interest:”,P)
compound_interest(principle,time,rate,n)

