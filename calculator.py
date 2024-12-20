keepGoing = True;

calcType = input("Would you like to run the Scientific (enter s) or Programmer (enter p) calculator? ");

while(keepGoing): 

    if(len(calcType) == 1 and ord(calcType) == 'p'):    
        #run programmer calculator  
        converter = input("Enter 'd' to convert a decimal to binary, or 'b' to convert binary to decimal: ");
        if(len(converter) == 1 and (converter) == 'd'):
            num = input("Enter a positive Decimal number to convert to Binary: ");
            acceptable = True;
            result = "";
        
        # makes sure the value entered is a good decimal value
            for x in range(0,len(num)):
                if((num[x]) < '0' or (num[x]) > '9'):
                    acceptable = False;
                    break;
        
        # converts the string input to an integer if it is valid
            if(acceptable):
                num = int(num);
                if(num < 0):
                    acceptable = False;
        
        # converts the decimal number to binary
            if(acceptable):
                if(num == 0):
                    result = "0";

                while(num > 0):
                    result = str(num % 2) + result;
                    num = num // 2;

                print("Binary conversion is: " + str(result));
            else:
                print("This is not a positive whole number!");
        elif(len(converter) == 1 and (converter) == 'b'):
            num = input("Enter an unsigned binary number to convert to decimal: ");
            acceptable = True;
            result = 0;

        # makes sure the value entered is a good binary value
            for x in range(0,len(num)):
                if((num[x]) < '0' or (num[x]) > '1'):
                    acceptable = False;
                    break;
            
        # converts the binary value to a decimal number
            if(acceptable):
                for x in range(0, len(num)):
                    position = len(num) - x - 1;
                    if((num[x]) == '1'):
                        result = result + (2 ** position);

                print("Decimal conversion is: " + str(result));

            else:
                print("This is not an unsigned binary number!");
        else:
            print("Value not recognized, please enter a 'd' or 'b' while in the programmer calculator");

    elif(len(calcType) == 1 and (calcType) == 's'):
        #run scientific
        operator = input("What kind of operation would you like to run? (+,-,*,/,**) ");
        operand1 = input("What is the first operand? ");
        operand2 = input("What is the second operand? ");
        
        acceptable = True;
        opOneDec = False;
        opTwoDec = False;
        opOneNeg = False;
        opTwoNeg = False;

        # both operands have to be values
        if(len(operand1) == 0 or len(operand2) == 0):
            acceptable = False;

        # determines if either operand is negative
        if((operand1[0]) == '-'):
            opOneNeg = True;

        if((operand2[0]) == '-'):
            opTwoNeg = True;        

        # makes sure the first operand is a valid number
        for x in range(int(opOneNeg),len(operand1)):
            if((operand1[x]) == '.' and not opOneDec):
                opOneDec = True;
            elif((operand1[x]) == '.' and opOneDec):
                acceptable = False;
                print("The first operand is not a number");
                break;
            elif((operand1[x]) < '0' or (operand1[x]) > '9'):
                acceptable = False;
                print("The first operand is not a number");
                break;

        # makes sure the second operand is a valid number
        for x in range(int(opTwoNeg),len(operand2)):
            if((operand2[x]) == '.' and not opTwoDec):
                opTwoDec = True;
            elif((operand2[x]) == '.' and opTwoDec):
                acceptable = False;
                print("The second operand is not a number");
                break;
            elif((operand2[x]) < '0' or (operand2[x]) > '9'):
                acceptable = False;
                print("The second operand is not a number");
                break;
       
        # converts both string inputs to floats or integers 
        if(acceptable):
            if(not opOneDec):
                operand1 = int(operand1);
            else:
                operand1 = float(operand1);
            if(not opTwoDec):
                operand2 = int(operand2);
            else:
                operand2 = float(operand2);
    
        result = 0; 

        # performs operation based on operator
        if(len(operator) == 1 and (operator) == '+' and acceptable):
            result = operand1 + operand2;

        elif(len(operator) == 1 and (operator) == '-' and acceptable):
            result = operand1 - operand2;

        elif(len(operator) == 1 and (operator) == '*' and acceptable):
            result = operand1 * operand2;

        elif(len(operator) == 1 and (operator) == '/' and acceptable):
            result = operand1 / operand2;

        elif(len(operator) == 2 and (operator[0]) == '*' and (operator[1]) == '*'):
            if(acceptable):
                result = operand1 ** operand2;
        elif(acceptable):
            print("The operator is not recognized");
            acceptable = False;         

        if(acceptable):
            print(str(operand1) + " " + str(operator) + " " + str(operand2) + " = " + str(result));

    else:
        print("The value you input is not recognized, please input either 's' or 'p.'");

    calcType = input("Enter an 'x' to escape, 's' for the scientific calculator, or 'p' for the programmer calculator: ")
    if(len(calcType) == 1 and (calcType) == 'x'):
        keepGoing = False;
  