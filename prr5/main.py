import sys
from alchemist import Alchemist
from database import POTIONS_POOL


def show_recipes():
    """Відображає доступні рецепти."""
    try:
        print("\n📜 КНИГА РЕЦЕПТІВ (Топ-10 доступних):")
        for i, (name, data) in enumerate(list(POTIONS_POOL.items())[:10], 1):
            ing_str = ", ".join(data["recipe"])
            print(f" {i}. {name} | Потрібно: [{ing_str}] | Ціна: {data['price']} gold")
    except Exception as e:
        print(f"[Помилка відображення рецептів]: {e}")


def main():
    try:
        hero = Alchemist()
        day = 1
        TARGET_GOLD = 1000  # Умова перемоги: зібрати 1000 золота
        MAX_DAYS = 15  # Умова поразки: не встигнути за 15 днів

        print("==================================================")
        print("  🧙‍♂️ ЛАБОРАТОРНА №5: РПГ АЛХІМІК ")
        print("==================================================")
        print(f"Ціль: Зібрати {TARGET_GOLD} золота за {MAX_DAYS} днів.")

        while day <= MAX_DAYS:
            print(f"\n=================== ДЕНЬ {day}/{MAX_DAYS} ===================")
            print(f"💰 Золото: {hero.gold}/{TARGET_GOLD}")

            # Ранкова фаза: отримання інгредієнтів
            hero.receive_daily_ingredients()

            # Денна фаза: дії гравця
            while True:
                try:
                    print("\nОберіть дію:")
                    print("1. Переглянути інвентар")
                    print("2. Переглянути рецепти зілля")
                    print("3. Зварити зілля")
                    print("4. Завершити день та продати зілля")
                    print("5. Вийти з гри")

                    choice = input("Ваш вибір (1-5): ").strip()

                    if choice == "1":
                        hero.ingredients_inv.display("Інвентар Інгредієнтів")
                        hero.potions_inv.display("Інвентар Зілля")
                    elif choice == "2":
                        show_recipes()
                    elif choice == "3":
                        potion_name = input("Введіть точну назву зілля для варіння: ").strip()
                        hero.craft_potion(potion_name)
                    elif choice == "4":
                        print("\n🌙 День закінчується. Ви йдете на ринок...")
                        hero.sell_potions()
                        break
                    elif choice == "5":
                        print("Вихід з гри...")
                        sys.exit(0)
                    else:
                        print("⚠️ Некоректний вибір. Спробуйте ще раз.")

                except Exception as e:
                    print(f"[Помилка обробки меню]: {e}")

            # Логічна перевірка Кінцівки гри
            if hero.gold >= TARGET_GOLD:
                print("\n🎉 ================================================= 🎉")
                print(f" ПЕРЕМОГА! Ви заробили {hero.gold} золотих і стали Майстром Алхімії!")
                print("🎉 ================================================= 🎉")
                return

            day += 1

        # Якщо дні закінчилися, а золото не зібрано
        print("\n💀 ================================================= 💀")
        print(f" ПОРАЗКА! Час вийшов (15 днів). Ви не змогли сплатити оренду лавки.")
        print("💀 ================================================= 💀")

    except Exception as e:
        print(f"[Критична помилка гри]: {e}")


if __name__ == "__main__":
    main()