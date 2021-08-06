
import os

os.system("cls")


print("Запуск...")
print("Настройка цветов текста...")
print("Настройка цветов    |     \u001b[32mOK\u001b[37m")
print("Настройка переменных...")
#переменные
print("Символьные          |     \u001b[32mOK\u001b[37m")
t1="Anonimus jopu HUCK"
print("Имитация картинок   |     \u001b[32mOK\u001b[37m")
p1='   mm   mm   m  mmmm  mm   m mmmmm  m    m m    m  mmmm\n   ##   #"m  # m"  "m #"m  #   #    ##  ## #    # #"   "\n  #  #  # #m # #    # # #m #   #    # ## # #    # "#mmm\n  #mm#  #  # # #    # #  # #   #    # "" # #    #     "#\n #    # #   ##  #mm#  #   ## mm#mm  #    # "mmmm" "mmm#"'
p2='  mmmm  mm   m m    m  mmmm\n #"   " #"m  # #    # #"   "\n "#mmm  # #m # #    # "#mmm\n     "# #  # # #    #     "#\n "mmm#" #   ## "mmmm" "mmm#"'
p3='  mmmm  m    m\n m"  "m #  m"\n #    # #m#\n #    # #  #m\n  #mm#  #   "m'
print("Ввод текста         |     \u001b[32mOK\u001b[37m")
#input("\u001b[33mWARNING: BAD_GENERAL_FILE \u001b[37m \nPress Enter to contineo...")
v1=input("Введите имя: ")
v2=input("Вы анонимус?(yes или no): ")
if v2=="no":
    print("\u001b[31mFATAL ERROR: USER_NOT_ANONIMUS\u001b[37m")
    input("Press Enter to contineo...")
elif v2=="yes":
    print('\u001b[32m  ')
    print(p1)
    print(' \n ')
    print('Дорогой '+v1+', вас пртветствует программа '+t1)
    print(' \n ')
    print(p2)
    print(' \n ')
    print('Подготока к взлому жопы...')
    print('Инициализация...')
    print('Подождите...')
    input("Press Enter to contineo...")
    for t1 in range(0,101):
        print(str(t1)+'% completed ')
    print(p3)
    print('')
    print('Подготовка к взлому выполнена успешно!!!')
    v3=input('Введите имя челоека жопа которого будет взломана: ')
    input("Press Enter to contineo...")
    for t2 in range(0,101):
        print(str(t2)+'% compleited')
    print(p3)
    print('Жопа пользователя '+v3+' взломана!!!')
    print('\u001b[31mWARNING!\nДальнейший этап "РАЗРЫ ОЧКА" опаен для пользователя '+v3+'!')
    v4=input("\u001b[32mХотите ли в продолжить?(yes или no): ")
    if v4=='yes':
        for t3 in range(0,101):
            print(str(t3)+'% completed')
        print('Взлом жопы с разрывом очка пользователю '+v3+' вполнен успешно!!!')
    else:
        print('Взлом жопы пользователю '+v3+' вполнен успешно!!!')
    print(p3)
    input('Press Enter to exit...')
else:
    print('Чиво!?')
    input()
