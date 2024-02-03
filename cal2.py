print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice=int(input())
if choice==1:
   number=int(input("numbers" ))
   for x in range(number):
      element=int(input())
   sum=0
   for x in range(number):
      sum=sum + x
   print(f"the total sum is :{sum} ")



choice=int(input())
if choice==2:
   number=int(input("numbers" ))
   for x in range(number):
      element=int(input())
   sub=0
   for x in range(number):
      sub=sub - element

   

choice=int(input())
if choice==3:
   number=int(input("numbers" ))
   for x in range(number):
      element=int(input())
   mul=1
   for x in range(number):
      mul=mul*element
   print(f"the total Multiplication is {mul}")

