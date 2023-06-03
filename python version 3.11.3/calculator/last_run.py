while True :
    solution = input("What do you want in the calculator Please select ( calculator , equation ) ")
    if solution == "c" :
        number1 = int(input(" Please inter number 1 "))
        number2 = int(input("Please inter number 2 "))
        operation = input("Please inter the operation please select ( + , - , * , / ) ")
        result = 0
        if operation == "+" :
            result = number1 + number2
            print(result)
        elif operation == "-" :
            result = number1 - number2
            print(result)
        elif operation == "*" :
            result = number1 * number2
            print(result)
        elif operation == "/" :
            result = number1 / number2
            print(result)
        else :
            print("Oh ! it's not supported now please retry")
    elif solution == "e" :
        print("Hi")
        numberofs = int(input("Please , inter your number of s "))
        operation = input("Please , inter your operation Please select this ( + , - ) ")
        numberafteroperation = int(input("Please , inter you number after opretion "))
        numberafterequal = int(input("Please , inter you number after equal "))
        if operation == "+" :
            afterinputs_afternumbers = numberafterequal - numberafteroperation
            numberofs_number_afterinputs_afternumbers = afterinputs_afternumbers / numberofs
            result = numberofs_number_afterinputs_afternumbers
            print(f" The solution is {result}")
        elif operation == "-" :
            afterinputs_afternumbers = numberafterequal + numberafteroperation
            numberofs_number_afterinputs_afternumbers = afterinputs_afternumbers / numberofs
            result = numberofs_number_afterinputs_afternumbers
            print(f" The solution is {result}")
        else :
            print("Oh ! it's not supported now please retry")
    else:
        print("Oh ! it's not supported now please retry")