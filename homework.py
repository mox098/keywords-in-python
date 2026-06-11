def func():

    a=int(input("enter your bill amount"))
    b=int(input("enter amount you've payed"))
    if b>a:
        c=b-a
        print(c)
        return print("done!!!")
func()