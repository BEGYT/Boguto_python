def determine_color():
    while True:
        try:
            wavelength = float(input("Введите длину волны в нанометрах (нм): "))
            
            # Определение цвета в зависимости от длины волны
            if 620 <= wavelength <= 750:
                color = "Красный"
            elif 590 <= wavelength < 620:
                color = "Оранжевый"
            elif 570 <= wavelength < 590:
                color = "Желтый"
            elif 495 <= wavelength < 570:
                color = "Зеленый"
            elif 450 <= wavelength < 495:
                color = "Голубой"
            elif 380 <= wavelength < 450:
                color = "Фиолетовый"
            else:
                color = "Длина волны вне видимого спектра."
            
            print("Цвет:", color)
            break  # Выход из цикла при успешном вводе
        except ValueError:
            print("Неправильно ввели! Пожалуйста, введите числовое значение.")

determine_color()