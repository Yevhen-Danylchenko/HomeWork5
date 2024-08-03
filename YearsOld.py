userInput = 0
def My_Func_Yeas (userInput) :
    try:
        userInput = int(input('Укажіть свій вік: \t'))
        if userInput == str(userInput) :
            raise TypeError('Пишіть цифри будь ласка!')
        if userInput <= 0 :
            raise ValueError('Ваш вік не може бути меньше нуля.\n')
        if userInput > 150 :
            raise ValueError('Ваш вік не може бути більше 150 років. \n')
        else: print(f'Ваш вік: {userInput}')
    except ValueError as e :
        print(e)
    except TypeError as e :
        print(e)

My_Func_Yeas (userInput)
