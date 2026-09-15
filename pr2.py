users_db = {
    "yaryk": {
        "password": "pass123",
        "grades": [11, 10, 12, 8, 9, 4, 7]
    },
    "maksym": {
        "password": "user456",
        "grades": [4, 3, 2, 5, 4, 6]
    },
    "olena": {
        "password": "qwerty789",
        "grades": [12, 11, 10, 11, 12, 9]
    },
    "dmytro": {
        "password": "admin321",
        "grades": [2, 5, 8, 3, 6, 1, 10, 4]
    }
}

def ide():
    print("=== АВТОРИЗАЦІЯ В СИСТЕМІ ===")
    login = input("Введіть логін: ").strip()
    password = input("Введіть пароль: ").strip()

    if login in users_db and users_db[login]["password"] == password:
        user_data = users_db[login]
        grades = user_data["grades"]

        satisfactory_count = sum(1 for g in grades if 5 <= g <= 12)
        unsatisfactory_count = sum(1 for g in grades if 1 <= g <= 4)

        print("\n--- Успішний вхід! ---")
        print("Користувач:", login)
        print("Всі виставлені оцінки:", grades)
        print("Кількість задовільних оцінок (5-12):", satisfactory_count)
        print("Кількість незадовільних оцінок (1-4):", unsatisfactory_count)
    else:
        print("\nПомилка: Невірний логін або пароль. Доступ заборонено.")

ide()