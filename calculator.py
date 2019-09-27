import re

print("Our magical calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    if previous == 0:
        equation = input("enter equation:")
    else:
        equation = input(str(previous))

    
    if equation == 'quit':
        print('Goodbye...')
        run = False
    else:
        equation=re.sub('[a-zA-Z,.:()]" "','',equation)
        if previous == 0:
            previous = eval(equation) 
        else:
            previous = eval(str(previous) + equation)
        print(previous)
        #we could use above function print result but it will execute if non arithmatic code is entered


while run:
    performMath()
    
