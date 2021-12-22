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
    lineList = ["-----"]*len(mainInputList)
    # store answer of each operator
    ansList = []


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
        if len(firstValue) > 4 or len(secondValue) > 4:
            print("Error: Numbers cannot be more than four digits.")
            quit()
        if operator == "*" or operator == "/":
            print("Error: Operator must be '+' or '-'.")
            quit()


    # calculate arithmetic oparetion of two number:
    def calculate(firstValue, secondValue, operator):
        try:
            result = ops[operator](int(firstValue) , int(secondValue))
            return result
        except ValueError:
            print("Error: Numbers must only contain digits")
            quit()
        


    # append calculate answer in "ansList" list:
    def ansListValue(i):
        result = calculate(firstRow[i], secondRow[i], operatorList[i])
        ansList.append(result)



    # final output format :
    def formatStyle():
        contacinateOps_Sec_List = [a+" "+b for a, b in zip(operatorList, secondRow)]
        for line in [firstRow, contacinateOps_Sec_List, lineList, ansList]:
            if len(mainInputList) == 1:
                print("{:>8}".format(*line))
            if len(mainInputList) == 2:
                print("{:>8} {:>8}".format(*line))
            if len(mainInputList) == 3:
                print("{:>8} {:>8} {:>8}".format(*line))
            if len(mainInputList) == 4:
                print("{:>8} {:>8} {:>8} {:>8}".format(*line))
            if len(mainInputList) == 5:
                print("{:>8} {:>8} {:>8} {:>8} {:>8}".format(*line))


    # final output format without true :
    def formatStyleWithoutTrue():
        contacinateOps_Sec_List = [a+" "+b for a, b in zip(operatorList, secondRow)]
        for line in [firstRow, contacinateOps_Sec_List, lineList]:
            if len(mainInputList) == 1:
                print("{:>8}".format(*line))
            if len(mainInputList) == 2:
                print("{:>8} {:>8}".format(*line))
            if len(mainInputList) == 3:
                print("{:>8} {:>8} {:>8}".format(*line))
            if len(mainInputList) == 4:
                print("{:>8} {:>8} {:>8} {:>8}".format(*line))
            if len(mainInputList) == 5:
                print("{:>8} {:>8} {:>8} {:>8} {:>8}".format(*line))


    # main function
    def output(mainInputList, answer):
        if len(mainInputList) > 5:
            print("Error: Too many problems.")
            quit()
        for i in range(len(mainInputList)):
            dividedValue(mainInputList[i])
            ansListValue(i)
        if answer:
            formatStyle()
        else :
            formatStyleWithoutTrue()
            

    # Main output function for showing IndexError 
    def mainOutput(mainInputList, answer):
        try:    
            output(mainInputList, answer)
        except IndexError:
            print("Error: Plese input list with proper format !!!")


    mainOutput(mainInputList, answer)
    if len(mainInputList) == 0:
        print("Plese input value !!!")


# arithmetic_arranger(["4 + 4", "5 + 6", "5 + 6", "5 + 6", "5 + 6"], True)

