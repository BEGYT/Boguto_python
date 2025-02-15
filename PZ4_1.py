
while True:
    try:
        price_per_kg = float(input("Введите цену 1 кг конфет: "))
        if price_per_kg < 0:
            print("Цена должна быть положительной. Попробуйте еще раз.")
            continue
        break
    except ValueError:
        print("Неправильно ввели! Попробуйте еще раз.")

print("Стоимость конфет:")
for i in range(1, 11): 
    weight = i / 10  
    cost = weight * price_per_kg
    print(f"{weight:.1f} кг: {cost:.2f} руб.")
