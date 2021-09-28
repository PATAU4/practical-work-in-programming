import os
import shutil
import settings

main_path = settings.main_path
main_path_tmp = settings.main_path_tmp 

def mk_file_v2(n): # создает пустой файл
    open(n,'a').close()
    print(f'Готово!\nФайл {n} был создан')     

def mk_dir(n): # создает директорию
    os.mkdir(n)
    print(f'Готово!\nРепозиторий {n} был создан')     

def remove_file(n): # удаляет файл
    os.remove(n)
    print(f'Готово!\nФайл {n} был удален')

def rm_dir(n): # удаляет директорию если пустая, если в директории есть файлы, то сначала удаляются файлы в ней, а потом она сама
    if os.listdir(n) != []:
        for i in ( os.listdir(n)):
            os.remove( str(n)+'/'+str(i) )
            if os.listdir(n) == []:
                os.listdir(n) == []
                os.rmdir(n)
                print(f'Готово!\nРепозиторий {n} был удален')
    else:
        os.listdir(n) == []
        os.rmdir(n)
        print(f'Готово!\nРепозиторий {n} был удален')

def rename_file(n, ger): # переименовывет файл/директорию
    os.rename(n, ger)
    print(f'Готово!\nНазвание было переименовано с {n} на {ger}')

def mv(n, ger): # перемещает файл/директорию 
    shutil.move(n, ger)
    print(f'Готово!\nФайл {n} был перемещен в {ger}')

def cpf(n, ger): # копирует файл
    shutil.copyfile(n, ger)
    print(f'Готово!\nСодержание файла {n} было копировано в файл {ger}')

def cpdir(fromm, to): # копирует  директорию
    for i in (os.listdir(fromm)):
        tmp = i
        tmp_new_file = i
        tmp = str(fromm)+'/'+str(tmp)
        print(tmp)
        open(tmp_new_file,'a').close()
        shutil.copy(tmp , tmp_new_file)
        shutil.move(tmp_new_file, to)
        print(f'Готово!\nСодержание папки {fromm} было копировано в папку {to}')

def cat(n): # записыввает в файл
    f = open(n, 'w')
    f.write(input())
    f.close()
    print(f'Готово!\nФайл был перезаписан')

def cat(n): # читает содержимое файла
    f = open(n)
    for line in f:
        print(line)

def ls(n): # показывает содержимое директории
    for i in (os.listdir(n)):
        print(i)

def cd(n): # осуществляет перемещение между папками
    global main_path, tmp
    check_file_2 = os.path.exists(n) 
    if check_file_2 is True:
        tmp = main_path
        main_path = n   #новый путь 
        print(f'Вы перешли в директорию {main_path}')

def cd_back(): # переход в прошлую директорию   
    global main_path, main_path_tmp, tmp
    main_path = tmp  # путь возврата назад 
    print(f'Вы перешли в директорию {main_path}')

def cd_main(): # переход в main директорию   
    global main_path, main_path_tmp, tmp
    main_path = main_path_tmp  # путь возврата назад 
    print(f'Вы перешли в директорию {main_path}')
        


