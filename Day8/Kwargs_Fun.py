def stud_info(**kwargs):

    '''
    for key in kwargs:
        print(key)

    for value in kwargs.items():
        print(value)
    '''
        
    for key, value in kwargs.items():
        print(key ,":", value)

stud_info(name = "Vishnu", age =  24, city = "Malappuram", course = "Python")