import random
from database import INGREDIENTS_POOL, POTIONS_POOL
from inventory_ops import add_to_inventory, remove_from_inventory


def give_daily_ingredients(ingredients_inv, max_slots=25, max_stack=25):
    """Видає 5 випадкових інгредієнтів на початок ігрового дня."""
    try:
        print("\n🎁 Щоденні інгредієнти (+5):")
        for _ in range(5):
            ing = random.choice(INGREDIENTS_POOL)
            added = add_to_inventory(ingredients_inv, ing, 1, max_slots, max_stack)
            if added:
                print(f"  + {ing}")
    except Exception as e:
        print(f"[Помилка видачі інгредієнтів]: {e}")


def brew_potion(potion_name, ingredients_inv, potions_inv):
    """Варить зілля, списує інгредієнти та кладе готове зілля в інвентар."""
    try:
        if potion_name not in POTIONS_POOL:
            print("❌ Такого зілля немає в книзі рецептів.")
            return False

        recipe = POTIONS_POOL[potion_name]["recipe"]

        # Перевіряємо, чи є потрібні інгредієнти
        for ing in recipe:
            if ingredients_inv.get(ing, 0) < 1:
                print(f"❌ Не вистачає інгредієнта: {ing}")
                return False

        # Пробуємо покласти зілля (ліміт: 10 слотів, стак по 10)
        added = add_to_inventory(potions_inv, potion_name, 1, max_slots=10, max_stack=10)
        if not added:
            return False

        # Списуємо інгредієнти після успішного додавання зілля
        for ing in recipe:
            remove_from_inventory(ingredients_inv, ing, 1)

        print(f"🧪 Зварено: {potion_name}!")
        return True
    except Exception as e:
        print(f"[Помилка варіння зілля]: {e}")
        return False


def sell_all_potions(potions_inv, gold):
    """Продаж усіх зварених зілля в кінці дня. Повертає новий баланс золота."""
    try:
        if not potions_inv:
            print("🛒 Зілля для продажу немає.")
            return gold

        earned = 0
        for potion_name, qty in list(potions_inv.items()):
            price = POTIONS_POOL[potion_name]["price"]
            earned += price * qty
            remove_from_inventory(potions_inv, potion_name, qty)

        new_gold = gold + earned
        print(f"💰 Продано зілля на {earned} золота. Баланс: {new_gold}")
        return new_gold
    except Exception as e:
        print(f"[Помилка продажу зілля]: {e}")
        return gold