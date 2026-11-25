import random
from inventory import Inventory
from database import INGREDIENTS_POOL, POTIONS_POOL


class Alchemist:
    def __init__(self):
        try:
            self.ingredients_inv = Inventory(max_slots=25, max_stack=25)
            self.potions_inv = Inventory(max_slots=10, max_stack=10)
            self.gold = 50
        except Exception as e:
            print(f"[Помилка створення алхіміка]: {e}")

    def get_daily_ingredients(self):
        """Видає 5 випадкових інгредієнтів щодня."""
        try:
            print("\n🎁 Отримано 5 інгредієнтів на день:")
            for _ in range(5):
                ing = random.choice(INGREDIENTS_POOL)
                if self.ingredients_inv.add_item(ing, 1):
                    print(f"  + {ing}")
        except Exception as e:
            print(f"[Помилка отримання інгредієнтів]: {e}")

    def craft_potion(self, potion_name):
        """Варить зілля, якщо вистачає інгредієнтів."""
        try:
            if potion_name not in POTIONS_POOL:
                print("❌ Такого зілля не існує!")
                return

            recipe = POTIONS_POOL[potion_name]["recipe"]

            # Перевірка наявності інгредієнтів
            for ing in recipe:
                if self.ingredients_inv.items.get(ing, 0) < 1:
                    print(f"❌ Не вистачає: {ing}")
                    return

            # Списуємо інгредієнти та додаємо зілля
            if self.potions_inv.add_item(potion_name, 1):
                for ing in recipe:
                    self.ingredients_inv.remove_item(ing, 1)
                print(f"🧪 Успішно зварено: {potion_name}!")
        except Exception as e:
            print(f"[Помилка варіння]: {e}")

    def sell_potions(self):
        """Продає все зілля в кінці дня."""
        try:
            if not self.potions_inv.items:
                print("🛒 Немає зілля для продажу.")
                return 0

            earned = 0
            for name, count in list(self.potions_inv.items.items()):
                price = POTIONS_POOL[name]["price"] * count
                earned += price
                self.potions_inv.remove_item(name, count)

            self.gold += earned
            print(f"💰 Продано зілля на суму: {earned} золота!")
            return earned
        except Exception as e:
            print(f"[Помилка продажу]: {e}")
            return 0