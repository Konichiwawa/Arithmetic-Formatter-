def arithmetic_arranger(problems, solve = False):
    
    # check for the limit of 5 problems 
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_row = ""
    second_row = ""
    third_row = ""
    fourth_row = ""
  
    # create a loop to split and work on each problem 
    for index, value in enumerate(problems):
        problem = value.split()
        
        # check for the appropriate operators
        if problem[1] not in '+-':
            return "Error: Operator must be '+' or '-'."
        
        # check for max width of 4 digits 
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # check for only digits 
        try:
            operand_1 = int(problem[0])
            operand_2 = int(problem[2])
        except ValueError:
            return "Error: Numbers must only contain digits."
        
        # calculate the width used to align the numbers and to calcute the number of dashes 
        width = max(len(problem[0]), len(problem[2])) + 2
        dashes = '-'*width
        
        # calculate the answer
        if problem[1] == "+":
            answer = str(operand_1 + operand_2)
        else:
            answer = str(operand_1 - operand_2) 
       
        if index != (len(problems)-1):
            # formatted output of each problem 
            first_row += f"{problem[0]:>{width}}" + "    "
            second_row += f"{problem[1]}{problem[2]:>{width-1}}" + "    "
            third_row += f"{dashes:>{width}}" + "    "
            fourth_row += f"{answer:>{width}}" + "    "  
        else:
            first_row += f"{problem[0]:>{width}}" 
            second_row += f"{problem[1]}{problem[2]:>{width-1}}"
            third_row += f"{dashes:>{width}}" 
            fourth_row += f"{answer:>{width}}"
        
    display_all = f"{first_row}\n{second_row}\n{third_row}\n{fourth_row}"
    display_some = f"{first_row}\n{second_row}\n{third_row}"
    
    if solve == True:
        return display_all
    else:
        return display_some

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))
