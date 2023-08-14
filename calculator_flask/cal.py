def calculator(a,b,op):
    if a.isnumeric() and b.isnumeric():
        a = float(a) 
        b = float(b)
        if op == 'add':
            return(a+b) 
        elif op == 'sub':
            return(a-b) 
        elif op == 'div':
            return(a/b)  
        elif op == 'mul':
            return (a*b) 
        else:
            return(a**b)
calculator('9','7','add')