
#reply = input("Do you want to foil or unfoil the equation?")
unfoil_equation = "x^2 + 2x + 3"
foil_equation = '(x+9)(x-1)'

def foil(equation):
    # replacing x values with one to do arithmatic
    if equation[1] == 'x':
        equation = equation.replace('x','1')
    if equation[6] == 'x':
        equation.replace('x','1')
    if equation[7] == 'x':
        equation.replace('x','1')
    
    #doing the multiplication of the FOIL and adding the two like values
    first = int(equation[1]) * int(equation[6])
    inner = int(equation[3]) * int(equation[6])
    outer = int(equation[1]) * int(equation[8])
    last = int(equation[3]) * int(equation[8])
    inner_outer = inner + outer

    # need way to determine the sign of the string printout
    if equation.find('-') == -1 or equation.find('+') == -1:
        outer_sign = '+'
    else:
        outer_sign = '-'  
        #if there is a negative sign is it in first or second set 
        if equation.find('-') < 4:
            inner_outer = (outer - inner)
        else:
            inner_outer = (inner - outer)

    #getting the last part of the sign for the string print
    if inner_outer > 0:
        sign = '+'
    else:
        sign = '-'
    if first == 1: # dont want to print a 1 just print x
        first = ''

    # actual print statement once math is done
    print(f"{first}x\N{SUPERSCRIPT TWO} {sign} {abs(inner_outer)}x {outer_sign} {last}")

def unfoil(equation):
    square = ""
    xnumber = ""
    number = ""

def setEquation():
    global equation
    equation = input("Please enter the equation: ")

foil(foil_equation)

"""
if reply == "foil":
    setEquation()
    foil(equation)

if reply == "unfoil":
    setEquation()
    unfoil(equation)
"""
    