print('Добро пожаловать в самый бездарный файловый менеджер. Можете ознакомиться с существующими командами, введя help .\nЧтобы посмотреть справку по команде, напишите: man <команда> .')
while True :

    user_input_comm = str(input('Введите команду...\n'))



    if user_input_comm == 'help': # просто список команд...
        print('Список команд:\nexit, mkdir, remove, rmdir, touch, rename, mv, cpf, cpdir, cat, ls, cd')





        # if, которые определяют команду по первому слову ввода и вызывают соответствующую функцию

    if (user_input_comm.split(' ')[0]) == 'mkdir':
        mk_dir(str(main_path)+'/'+str(user_input_comm.split(' ')[1]))

    if (user_input_comm.split(' ')[0]) == 'touch':
        mk_file_v2(str(main_path)+'/'+str(user_input_comm.split(' ')[1]))

    if (user_input_comm.split(' ')[0]) == 'remove':
        remove_file(str(main_path)+'/'+str(user_input_comm.split(' ')[1]))

    if (user_input_comm.split(' ')[0]) == 'rmdir':
        rm_dir(str(main_path)+'/'+str(user_input_comm.split(' ')[1]))

    if (user_input_comm.split(' ')[0]) == 'rename':
        rename_file((str(main_path)+'/'+str(user_input_comm.split(' ')[1])), (str(main_path)+'/'+str(user_input_comm.split(' ')[2])))

    if (user_input_comm.split(' ')[0]) == 'mv':
        mv((str(main_path)+'/'+str(user_input_comm.split(' ')[1])), (str(main_path)+'/'+str(user_input_comm.split(' ')[2])))

    if(user_input_comm.split(' ')[0]) == 'cpf':
        cpf((str(main_path)+'/'+str(user_input_comm.split(' ')[1])), (str(main_path)+'/'+str(user_input_comm.split(' ')[2])))

    if(user_input_comm.split(' ')[0]) == 'cpdir':
        cpdir((str(main_path)+'/'+str(user_input_comm.split(' ')[1])), (str(main_path)+'/'+str(user_input_comm.split(' ')[2])))

    if(user_input_comm.split(' ')[0]) == 'cat':
        cat(str(main_path)+'/'+str(user_input_comm.split(' ')[1]))

    if(user_input_comm.split(' ')[0]) == 'ls':
        ls(str(main_path)+'/'+str(user_input_comm.split(' ')[1]))

    if (user_input_comm.split(' ')[0]) == 'cd' and (user_input_comm.split(' ')[1]) != 'back' or (user_input_comm.split(' ')[1]) != '~':
        cd(str(main_path)+'/'+str(user_input_comm.split(' ')[1]))

    if (user_input_comm.split(' ')[0]) == 'cd' and (user_input_comm.split(' ')[1]) == 'back':
        cd_back()

    if (user_input_comm.split(' ')[0]) == 'cd' and (user_input_comm.split(' ')[1]) == '~':
        cd_main()



    if user_input_comm == 'man mkdir':
        print('mkdir - создает директории\nсинтаксис: <mkdir "название создаваемого репозитория">')
    if user_input_comm == 'man exit':
        print('exit - останавливает работу файлового менеджера. зачем вы вообще это запускали...')
    if user_input_comm == 'man remove':
        print('remove - удаляет файл\nсинтаксис: <remove "название удаляемого файла">')
    if user_input_comm == 'man rmdir':
        print('rmdir - удаляет директорию\nсинтаксис: <rmdir "название удаляемого репозитория">')
    if user_input_comm == 'man touch':
        print('touch - создает пустой файл\nсинтаксис: <touch "название создаваемого файла">')
    if user_input_comm == 'man rename':
        print('rename - переименовывает название файла\nсинтаксис: <rename "название файла который хотите переименовать, название файла на который хотите переименовать">')
    if user_input_comm == 'man mv':
        print('mv - перемещает файлы\nСинтаксис: <mv "название файла который хотите переместить, название куда хотите переместить файл">')
    if user_input_comm == 'man cpf':
        print('cpf - копирует содержимое одного файла в другой\nсинтаксис: <cpf "название файла откуда копируется данные, название файла куда копируется данные">')
    if user_input_comm == 'man cpdir':
        print('cpdir - копирует файлы из одного репозитория в другой\nсинтаксис: <cpdir "название директории откуда копируются файлы, название репозитория куда копируются файлы">')
    if user_input_comm == 'man cat':
        print('cat - осуществляет запись либо чтение из указанного файла\nсинтаксис:\nзапись -- <cat -> "название файла который хотите открыть на чтение">\nчтение -- <cat "название файла который хотите открыть на чтение">')
    if user_input_comm == 'man ls':
        print('ls - показывает содержимое директории\nсинтаксис: <ls "название директории">')
    if user_input_comm == 'man cd':
        print('cd - позволяет перемещаться между директориями\nсинтаксис:\n<cd "название ПОДдиректории">\n<cd "back"> (осуществляет переход к главной директории)\n<cd ~>(осуществляет переход в main каталог)')



        
     # выход из цикла, чтобы остановить програмку
    if user_input_comm == 'exit':
        break