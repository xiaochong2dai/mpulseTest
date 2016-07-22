import sys
# split the string: check if the 160th char is space, if so, then split the string by the space, 
# if not, then use 'rindex' to search the index from 160th backwards, and find the index. Append
# each part to the ree list.
def stringSpliter(strIn, counter):
    res = []
    while(len(strIn) > 160):
        part = strIn[:160]
        if strIn[159].isspace():
            res.append(part)
            strIn = strIn[160:]
        else:
            index = part.rindex(' ')
            res.append(strIn[:index+1])
            strIn = strIn[index+1:]
    res.append(strIn)

    if counter == True:
        i = 0
        while i < len(res):
            smsNum = '(' + str(i+1) + '/' + str(len(res)) + ')'
            res[i] = smsNum + ' ' + res[i]
            i = i + 1
    return res


def parsingContent(**tokens):
    clientName = tokens['FIRST_NAME']
    ordersRes = tokens['ORDERS']
    clientOrders = ', '.join(ordersRes)
    messageTemp = tokens['TEMPLATE']
    counter = tokens['COUNTER']
    res = messageTemp.replace("FIRST_NAME", clientName).replace("ORDERS", clientOrders)
    context = stringSpliter(res, counter)
    print '\n'
    for part in context:
    	print part, '\n'


if __name__=="__main__":
    cilentName = sys.argv[1]
    orderList = sys.argv[2:-2]
    template = sys.argv[-2] 
    counterStr = sys.argv[-1]
    counter = True if counterStr in ["True", "true"] else False
    tokens = {"FIRST_NAME": cilentName, "ORDERS": orderList, "TEMPLATE": template, "COUNTER": counter}
    parsingContent(**tokens)
