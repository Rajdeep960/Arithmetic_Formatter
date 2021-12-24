import operator



def arithmetic_arranger(inputList, answer=False):


    ops = { 
        "+": operator.add, 
        "-": operator.sub 
        }


    # some important list :
    # store input list here
    mainInputList = inputList
    # store all first elements in input list
    firstRow = []
    # store all operators in input list
    operatorList = []
    # store all second element in input list
    secondRow = []
    lineList = []
    # store answer of each operator
    ansList = []

    error = []


    # divide input list to firstRow, operatorList, secondRow
    def dividedValue(value):
        stripValue = value.strip()
        valueList = stripValue.split(" ")
        firstValue = valueList[0]
        operator = valueList[1]
        secondValue = valueList[2]
        firstRow.append(firstValue)
        operatorList.append(operator)
        secondRow.append(secondValue)
        max_num = max(len(str(firstValue)), len(str(secondValue)))
        gap = "-"*max_num + "--"
        lineList.append(gap)
        if len(firstValue) > 4 or len(secondValue) > 4:
            error1 = ("Error: Numbers cannot be more than four digits.")
            error.append(error1)
   

    # calculate arithmetic oparetion of two number:
    def calculate(firstValue, secondValue, operator):
        try:
            result = ops[operator](int(firstValue) , int(secondValue))
            return result
        except ValueError:
            error2 = ("Error: Numbers must only contain digits.")
            error.append(error2)
        except KeyError:
            error3 = ("Error: Operator must be '+' or '-'.")
            error.append(error3)

    # append calculate answer in "ansList" list:
    def ansListValue(i):
        result = calculate(firstRow[i], secondRow[i], operatorList[i])
        ansList.append(result)


    # final output format without true :
    def formatStyle(answer):
        out = ""
        contacinateOps_Sec_List = []
        for i in range(len(operatorList)):
            l = operatorList[i] + " "*(len(str(lineList[i])) - len(str(secondRow[i])) - 1) + secondRow[i]
            contacinateOps_Sec_List.append(l)
        firstString = ""
        secString = ""
        lineString = ""
        ansString = ""
        for i in range(len(firstRow)):
            space_between = max(len(str(firstRow[i])), len(str(secondRow[i]))) + 2
            firstString += str(firstRow[i]).rjust(space_between)
            secString += str(contacinateOps_Sec_List[i]).rjust(space_between)
            lineString += str(lineList[i]).rjust(space_between)
            ansString += str(ansList[i]).rjust(space_between)
            if i < len(firstRow) - 1:
                firstString += ' ' * 4
                secString += ' ' * 4
                lineString += ' ' * 4
                ansString += ' ' * 4
        if answer:
            out += firstString + "\n" + secString + "\n" + lineString + "\n" + ansString
            
        else:
            out += firstString + "\n" + secString + "\n" + lineString
        
        return out


    # main function
    def output(mainInputList, answer):
        if len(mainInputList) > 5:
            error4 = ("Error: Too many problems.")
            error.append(error4)
            
        for i in range(len(mainInputList)):
            dividedValue(mainInputList[i])
            ansListValue(i)

        return formatStyle(answer)

            

    # Main output function for showing IndexError 
    def mainOutput(mainInputList, answer):
        try:    
            return output(mainInputList, answer)
        except IndexError:
            error5 = ("Error: Plese input list with proper format !!!")
            error.append(error5)


    arranged_problems = mainOutput(mainInputList, answer)
    if len(mainInputList) == 0:
        error6 = ("Plese input value !!!")
        error.append(error6)

    if len(error) == 0:
        return arranged_problems
    else :
        return error[0]
        


# print(arithmetic_arranger(["4 + 1164", "5 + 6", "5545 + 66", "5 + 6", "5 + 6"],True))

