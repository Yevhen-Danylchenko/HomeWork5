def My_Func_String (my_list) :
    for index in my_list :
        try:
            if index == str(index) :
                raise TypeError('В списку строчний елемент.')
        except TypeError as e :
            print(e)
    print(my_list)

my_list = [1,2,6,-1,0,'er',2,4,]


My_Func_String (my_list)