def is_armstrong_number(number):
    lengthOfNumber = len(str(number))
    iterator=lengthOfNumber
    result=0
    numberIteration=number
    if lengthOfNumber == 1:
        return True
    while iterator !=0:
        result = result + (int(numberIteration%10) ** lengthOfNumber)
        numberIteration=int(numberIteration/10)
        iterator=iterator-1
    if result==number:
        return True
    return False
