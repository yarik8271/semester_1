def create_ingredients_pool():
    """Створює 200 унікальних інгредієнтів."""
    try:
        prefixes = [
            "Місячний", "Сонячний", "Лісовий", "Печерний", "Вогняний",
            "Крижаний", "Тіньовий", "Драконячий", "Древній", "Магічний"
        ]
        bases = [
            "Корінь", "Квітка", "Лист", "Гриб", "Плід",
            "Пилок", "Кристал", "Камінь", "Перо", "Хвіст",
            "Ікла", "Луска", "Жовч", "Жало", "Сік",
            "Кора", "Мох", "Ягода", "Сльоза", "Руда"
        ]

        pool = []
        for p in prefixes:
            for b in bases:
                pool.append(f"{p} {b}")
        return pool  # 10 * 20 = 200
    except Exception as e:
        print(f"[Помилка створення інгредієнтів]: {e}")
        return ["Трава"]


def create_potions_pool(ingredients):
    """Створює 50 зілля з рецептами та цінами."""
    try:
        potions = {}
        for i in range(1, 51):
            potion_name = f"Зілля №{i}"
            ing1 = ingredients[(i - 1) % len(ingredients)]
            ing2 = ingredients[(i + 49) % len(ingredients)]
            potions[potion_name] = {
                "recipe": [ing1, ing2],
                "price": i * 20
            }
        return potions
    except Exception as e:
        print(f"[Помилка створення зілля]: {e}")
        return {}


INGREDIENTS_POOL = create_ingredients_pool()
POTIONS_POOL = create_potions_pool(INGREDIENTS_POOL)