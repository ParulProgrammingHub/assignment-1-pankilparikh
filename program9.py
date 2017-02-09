a1=float(input(“SUBJECT1=”))
a2= float(input(“SUBJECT2=”))
a3= float(input(“SUBJECT3=”))
a4= float(input(“SUBJECT4=”))
a5= float(input(“SUBJECT5=”))
avg=a1+a2+a3+a4+a5
mean=avg/5
pr=(avg*100)/500
print(“TOTAL=”,avg”)
print(“MEAN=”,mean)
print(“PERCENTAGE=”,pr,”%”)
if(pr<=35):
	print(“RESULT:FAIL”)
else:
	print(“RESULT=PASS”)
