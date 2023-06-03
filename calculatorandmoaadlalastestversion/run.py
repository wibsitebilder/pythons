print("Hi")
while True :
    sure = input("What do you want please select ( c of calculator _ m of moaadla ) ")
    if sure == "c" :
        number1 = float(input("Please Enter Number 1 "))
        operation = input("Please Enter operation please select ( + _ - _ * _ / ) ")
        number2 = float(input("Please Enter Number 2 "))
        if operation == "+" :
            result = number1 + number2
            print(float(result))
        elif operation == "-" :
            result = number1 - number2
            print(float(result))
        elif operation == "*" :
            result = number1 * number2
            print(float(result))
        elif operation == "/" :
            result = number1 / number2
            print(float(result))
        else :
            print("I'm sorry it's not supported now please retry")
    elif sure == "m" :
        numberofs = 0
        operation = 0
        numberafteropeartion = 0
        numberafterequal = 0
        result1 = 0
        result2 = 0
        result = 0
        numberofs = float(input("Please Enter a coefficient of x "))
        operation = input("please Enter the operation after x please select (+ / -) ")
        numberafteropeartion = float(input("Please Enter a second number after operation "))
        numberafterequal = float(input("Please Enter a number after equal "))
        if operation == "+" :
            result1 = numberafterequal - numberafteropeartion
            result2 =    result1 /    numberofs
            result =    result2
            print(result)
        elif operation == "-" :
            result1 =    numberafterequal +    numberafteropeartion
            result2 =    result1 /    numberofs
            result =    result2
            print(result)
        elif operation == "*" :
            result1 =    numberafterequal /    numberafteropeartion
            result2 =    result1 /    numberofs
            result =    result2
            print(result)
        elif operation == "/" :
            result1 =    numberafterequal *    numberafteropeartion
            result2 =    result1 /    numberofs
            result =    result2
            print(result)
        else :
            print("I'am sorry it's not supported now please retry")
    else :
        print("I'am sorry it's not supported now please retry")