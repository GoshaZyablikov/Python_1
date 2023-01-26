print("Калькулятор")
number=0
print("1. Сумма "
"2. Вычитание "
"3. Умножение "
"4. Деление "
"5. Возведение в степень "
)
while (number<=0):
    number=int(input("Введите кол-во операций в примере: "))
figure1=float(input("Введите число: "))

while number>0:
    figure2=float(input("Введите число: "))
    function=int(input("Введите функцию: "))
    if (function==1):
        figure1=figure1+figure2
        print(f"Сумма {figure1}")
    elif(function == 2):
        figure1=figure1-figure2 
        print(f"Разность {figure1}")
    elif(function==3):
        figure1=figure1*figure2 
        print(f"Произведение {figure1}")
    elif(function==4):
        while (figure2==0):
            print("Мы не делим на нуль")
            figure2=float(input("Введите число: ")) 
        else:
            figure1=figure1/figure2 
            print(f"Частное {figure1}")
    elif(function==5):
        figure1=figure1**figure2
        print(f"Результат {figure1}")
    else:
        print("Такой операции нет")
    number-=1
print("Спасибо, что воспользовались нашим севрисом")