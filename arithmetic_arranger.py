def arithmetic_arranger(problems, calculate=None):

    if len(problems) > 5:
      return "Error: Too many problems."

    operator_list = []
    operands_list = []
    longest_list = []
    
    # for each problem, take out the operator and operands, check them against defined cosntraints
    for problem in problems:
      operator = problem.split(' ')[1]
      operands = [problem.split(' ')[index].strip() for index in [0,2]]
      if operator not in ['+', '-']:
        return "Error: Operator must be '+' or '-'."
      for operand in operands:
        if len(operand) > 4:
          return "Error: Numbers cannot be more than four digits."
        elif not operand.isdigit():
          return "Error: Numbers must only contain digits."
      operator_list.append(operator)
      operands_list.append(operands)

    # identify the longest operand for each problem, in order to use it later, for requirement "There should be a single space between the operator and the longest of the two operands"
    for pair in operands_list:
      op1 = len(pair[0])
      op2 = len(pair[1])
      longest = op1
      if op2 > op1:
        longest = op2
      longest_list.append(longest)
    
    top = ''; bottom = ''; dashes = ''; results = ''
    # construct string with top and bottom lines
    for idx in range(len(problems)):
        top += f'{operands_list[idx][0].rjust(longest_list[idx] + 2)}    '
        bottom += f'{operator_list[idx]} {operands_list[idx][1].rjust(longest_list[idx])}    '
        dashes += '-'*(longest_list[idx] + 2) + ' '*4
        # cosntruct string with the result line
        result = ''
        if operator_list[idx] == '-':
            result = int(operands_list[idx][0]) - int(operands_list[idx][1])
        else:
            result = int(operands_list[idx][0]) + int(operands_list[idx][1])
        results += f'{str(result).rjust(longest_list[idx] + 2)}    '

    # cosntruct the string with arranged problems, if the "calculate" parameter is given or not
    if calculate:
        arranged_problems = top.rstrip() + '\n' + bottom.rstrip() + '\n' + dashes.rstrip() + '\n' + results.rstrip()
    else:
        arranged_problems = top.rstrip() + '\n' + bottom.rstrip() + '\n' + dashes.rstrip()

    return arranged_problems

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))