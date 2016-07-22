import sys
# split the string: check if the 160th char is space, if so, then split the string by the space, 
# if not, then use 'rindex' to search the index from 160th backwards, and find the index. Append
# each part to the ree list.
def stringSpliter(str):
	res = []
	while(len(str) > 160):
		part = str[:160]
		if str[159].isspace():
			res.append(part)
			str = str[160:]
		else:
			index = part.rindex(' ')
			res.append(str[:index+1])
			str = str[index+1:]

	res.append(str)
	return res


def parsingContent(**tokens):
    clientName = tokens['FIRST_NAME']
    ordersRes = tokens['ORDERS']
    clientOrders = ', '.join(ordersRes)
    messageTemp = tokens['TEMPLATE']
    res = messageTemp.replace("FIRST_NAME", clientName).replace("ORDERS", clientOrders)
    context = stringSpliter(res)
    print '\n'
    for part in context:
    	print part, '\n'


if __name__=="__main__":
    # defaultTemplate = "Hello FIRST_NAME, this is your current medication order: ORDERS. If you would like to confirm this order, text \'order\', otherwise text \'help\' for help"
    cilentName = sys.argv[1]
    orderList = sys.argv[2:-1]
    template = sys.argv[-1] 
    # tokens = {"FIRST_NAME": cilentName, "ORDERS": ["Nutrition", "Health", "Food"]}
    tokens = {"FIRST_NAME": cilentName, "ORDERS": orderList, "TEMPLATE": template}
    parsingContent(**tokens)
