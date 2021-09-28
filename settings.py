import os
# здесь проверяется существование указанной директории
while True:
    main_path = input('Чтобы продолжить работу в файловом менеджере, укажите основную директорию:\n')
    main_path_tmp = main_path
    check_file = os.path.exists(main_path) 
    if check_file is True:
        print(f'Ваша рабочая директория {main_path}')
        break
    else:
        print('Указанное расположение директории не было найдено')
        continue