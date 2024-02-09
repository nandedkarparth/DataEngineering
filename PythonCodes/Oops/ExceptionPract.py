def max(a,b):
    try:
        c = ((a + b)/(a - b))

    except ZeroDivisionError:
        print("a/b result not possible")

    else:
        print(c)

    finally:
        print("Always Works")

max(2,3)
max(3,3)
