def calculate_ideal_weight():
    try:
        height = float(input("Введите ваш рост в сантиметрах: "))

        gender = input("Введите ваш пол (м/ж): ").strip().lower()


        if gender == 'м':
            # Формула Девина для мужчин
            ideal_weight = 50 + 0.9 * (height - 152.4)
        elif gender == 'ж':
            # Формула Девина для женщин
            ideal_weight = 45.5 + 0.9 * (height - 152.4)
        else:
            print("Некорректный ввод пола.")
            return

        print(f"Ваш идеальный вес: {ideal_weight:.2f} кг")
    except ValueError:
        print("Пожалуйста, введите корректные числовые значения.")

calculate_ideal_weight()