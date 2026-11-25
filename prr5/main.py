import sys
from alchemist import Alchemist
from database import POTIONS_POOL


def main():
    try:
        hero = Alchemist()
        day = 1
        TARGET_GOLD = 500  # Ціль: 500 золота
        MAX_DAYS = 10  # Ліміт: 10 днів

        print("=== ГРА: АЛХІМІК ===")
        print(f"Зіберіть {TARGET_GOLD} золота за {MAX_DAYS} днів, щоб виграти!\n")

        while day <= MAX_DAYS:
            print(f"\n📅 --- ДЕНЬ {day}/{MAX_DAYS} ---")
            print(f"💵 Баланс: {hero.gold}/{TARGET_GOLD} золота")

            hero.get_daily_ingredients()

            while True:
                try:
                    print("\n1. Інвентар")
                    print("2. Показати 5 рецептів")
                    print("3. Зварити зілля")
                    print("4. Продати зілля та закінчити день")
                    print("5. Вийти з гри")

                    choice = input("Вибір (1-5): ").strip()

                    if choice == "1":
                        hero.ingredients_inv.display("Інгредієнти")
                        hero.potions_inv.display("Зілля")
                    elif choice == "2":
                        print("\n📜 Доступні рецепти (перші 5):")
                        for name in list(POTIONS_POOL.keys())[:5]:
                            rec = ", ".join(POTIONS_POOL[name]["recipe"])
                            price = POTIONS_POOL[name]["price"]
                            print(f" • {name}: [{rec}] -> Ціна: {price}")
                    elif choice == "3":
                        name = input("Введіть назву (наприклад, 'Зілля №1'): ").strip()
                        hero.craft_potion(name)
                    elif choice == "4":
                        hero.sell_potions()
                        break
                    elif choice == "5":
                        sys.exit(0)
                except Exception as e:
                    print(f"[Помилка меню]: {e}")

            # Перевірка умови перемоги
            if hero.gold >= TARGET_GOLD:
                print(f"\n🎉 ПЕРЕМОГА! Ви зібрали {hero.gold} золота!")
                return

            day += 1

        print(f"\n💀 ПОРАЗКА! Дні закінчилися. Ви зібрали лише {hero.gold} золота.")
    except Exception as e:
        print(f"[Помилка гри]: {e}")


if __name__ == "__main__":
    main()