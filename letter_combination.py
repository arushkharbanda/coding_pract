
def letterCombinations(digits: str):


    '''
    digitMap={}
    start=ord('a')
    for k in range (2,10):
        if k ==7 or k==9:
            digitMap[str(k)]=[chr(start), chr(start+1) ,chr(start+2),chr(start+3)]
            start=start+4
        else:
            digitMap[str(k)]=[chr(start), chr(start+1) ,chr(start+2)]
            start=start+3
    print(digitMap)
    '''
    digitMap={'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

    possibleStack=[]
    for i in range(0,len(digits)):
        possibleStack.append(digitMap[digits[i]])
    #print(possibleStack)

    posbArr=[]
    for i in range(len(possibleStack)):
        a=possibleStack.pop()
        if (len(posbArr)==0):
            posbArr=a
        else:
            tempArr=[]
            for i in range(len(a)):
                for j in range(len(posbArr)):
                    tempArr.append(a[i]+''+posbArr[j])
            posbArr=tempArr
    return posbArr







#letterCombinations("23")
assert(letterCombinations("23")==["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
assert(letterCombinations("2")==["a", "b","c"])
#assert(letterCombinations("789")==["a", "b","c"])
