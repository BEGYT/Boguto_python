def check_inequalities():
    while True:
        try:
            A = int(input("Введите целое число A: "))
            B = int(input("Введите целое число B: "))
            
            # Проверка неравенств
            if A > 2 and B < 3:
                print("Высказывание истинно: A > 2 и B < 3.")
            else:
                print("Высказывание ложно.")
            break  # Выход из цикла при успешном вводе
        except ValueError:
            print("Неправильно ввели! Пожалуйста, введите целые числа.")

check_inequalities()