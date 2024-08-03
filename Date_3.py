
def My_Func_Date() :
    try:
        userInDate = int(input('Введіть число місяця: \t'))
        userInMonth = int(input('Введіть місяць: \t'))
        userInYear = int(input('Введіть рік: \t'))
        if userInDate == str(userInDate) :
            raise TypeError('Некорректно введена дата. \n')
        if userInMonth == str(userInMonth):
            raise TypeError('Некорректно введений місяць. \n')
        if userInYear == str(userInYear):
            raise TypeError('Некорректно введений рік. \n')
        if userInDate <= 0 or userInDate > 31 :
            raise ValueError('Некорректно введена дата. \n')
        if userInMonth < 1 or userInMonth > 12 :
            raise ValueError('Некорректно введений місяць. \n')
        if userInYear < 0 :
            raise ValueError('Некорректно введений рік. \n')
        else:
            print(f'{userInDate}.{userInMonth}.{userInYear}')
    except ValueError as e :
        print(e)
    except TypeError as e :
        print(e)

My_Func_Date()