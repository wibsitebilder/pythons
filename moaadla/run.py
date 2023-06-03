while True :
    import sofnumber
    sofnumber.numberofs = float(input("Please Enter a coefficient of x "))
    sofnumber.operation = input("please Enter the operation after x please select (+ / -) ")
    sofnumber.numberafteropeartion = float(input("Please Enter a second number after operation "))
    sofnumber.numberafterequal = float(input("Please Enter a number after equal "))
    import results
    if sofnumber.operation == "+" :
        results.result1 = sofnumber.numberafterequal - sofnumber.numberafteropeartion
        results.result2 = results.result1 / sofnumber.numberofs
        results.result = results.result2
        print(results.result)
    elif sofnumber.operation == "-" :
        results.result1 = sofnumber.numberafterequal + sofnumber.numberafteropeartion
        results.result2 = results.result1 / sofnumber.numberofs
        results.result = results.result2
        print(results.result)
    elif sofnumber.operation == "*" :
        results.result1 = sofnumber.numberafterequal / sofnumber.numberafteropeartion
        results.result2 = results.result1 / sofnumber.numberofs
        results.result = results.result2
        print(results.result)
    elif sofnumber.operation == "/" :
        results.result1 = sofnumber.numberafterequal * sofnumber.numberafteropeartion
        results.result2 = results.result1 / sofnumber.numberofs
        results.result = results.result2
        print(results.result)
    else :
        print("I'am sorry it's not supported now please retry")