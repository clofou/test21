# operation entre deux nombres

number1 = int(input("Number1 = "))
number2 = int(input("Number2 = "))
op = input("Choississez une opération:\n\t +, *, /, - :")

if op == '+' :
    print ("somme {}{}{} = {}".format(number1, op, number2, number1+number2))
elif op == '*' :
    print ("multiplication {}{}{} = {}".format(number1, op, number2, number1*number2))
elif op == '/' :
    if number2 == 0:
        print("Division impossible!")
    else:
        print ("division {}{}{} = {}".format(number1, op, number2, number1/number2))
else :
    print ("soustraction {}{}{} = {}".format(number1, op, number2, number1-number2))