expression = input('Expression: ') # Get user input

x, y, z = expression.split(' ') # convert into var

# convert into new variables

new_x = float(x)
new_z = float(z)

# get result
if y == '+':
    result = new_x + new_z
if y == '-':
    result = new_x - new_z
if y == '*':
    result = new_x * new_z
if y == '/':
    result = new_x / new_z

print(round(result,1))

