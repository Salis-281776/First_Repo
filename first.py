"""Ask user the year enter and write a program to vlidate the year a leap year

year =int(input("Enter the year"))


if year%400==0 or (year%100!=0 and year%4==0):
    print("true")
else:
    print("False")"""

"""ashish has decided to take out a 30 year fixed rate mortage lone of 500,000 with RBL bank ,
bajaj finance and bit coin traiding. the intrest rate is 5 % and the monthly payment is 2684.11
Calculate the total amount that ashish has to pay over the life of the mortage
import math
loan_amount=500000
intrest=0.05
years=30
total_paid=0
monthly_pay=2684.11
i=1

while loan_amount>0:
    loan_amount=loan_amount*(1+intrest/12)-monthly_pay
    total_paid+=monthly_pay
    i+=1
print(total_paid,i)

print(math.factorial(5))
"""

"""



s=input("enter the string")
if s==s[-1::-1]:
    print("String is palindrome")
else:
    print("String is not palindrome")

"""

msg=" Learning Python for Data   Engineering "
vowels="aeiouAEIOU"
v_count=0
c_count=0
space=0
s_count=0
words=0

for i in msg:
    if i in vowels:
        v_count+=1
    else:
        c_count+=1
for i in msg:
    if ord(i)==32 or i==" ":
        space+=1
msg=msg.strip()
for i in range(0,len(msg)):
    if msg[i]==" ":
        if msg[i+1]==" ":
            s_count+=0
        else:
            s_count+=1
print("vowels= ",v_count)
print("consonent= ",c_count-s_count)
print("words= ",s_count+1)
print("space= ",space)
    
        

























    
  
        
    
