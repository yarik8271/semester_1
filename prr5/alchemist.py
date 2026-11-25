import random
from inventory import Inventory
from database import INGREDIENTS_POOL, POTIONS_POOL


class Alchemist:
    def __init__(self):
        try:
            self.potions_inv = Inventory(max_slots=10, max_stack=10)
            self.ingredients_inv = Inventory(max_slots=25, max_stack=25)
            self.gold = 50
        except Exception as e:
            print(f"[Помилка ініціалізації Алхіміка]: {e}")

    def receive_daily_ingredients(self):
        """Видає 5 випадкових інгредієнтів кожного дня."""
        try:
            print("\n🎁 Ранкове постачання інгредієнтів:")
            given = random.choices(INGREDIENTS_POOL, k=5)
            for ing in given:
                if self.ingredients_inv.add_item(ing, 1):
                    print(f" + Отримано: {ing}")
        except Exception as e:
            print(f"[Помилка отримання щоденних інгредієнтів]: {e}")

    def craft_potion(self, potion_name):
        """Варка зілля з перевіркою наявності інгредієнтів."""
        try:
            if potion_name not in POTIONS_POOL:
                raise KeyError("Такого зілля не існує в рецептах.")

            recipe = POTIONS_POOL[potion_name]["recipe"]

            # Перевірка наявності всіх необхідних інгредієнтів
            for ing in recipe:
                if self.ingredients_inv.items.get(ing, 0) < 1:
                    print(f"❌ Не вистачає інгредієнта: {ing}")
                    return False

            # Перевірка вільного місця під зілля
            if self.potions_inv.get_used_slots() >= 10 and potion_name not in self.potions_inv.items:
                print("❌ Немає вільних слотів під нове зілля!")
                return False

            # Списання інгредієнтів
            for ing in recipe:
                self.ingredients_inv.remove_item(ing, 1)

            # Додавання зілля
            self.potions_inv.add_item(potion_name, 1)
            print(f"🧪 Успішно зварено зілля: '{potion_name}'!")
            return True

        except KeyError as ke:
            print(f"❌ Помилка: {ke}")
        except Exception as e:
            print(f"[Помилка процесу варіння]: {e}")
            return False

    def sell_potions(self):
        """Продаж усіх зварених зілля в кінці дня."""
        try:
            if not self.potions_inv.items:
                print("🛒 У вас немає зілля для продажу.")
                return 0

            total_earned = 0
            print("\n💰 Продаж зілля ярмарку:")

            # Робимо копію ключів для безпечного видалення під час ітерації
            for potion_name, count in list(self.potions_inv.items.items()):
                price_per_one = POTIONS_POOL[potion_name]["price"]
                earned = price_per_one * count
                total_earned += earned
                print(f" • Продано {count}x '{potion_name}' за {earned} золотих.")
                self.potions_inv.remove_item(potion_name, count)

            self.gold += total_earned
            print(f"💵 Загальний прибуток за день: {total_earned} золотих. Поточний баланс: {self.gold}")
            return total_earned

        except Exception as e:
            print(f"[Помилка під час продажу]: {e}")
            return 0