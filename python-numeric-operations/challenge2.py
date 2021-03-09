print("Simple calculator!")

first_number = input("First number? ")

while not(first_number.isnumeric()):
    print("Please, input a number")
    first_number = input("First number? ")

op = input("Operation? ")

if op != '+' and op != '-' and op != '*' and op != '/' and op != '**' and op != '%':
    print("Operation not recognized")
    exit()

second_number = input("Second number? ")

while not(second_number.isnumeric()):
    print("Please, input a number")
    second_number = input("Second number? ")

first_number = int(first_number)
second_number = int(second_number)

if op == '+':
    res = first_number + second_number
    opAux = "Sum of "
elif op == '-':
    res = first_number - second_number
    opAux = "Substraction of "
elif op == '*':
    res = first_number * second_number
    opAux = "Multiplication of "
elif op == '/':
    res = first_number / second_number
    opAux = "Quotient (division) of "
elif op == '**':
    res = first_number ** second_number
    opAux = "Exponent of "
else: # only left the module
    res = first_number % second_number
    opAux = "Modulus of "

first_number = str(first_number)
second_number = str(second_number)
res = str(res)

print(opAux + first_number + ' ' + op + ' ' + second_number + " = " + res)