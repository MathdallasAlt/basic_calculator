while True:
    #Setting variables
    optype=input("Enter type of operation(+ for add,-for sub,*for mul,d/for decimal divison and l/ for long division):")
    numI=int(input("Enter first number:"))
    numII=int(input("Enter second number:"))
    #Conditional operations
    if optype=="+":
        print(str(numI),"+",str(numII),"is",numI+numII)

    if optype=="-":
        print(str(numI),"-",str(numII),"is",numI-numII)

    if optype=="*":
        print(str(numI),"*",str(numII),"is",numI*numII)

    if optype=="/":
        print(str(numI),"/",str(numII),"is",numI/numII)
