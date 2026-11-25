def generate_ingredients_pool():
    """Створює 200 унікальних інгредієнтів."""
    try:
        prefixes = ["Місячний", "Сонячний", "Лісовий", "Печерний", "Вогняний", "Крижаний", "Тіньовий", "Драконячий",
                    "Древній", "Магічний"]
        bases = ["Корінь", "Квітка", "Лист", "Гриб", "Плід", "Пилок", "Кристал", "Камінь", "Перо", "Хвіст", "Ікла",
                 "Луска", "Жовч", "Жало", "Сік", "Кора", "Мох", "Ягода", "Сльоза", "Руда"]

        ingredients = []
        for p in prefixes:
            for b in bases:
                ingredients.append(f"{p} {b}")
        return ingredients  # 10 * 20 = 200 елементів
    except Exception as e:
        print(f"[Помилка бази інгредієнтів]: {e}")
        return ["Трава"]


def generate_potions_pool(ingredients):
    """Створює 50 зілля з цінами та рецептами."""
    try:
        potions = {}
        for i in range(1, 51):
            name = f"Зілля №{i}"
            # Беремо 2 інгредієнти за індексом
            ing1 = ingredients[(i - 1) % len(ingredients)]
            ing2 = ingredients[(i + 49) % len(ingredients)]

            potions[name] = {
                "recipe": [ing1, ing2],
                "price": i * 20  # Ціна від 20 до 1000
            }
        return potions
    except Exception as e:
        print(f"[Помилка бази зілля]: {e}")
        return {}


INGREDIENTS_POOL = generate_ingredients_pool()
POTIONS_POOL = generate_potions_pool(INGREDIENTS_POOL)