import sums
import diff
import product
import division

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user 
choice = input("Enter choice(1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", sums(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", diff(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", product(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", division(num1,num2))
else:
   print("Invalid input")
