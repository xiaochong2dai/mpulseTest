# Problem 1:

## (1) basic version: parsingContent.py

run the below command:
```
python parsingContent.py FIRST_NAME ORDERS TEMPLATE
```
Here since each client may have multiple orders, the commands takes more than one orders, just treat each of them as a argument, for example, we can run the command like this:
```
python parsingContent.py "Andrew" "Nutrition" "Health" "Food" "Hello FIRST_NAME, this is your current medication order: ORDERS. If you would like to confirm this order, text \'order\', otherwise text \'help\' for help"
```

## (2) bonus with counter: parsingContentCounter.py

For this part, I'm not sure if the counter should be counted as part of the 160 characters. My code does not count the counters.

Similar way of running command, but add "True/true/False/false" as an extra arguments. For example:

a. This command will add a counter at the beginning of each message:
```
python parsingContentCounter.py "Andrew" "Nutrition" "Health" "Food" "Hello FIRST_NAME, this is your current medication order: ORDERS. If you would like to confirm this order, text \'order\', otherwise text \'help\' for help" True
```

b. This	command	 will not add a counter at the beginning of each message:
```
python parsingContentCounter.py "Andrew" "Nutrition" "Health" "Food" "Hello FIRST_NAME, this is your current medication order: ORDERS. If you would like to confirm this order, text \'order\', otherwise text \'help\' for help" false
```

## (3) double bonus part: 

For this part, I was thinking since there are extra empty spaces after each ORDER_ITEM. I don't know the number of these spaces, so I need more clarifications for this part, so that I know how to handle it. These empty spaces after the ORDER_ITEM will affect the 160 character limit.


Note: for command-line arguments, we can also use argparse module.




# Problem 2:

The program can be run with the command as follows:
```
python triangle.py
```
User can type in the length of the equilateral triangle. It handles negative(invalid) inputs.

I added a notes how I figured out this problem as a seperate file "triangle example"




# Problem 3:

For this part, the HTTP method we use is "GET" since we are requesting resources. Also, we can use Flask to build web services. The way it works is we search in the data array (each element is dictionary), and if the mobile number is not in the array, then return status code 404, which means "Resource Not Found". If it is in, then we use jsonify module to convert the dict to json, and send it to teh client side.

First, open a terminal window and start the local server:
```
python app.py
```
Then open another terminal window, and use curl to get the mobile number and name:
```
curl -i http://localhost:5000/api/1310404889
```
