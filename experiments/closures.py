def outer():
    x = 'foo'
    print("x is {} in outer before assignment".format(x))

    def inner_local():
        x = 'bar' 
        print("x is {} in inner_local after assignment".format(x))

    inner_local()
    print("x is {} in outer after calling inner_local()".format(x))

    def inner_nonlocal():
        nonlocal x
        x = 'bar' 
        print("x is {} in inner_nonlocal after assignment".format(x))

    inner_nonlocal()
    print("x is {} in outer after calling inner_nonlocal()".format(x))

outer()


