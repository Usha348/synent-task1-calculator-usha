print("Simple Calculator")

num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))

print("1. Add\n2. Subract\n3. Multiply\n4. Divide")

choice = input("Enter choice: ")
if choice=='1':
    print("Result:", num1+num2)
elif choice=='2':
    print("Result:", num1-num2)
elif choice=='3':
    print("Result:", num1*num2)
elif choice=='4':
    if num2!=0:
        print("Result:", num1/num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")