def pemdas(equation) :
    list = []
    number = 0
    number2 = 0
    last_character = ""
    valid_equation = True
    equation_remaining = True
    place_value = 1
    solution = 0
    solution_list = []
    
    while valid_equation and equation_remaining:
            
        # Put the equation in a list
        for i in range(len(equation)):
            # 10*5
            if str(equation[i]) in "0,1,2,3,4,5,6,7,8,9" :
                number *= place_value
                number += int(equation[i])
                last_character = equation[i]
                place_value *= 10
                
            elif str(equation[i]) in "^,*,/,(,),+,-": 
                list.append(number)
                list.append(equation[i])
                number = 0
                place_value = 1
            else :
                valid_equation = False
                list = []
            last_character = equation[i]
        list.append(number)
                
        equation_remaining = False
    
    # Parenthesis
    for index, i in enumerate(list) :
        
        if i == "(" :
            number, index2 = parenthesis(list, index)
            list = list[:index - 1] + [number] + list[index + index2 + 2:]
            
    # Exponents
    for index, i in enumerate(list) :
        
        if i == "^" :
            number, number2 = numbers(list, index)
            solution = exponents(list[index:], i, number, number2, index)
            list = list[:index - 1] + [solution] + list[index + 2:]
            continue
    
    # Multiplication and Division
    for index, i in enumerate(list) :
        
        if i == "*" :
            number, number2 = numbers(list, index)
            solution = multiplication(number, number2)
            list = list[:index - 1] + [solution] + list[index + 2:]
            continue
        
        elif i == "/" :
            number, number2 = numbers(list, index)
            solution = division(number, number2)
            list = list[:index - 1] + [solution] + list[index + 2:]
            continue
    
    # Addition and Subtraction
    for index, i in enumerate(list) :
        
            if i == "+" :
                number, number2 = numbers(list, index)
                solution = addition(number, number2)
                list = list[:index - 1] + [solution] + list[index + 2:]
                continue
            
            elif i == "-" :
                number, number2 = numbers(list, index)
                solution = subtraction(number, number2)
                list = list[:index - 1] + [solution] + list[index + 2:]
                continue
        
    """try :
        if str(i) in "0,1,2,3,4,5,6,7,8,9" :
            number = numbers(last_character, i, number)
        
    except :
        if i == "^" :
            last_character = i
            print(number)
            solution = exponents(list[index:], i, number, last_character, index)
    else :"""
        
        
    """for index, i in enumerate(list) :
        
        if str(i) in "0,1,2,3,4,5,6,7,8,9" :
            number = numbers(last_character, i, number)
        
        elif i == "(" :
            solution = parenthesis(list, index)
                    
        elif i == "^" :
            last_character = i
            solution = exponents(list[index:], i, number, last_character, index)
        
        elif i == "*" :
            solution = multiplication(list[index:], i, number, last_character)"""
        
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

def exponents(list, i, number, number2, index) :
    """exponent = 0
        
    # Loops to find exponent
    
    if list[1] == "(":
        list = parenthesis(list, index)
        
    # Runs if exponent found and is a number
    if isinstance(list, int):
        exponent += list[i + 1]
    
    print(number, exponent)"""
    
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