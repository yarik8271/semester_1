from database import POTIONS_POOL
from inventory_ops import show_inventory
from alchemy_ops import give_daily_ingredients, brew_potion, sell_all_potions


def print_some_recipes(limit=5):
    """Виводить кілька рецептів для підказки гравцю."""
    try:
        print(f"\n📜 Перші {limit} рецептів:")
        for name in list(POTIONS_POOL.keys())[:limit]:
            ing_text = ", ".join(POTIONS_POOL[name]["recipe"])
            price = POTIONS_POOL[name]["price"]
            print(f"  • {name}: [{ing_text}] -> {price} золота")
    except Exception as e:
        print(f"[Помилка виводу рецептів]: {e}")


def play_game():
    """Послідовний головний цикл гри."""
    try:
        ingredients_inv = {}  # до 25 слотів, стак по 25
        potions_inv = {}      # до 10 слотів, стак по 10
        gold = 0
        target_gold = 500
        max_days = 10
        day = 1

        print("=== АЛХІМІК (ВЕРСІЯ БЕЗ КЛАСІВ) ===")
        print(f"Мета: зібрати {target_gold} золота за {max_days} днів.")

        while day <= max_days:
            print(f"\n================ ДЕНЬ {day}/{max_days} ================")
            print(f"Золото: {gold}/{target_gold}")

            # 1. Видача 5 інгредієнтів
            give_daily_ingredients(ingredients_inv, max_slots=25, max_stack=25)

            # 2. Дії протягом дня
            while True:
                try:
                    print("\n1. Показати інвентарі")
                    print("2. Показати рецепти")
                    print("3. Зварити зілля")
                    print("4. Завершити день і продати зілля")

                    action = input("Оберіть дію (1-4): ").strip()

                    if action == "1":
                        show_inventory("Інгредієнти", ingredients_inv, max_slots=25, max_stack=25)
                        show_inventory("Зілля", potions_inv, max_slots=10, max_stack=10)
                    elif action == "2":
                        print_some_recipes(5)
                    elif action == "3":
                        potion_name = input("Введіть назву зілля (наприклад, Зілля №1): ").strip()
                        brew_potion(potion_name, ingredients_inv, potions_inv)
                    elif action == "4":
                        gold = sell_all_potions(potions_inv, gold)
                        break
                    else:
                        print("⚠️ Введіть число від 1 до 4.")
                except Exception as e:
                    print(f"[Помилка в меню дня]: {e}")

            # 3. Перевірка кінцівки (виграш)
            if gold >= target_gold:
                print(f"\n🎉 ВИГРАШ! Ви зібрали {gold} золота за {day} дн.!")
                return

            day += 1

        # 4. Логічна кінцівка (програш)
        print(f"\n💀 ПРОГРАШ! За {max_days} днів зібрано {gold} із {target_gold} золота.")
    except Exception as e:
        print(f"[Критична помилка гри]: {e}")


if __name__ == "__main__":
    play_game()