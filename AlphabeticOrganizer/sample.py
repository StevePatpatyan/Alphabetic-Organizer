from Constants import*
def split(word):
    return [char for char in word]
mode = input("What would you like to use?\n\nAlphabetizer\nCalculator\nPhysics\n")
if (mode.capitalize()=="Alphabetizer"):
    order = [None,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    entered = input("Enter a list of words. Separate each word with a space. Press enter when you are done.\n\n")
    final = []
    letterNum=0
    counter = 1
    words = entered.split(' ')
    for word in words:
        if (len(word)>letterNum):
            letterNum = len(word)
    while (letterNum>=0):
        final = []
        for orders in order:
            for word in words:
                if (len(word)-1<letterNum and orders==None):
                    final.append(word)
                if (len(word)-1>=letterNum):
                    if (split(word)[letterNum].capitalize()==orders):
                        final.append(word)
        words = final
        letterNum = letterNum-counter
    print('\n'.join(final))

elif(mode.capitalize()=="Calculator"):
    order = ["*/%","+-e"]
    final = []
    ops = []
    ans = 0
    while (True):
        entered = input("Enter an equation. Put a space between each number/operation. To refer to the previous solution, type 'ans'.\n\n")
        number = entered.split(' ')
        if (number[0]=="ans"):
            number[0]=ans
        if (number[2]=="ans"):
            number[2]=ans
        number[0]=float(number[0])
        number[2]=float(number[2])
        if (number[1]=='+'):
            ans = number[0]+number[2]
        elif (number[1]=='-'):
            ans = number[0]-number[2]
        elif (number[1]=='*'):
            ans = number[0]*number[2]
        elif (number[1]=='/'):
            ans = number[0]/number[2]
        elif (number[1]=='%'):
            ans = number[0]%number[2]
        print(ans)

elif (mode.capitalize()=="Physics"):
    while (True):
        entered = input("What would you like to solve for?\n\nForce\nDistance\nSpeed\nAcceleration\n\n")
        if (entered.capitalize()=="Force"):
            entered = input("Select an equation via its respective number:\n\n1. F = ma\n\nFg = Gmm/r^2\n\n3. Torque = F*d\n\n4. Torque = I*alpha\n\n")
        if (entered=="1"):
            print("Give each quantity a value. Put an 'x' for the quantity to be solved.")
            force = input("Force (kg*m/s^2): ")
            mass = input("Mass (kg): ")
            acceleration = input("Acceleration (m/s^2): ")
            if (force.capitalize()=="X"):
                ans = float(mass)*float(acceleration)
                print(ans)
            elif (mass.capitalize()=="X"):
                ans = float(force)/float(acceleration)
                print(ans)
            elif (acceleration.capitalize()=="X"):
                ans = float(force)/float(mass)
                print(ans)
            else:
                raise Exception("No value to be solved for")
        if (entered=="2"):
            print("Give each quantity a value. Put an 'x' for the quantity to be solved.")
            force = input("Force of Gravitation (kg*m/s^2): ")
            mass1 = input("Mass 1 (kg): ")
            mass2 = input("Mass 2 (kg): ")
            radius = input("Radius of Orbit (m): ")
            if (force.capitalize()=="X"):
                ans = (const("G")*float(mass)*float(mass))/(float(radius)*float(radius))
                print(ans)
            elif (mass1.capitalize()=="X"):
                ans = (float(force)*float(radius)*float(radius))/(const("G")*float(mass2))
                print(ans)
            elif (mass2.capitalize()=="X"):
                ans = (float(force)*float(radius)*float(radius))/(const("G")*float(mass1))
                print(ans)
                #elif (radius.capitalize()=="X"):
                    #ans = float(
           # else:
               # raise Exception("No value to be solved for")
print("\n\n")
                    

        
    
    
