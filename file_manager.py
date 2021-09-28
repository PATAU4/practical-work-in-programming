import os
import shutil
import settings
import platform




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
            if(platform.system()) == 'Darwin' or (platform.system()) == 'linux' or (platform.system()) == 'linux2':
                os.remove( str(n)+'/'+str(i) )
                if os.listdir(n) == []:
                    os.listdir(n) == []
                    os.rmdir(n)
                    print(f'Готово!\nРепозиторий {n} был удален')
                else:
                    os.listdir(n) == []
                    os.rmdir(n)
                    print(f'Готово!\nРепозиторий {n} был удален')
            else:
                os.remove( str(n)+ '\\' + str(i) )
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
    if(platform.system()) == 'Darwin' or (platform.system()) == 'linux' or (platform.system()) == 'linux2':
        for i in (os.listdir(fromm)):
            tmp = i
            tmp_new_file = i
            tmp = str(fromm)+'/'+str(tmp)
            print(tmp)
            open(tmp_new_file,'a').close()
            shutil.copy(tmp , tmp_new_file)
            shutil.move(tmp_new_file, to)
            print(f'Готово!\nСодержание папки {fromm} было копировано в папку {to}')
    else:
        for i in (os.listdir(fromm)):
            tmp = i
            tmp_new_file = i
            tmp = str(fromm)+'\\'+str(tmp)
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
        print('Список команд:\nexit, mkdrt, removefl, removedrt, mkfl, newname, mvto, cpfl, cpdrt, actwfl, lst, go')





        # if, которые определяют команду по первому слову ввода и вызывают соответствующую функцию

    elif (user_input_comm.split(' ')[0]) == 'mkdrt':
        if(platform.system()) == 'Darwin' or (platform.system()) == 'linux' or (platform.system()) == 'linux2':
            mk_dir(str(main_path)+'/'+str(user_input_comm.split(' ')[1]))
        else:
            mk_dir(str(main_path)+'\\'+str(user_input_comm.split(' ')[1]))

    elif (user_input_comm.split(' ')[0]) == 'mkfl':
        if(platform.system()) == 'Darwin' or (platform.system()) == 'linux' or (platform.system()) == 'linux2':
            mk_file_v2(str(main_path)+'/'+str(user_input_comm.split(' ')[1]))
        else:
            mk_file_v2(str(main_path)+'\\'+str(user_input_comm.split(' ')[1]))

    elif (user_input_comm.split(' ')[0]) == 'removefl':
        if(platform.system()) == 'Darwin' or (platform.system()) == 'linux' or (platform.system()) == 'linux2':
            remove_file(str(main_path)+'/'+str(user_input_comm.split(' ')[1]))
        else:
            remove_file(str(main_path)+'\\'+str(user_input_comm.split(' ')[1]))

    elif (user_input_comm.split(' ')[0]) == 'removedrt':
        if(platform.system()) == 'Darwin' or (platform.system()) == 'linux' or (platform.system()) == 'linux2':
            rm_dir(str(main_path)+'/'+str(user_input_comm.split(' ')[1]))
        else:
            rm_dir(str(main_path)+'\\'+str(user_input_comm.split(' ')[1]))

    elif (user_input_comm.split(' ')[0]) == 'newname':
        if(platform.system()) == 'Darwin' or (platform.system()) == 'linux' or (platform.system()) == 'linux2':
            rename_file((str(main_path)+'/'+str(user_input_comm.split(' ')[1])), (str(main_path)+'/'+str(user_input_comm.split(' ')[2])))
        else:
            rename_file((str(main_path)+'\\'+str(user_input_comm.split(' ')[1])), (str(main_path)+'\\'+str(user_input_comm.split(' ')[2])))

    elif (user_input_comm.split(' ')[0]) == 'mvto':
        if(platform.system()) == 'Darwin' or (platform.system()) == 'linux' or (platform.system()) == 'linux2':
            mv((str(main_path)+'/'+str(user_input_comm.split(' ')[1])), (str(main_path)+'/'+str(user_input_comm.split(' ')[2])))
        else:
            mv((str(main_path)+'\\'+str(user_input_comm.split(' ')[1])), (str(main_path)+'\\'+str(user_input_comm.split(' ')[2])))

    elif (user_input_comm.split(' ')[0]) == 'cpfl':
        if(platform.system()) == 'Darwin' or (platform.system()) == 'linux' or (platform.system()) == 'linux2':
            cpf((str(main_path)+'/'+str(user_input_comm.split(' ')[1])), (str(main_path)+'/'+str(user_input_comm.split(' ')[2])))
        else:
            cpf((str(main_path)+'\\'+str(user_input_comm.split(' ')[1])), (str(main_path)+'\\'+str(user_input_comm.split(' ')[2])))

    elif (user_input_comm.split(' ')[0]) == 'cpdrt':
        if(platform.system()) == 'Darwin' or (platform.system()) == 'linux' or (platform.system()) == 'linux2':
            cpdir((str(main_path)+'/'+str(user_input_comm.split(' ')[1])), (str(main_path)+'/'+str(user_input_comm.split(' ')[2])))
        else:
            cpdir((str(main_path)+'\\'+str(user_input_comm.split(' ')[1])), (str(main_path)+'\\'+str(user_input_comm.split(' ')[2])))

    elif (user_input_comm.split(' ')[0]) == 'actwfl':
        if(platform.system()) == 'Darwin' or (platform.system()) == 'linux' or (platform.system()) == 'linux2':
            cat(str(main_path)+'/'+str(user_input_comm.split(' ')[1]))
        else:
            cat(str(main_path)+'\\'+str(user_input_comm.split(' ')[1]))

    elif (user_input_comm.split(' ')[0]) == 'lst':
        if(platform.system()) == 'Darwin' or (platform.system()) == 'linux' or (platform.system()) == 'linux2':
            ls(str(main_path)+'/'+str(user_input_comm.split(' ')[1]))
        else:
            ls(str(main_path)+'\\'+str(user_input_comm.split(' ')[1]))

    elif (user_input_comm.split(' ')[0]) == 'go' and (user_input_comm.split(' ')[1]) != 'back' or (user_input_comm.split(' ')[1]) != '~':
        if(platform.system()) == 'Darwin' or (platform.system()) == 'linux' or (platform.system()) == 'linux2':
            cd(str(main_path)+'/'+str(user_input_comm.split(' ')[1]))
        else:
            cd(str(main_path)+'\\'+str(user_input_comm.split(' ')[1]))

    elif (user_input_comm.split(' ')[0]) == 'go' and (user_input_comm.split(' ')[1]) == 'back':
        cd_back()

    elif (user_input_comm.split(' ')[0]) == 'go' and (user_input_comm.split(' ')[1]) == '~':
        cd_main()



    elif user_input_comm == 'man mkdrt':
        print('mkdrt - создает директории\nсинтаксис: <mkdrt "название создаваемого репозитория">')
    elif user_input_comm == 'man exit':
        print('exit - останавливает работу файлового менеджера. зачем вы вообще это запускали...')
    elif user_input_comm == 'man removefl':
        print('removefl - удаляет файл\nсинтаксис: <removefl "название удаляемого файла">')
    elif user_input_comm == 'man rmdir':
        print('removedrt - удаляет директорию\nсинтаксис: <removedrt "название удаляемого репозитория">')
    elif user_input_comm == 'man mkfl':
        print('mkfl - создает пустой файл\nсинтаксис: <mkfl "название создаваемого файла">')
    elif user_input_comm == 'man newname':
        print('newname - переименовывает название файла\nсинтаксис: <newname "название файла который хотите переименовать, название файла на который хотите переименовать">')
    elif user_input_comm == 'man mvto':
        print('mvto - перемещает файлы\nСинтаксис: <mvto "название файла который хотите переместить, название куда хотите переместить файл">')
    elif user_input_comm == 'man cpfl':
        print('cpfl - копирует содержимое одного файла в другой\nсинтаксис: <cpfl "название файла откуда копируется данные, название файла куда копируется данные">')
    elif user_input_comm == 'man cpdrt':
        print('cpdrt - копирует файлы из одного репозитория в другой\nсинтаксис: <cpdrt "название директории откуда копируются файлы, название репозитория куда копируются файлы">')
    elif user_input_comm == 'man actwfl':
        print('actwfl - осуществляет запись либо чтение из указанного файла\nсинтаксис:\nзапись -- <actwfl -> "название файла который хотите открыть на чтение">\nчтение -- <actwfl "название файла который хотите открыть на чтение">')
    elif user_input_comm == 'man lst':
        print('lst - показывает содержимое директории\nсинтаксис: <lst "название директории">')
    elif user_input_comm == 'man go':
        print('go - позволяет перемещаться между директориями\nсинтаксис:\n<go "название ПОДдиректории">\n<go "back"> (осуществляет переход к главной директории)\n<go ~>(осуществляет переход в main каталог)')



        
     # выход из цикла, чтобы остановить програмку
    elif user_input_comm == 'exit':
        break