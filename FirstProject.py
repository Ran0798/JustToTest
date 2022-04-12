while True:
    try:
        income=int(input("Enter your income:"))
        except ValueError:
            print("Error,Pls enter taxable income in number")
            continue
        else:
            break
    if income<=6200:
    tax=0
    elif income<=17000:
        tax=(income-6200)*0.15
    elif income<=40000:
        tax=(income-17000)*0.265 + 2361
     elif income <=120000:
         tax=(income-40000)*0.32 + 18607
     else:
         tax=(income-120000)*0.39+46067
         
         
