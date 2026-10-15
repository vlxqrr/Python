def Duplicates():
    listValue = [4, 2, 4, 1, 2, 7]
    resultList = list(dict.fromkeys(listValue))
    print(resultList)

    uniqueList = []

    for newValue in listValue:
        if newValue not in uniqueList:
            uniqueList.append(newValue)
    print(uniqueList)
    
Duplicates()