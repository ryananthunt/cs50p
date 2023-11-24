greeting = input('Greeting: ').lower() # prompt user for greeting, make lowercase for ease

greeting = greeting.strip() # remove any unnecessary whitespace


# check if greeting meets criteria
if greeting.startswith('hello'):
    print('$0')
elif greeting.startswith('h'):
    print('$20')
else:
    print('$100')
