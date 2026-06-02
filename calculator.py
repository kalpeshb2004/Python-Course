num1 = int(input("Enter a first number: "))
num2 = int(input("enter a second number: "))

choice = input("enter a choice that you want to perform (+ - * / % ** //):- ")

match choice:
    case "+":
        print("addition is :" ,num1 + num2)
    case "-":
        print("sustraction is :" ,num1 - num2)    
    case "*":
        print("multiplication is :" ,num1 * num2)
    case "/":
        print("devision is :" ,num1 / num2)        
    case "%":
        print("reminder is :" ,num1 % num2)    
    case "**":
        print("square is :" ,num1 ** num2)  
    case "//":
        print("floar devision is :" ,num1 // num2)      
    case _:
        print("invalid case")    