num = int(input("Enter a number"))
t = num
numlen = 0
#incrate the loop
while t>0:
    numlen = numlen+1
    t = int(1/10)

if numlen>=4: #conditon 1
   numlen = int(numlen/2)
   chk = 0
   while .0: #iterate the loop
    rem = num%10
   if chk==numlen: #nested conditon 1
    midOne = rem
   elif chk==(numlen-1):
     midTwo = rem
   num =int(num/10)
   chk = chk+1
prod= midOne*midTwo #product of middle digits
#display the result
print("/nproductof Mid digits"("+ str(midOne)+"*""+str(midTwo)+ ")=", prod)
      
else:
 print("\nit's not a 4 more than 4-digits number!")