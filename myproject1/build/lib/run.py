while True :
    solution = input("What do you want in the calculator Please select (c for calculator, e for equation): ")
    if solution == "c" :
        number1 = int(input(" Please enter number 1: "))
        number2 = int(input("Please enter number 2: "))
        operation = input("Please enter the operation (+, -, *, /): ")
        result = 0
        if operation == "+" :
            result = number1 + number2
            print(f"The answer is {result}")
        elif operation == "-" :
            result = number1 - number2
            print(f"The answer is {result}")
        elif operation == "*" :
            result = number1 * number2
            print(f"The answer is {result}")
        elif operation == "/" :
            if number2 == 0 :
                print("Oh! The selected option is not supported at the moment. Please try again.")
            else :
                result = number1 / number2
                print(f"The answer is {result}")
        else :
            print("Oh! The selected operation is not supported at the moment. Please try again.")

    elif solution == "e" :
        print("Hi")
        numberofs = int(input("Please enter the number of s: "))
        operation = input("Please enter the operation (+, -): ")
        numberafteroperation = int(input("Please enter the number after the operation: "))
        numberafterequal = int(input("Please enter the number after the equal sign: "))
        if operation == "+" :
            afterinputs_afternumbers = numberafterequal - numberafteroperation
            numberofs_number_afterinputs_afternumbers = afterinputs_afternumbers / numberofs
            result = numberofs_number_afterinputs_afternumbers
            print(f"The solution is {result}")
        elif operation == "-" :
            afterinputs_afternumbers = numberafterequal + numberafteroperation
            numberofs_number_afterinputs_afternumbers = afterinputs_afternumbers / numberofs
            result = numberofs_number_afterinputs_afternumbers
            print(f"The solution is {result}")
        else :
            print("Oh! The selected operation is not supported at the moment. Please try again.")

    else:
        print("Oh! The selected option is not supported at the moment. Please try again.")