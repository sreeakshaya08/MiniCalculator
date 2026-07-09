import add
import sub
import mult
import div

while True:
    print("select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("enter choice(1/2/3/4/5): ")
    if choice in ('1', '2', '3', '4','5'):
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        if choice == '1':
            print(a, "+", b, "=", add.add(a,b))
        elif choice == '2':
            print(a, "-", b, "=", sub.sub(a,b))
        elif choice == '3':
            print(a, "*", b, "=", mult.mult(a,b))
        elif choice == '4':
            print(a, "/", b, "=", div.div(a,b))
        else:
            print("Invalid input. Please enter a valid choice.")
       

