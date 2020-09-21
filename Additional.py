try:
    with open('text1.txt', mode='r') as f:
        fr=f.read()
    print(fr)
except FileNotFoundError:
   print('Файл не найден')
except PermissionError:
    print('Эта операция вам запрещена')
except Exception as err:
    print('Что-то пошло не так',str(err))
    
