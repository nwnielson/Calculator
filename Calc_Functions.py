def pemdas(equation) :
    list = []
    number = 0
    last_character = ""
    valid_equation = True
    equation_remaining = True
    
    while valid_equation and equation_remaining:
        
        for i in range(len(equation)):
            
            if str(equation[i]) in "0,1,2,3,4,5,6,7,8,9" :
                list.append(int(equation[i]))
            elif str(equation[i]) in "^,*,/,(,),+,-": 
                list.append(equation[i])
            else :
                valid_equation = False
                list = []
                
        equation_remaining = False
        
    for index, i in enumerate(list) :
        if i == "(" :
            solution = parenthesis(list, index)
    number = 0
    for index, i in enumerate(list) :
        if str(i) in "0,1,2,3,4,5,6,7,8,9" :
            number = numbers(last_character, i, number)
        if i == "^" :
            last_character = i
            print(number)
            solution = exponents(list[index:], i, number, last_character, index)
    number = 0
    for index, i in enumerate(list) :
        if str(i) in "0,1,2,3,4,5,6,7,8,9" :
            number = numbers(last_character, i, number)
        if i == "*" :
            last_character = i
            solution = multiplication(list[index:], number, last_character)
    
    
        
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

def numbers(last_character, i, number) :
    if str(last_character) not in "0,1,2,3,4,5,6,7,8,9" :
        number += i
        last_character = i
    else :
        number *= 10
        number += i
    print(number)
    return number
                
def parenthesis(list, index) :
    number = 0
                
    for index2, j in enumerate(list[index:]) :
        
        if j == ")" :
            new_list = []
            simplified_segment = pemdas(list[index:index2])
            for k in range(len(str(simplified_segment))) :
                new_list.append(str(simplified_segment)[k])
            list = list[:index] + new_list + list[index2:]
            number = 0
    return list

def exponents(list, i, number, last_character, index) :
    exponent_found = False
    exponent = 0
    last_character = i
        
    # Loops to find exponent
    for j in range(len(list)) :
        # Checks if there are parenthesis in the 
        if j == "(" and not exponent_found:
            list = parenthesis(list, index)
        
        # Runs if exponent found and is a number
        if str(list[j]) in "0,1,2,3,4,5,6,7,8,9" and not exponent_found:
            # If 
            if str(last_character) not in "0,1,2,3,4,5,6,7,8,9" : 
                exponent += list[j]
                last_character = list[j]
            elif str(last_character) in "0,1,2,3,4,5,6,7,8,9" :
                exponent *= 10
                exponent += list[j]
        elif str(list[j]) in "+,-,*,/": 
            exponent_found = True
    
    print(number, exponent)
    
    number = number ** exponent
    
    return number
    
def multiplication(list, number, last_character) :
    number2 = 0
    number2_found = False
    
    for j in range(len(list)) :
        # Runs if exponent found and is a number
        if str(list[j]) in "0,1,2,3,4,5,6,7,8,9" and not number2_found:
            # If 
            if str(last_character) not in "0,1,2,3,4,5,6,7,8,9" : 
                number2 += list[j]
                last_character = list[j]
            elif str(last_character) in "0,1,2,3,4,5,6,7,8,9" :
                number2 *= 10
                number2 += list[j]
        elif str(list[j]) in "+,-,/": 
            number2_found = True
    number = number * number2
    return number

"""def division() :
    
    
def addition() :
    
    
def subtraction() :
    
    
def """