files =['Еля','Яся']
def start(files,element):
    a = int(input('Найти - 1,Добавить - 2: '))

    if a == 1:
        ok = 0
        poisk = input('Веди имя: ')
        print('                ')
        for i in range(len(files)):
            if poisk == files[i]:
                print('Найдено')
                ok = 1
        if ok == 0:        
            print('Не найдено')
        print('                ')
        start(files,2)

    if a == 2:
        check = input('Веди имя: ')
        print('                ')
        files.append(check)
        start(files,2)
    if a == 2222:
        print(files)
        print('                ')
        start(files,2)
start(files,2)
