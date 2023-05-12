#1 Ask the user their name and out Hello and their name that has been input
name = input("What is your name?")
print("Hello", name)

#Getvtwo number from the user and add them together  
num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
print("When we add it ,it becomes :" , num1 + num2 )

#write a program that output all number 1to 10

for i in range(1, 11):
 print (i)

# in two steps
numbers= list(range(1, 11)) 

for i in numbers:
  print(i)

# write a program to get all number  from a number that user set
my_num= int(input("Enter a number you want us to count till:"))
count = []
for i in range(1, my_num+1):
  count.append(i)
print ("the counting till given number  is ", count)



