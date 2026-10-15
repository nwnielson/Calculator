def pemdas(equation) :
    list = []
    number = 0
    number2 = 0
    place_value = 1
    solution = 0
    
    # Put the equation in a list
    for i in range(len(equation)):
        
        # If it's the first number add number to 1's place and increase place_value, 
        # Following numbers will be added to 1s place while earlier numbers are multiplied by 10
        if str(equation[i]) in "0,1,2,3,4,5,6,7,8,9" :
            
            # If it's on the left side of the decimal
            if place_value >= 1 :
                number *= place_value
                number += int(equation[i])
                place_value *= 10
            # If it's on the right side of the decimal
            else :
                number += int(equation[i]) * place_value
                place_value *= 0.1
        
        # If it's an operator, append the number, followed by the operator
        elif str(equation[i]) in "^,*,/,(,),+,-": 
            list.append(number)
            list.append(equation[i])
            number = 0
            place_value = 1
        
        # If it's a decimal, change place value to 0.1
        elif str(equation[i]) == "." :
            place_value = 0.1
        
        # If not a number or math symbol, raise exception and end loop.
        else :
            raise Exception
    list.append(number)
    
    # Parenthesis
    for index, i in enumerate(list) :
        
        if i == "(" :
            number, index2 = parenthesis(list, index)
            list = list[:index - 1] + [number] + list[index + index2 - 1:]
            
    # Exponents
    while "^" in list:
        index = list.index("^")
        number, number2 = numbers(list, index)
        solution = exponents(number, number2)
        list = list[:index - 1] + [solution] + list[index + 2:]

    # Multiplication and division
    while "*" in list or "/" in list :
        for index, i in enumerate(list) :
            if i == "*" :
                number, number2 = numbers(list, index)
                solution = multiplication(number, number2)
                list = list[:index - 1] + [solution] + list[index + 2:]
                break
            elif i == "/" :
                number, number2 = numbers(list, index)
                solution = division(number, number2)
                list = list[:index - 1] + [solution] + list[index + 2:]
                break
    
    # Addition and subtraction
    while "+" in list or "-" in list :
        
            for index, i in enumerate(list) :
                
                if i == "+" :
                    number, number2 = numbers(list, index)
                    solution = addition(number, number2)
                    list = list[:index - 1] + [solution] + list[index + 2:]
                    break
                if i == "-" :
                    number, number2 = numbers(list, index)
                    solution = subtraction(number, number2)
                    list = list[:index - 1] + [solution] + list[index + 2:]
                    break
        
    return solution


def numbers(list, index) :
    
    number = list[index - 1]
    number2 = list[index + 1]
    
    return number, number2


def parenthesis(list, index) :
                
    for index2, j in enumerate(list[index:]) :
        
        if j == ")" :
            simplified_segment = pemdas(list[index + 1 : index2 + index])
            
    return simplified_segment, index2


def exponents(number, number2) :
    
    number = number ** number2
    
    return number

 
def multiplication(number, number2) :
    
    number = number * number2
    
    return number


def division(number, number2) :
    
    number = number / number2
    
    return number
    
    
def addition(number, number2) :
    
    number = number + number2
    
    return number


def subtraction(number, number2) :
    
    number = number - number2
    
    return number

