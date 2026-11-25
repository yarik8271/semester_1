import math


def count_used_slots(items, max_stack):
    """Рахує зайняті слоти з урахуванням розміру стака."""
    try:
        slots = 0
        for qty in items.values():
            slots += math.ceil(qty / max_stack)
        return slots
    except Exception as e:
        print(f"[Помилка підрахунку слотів]: {e}")
        return 0


def add_to_inventory(items, item_name, count, max_slots, max_stack):
    """Додає предмет у словник інвентарю, якщо вистачає слотів."""
    try:
        if count <= 0:
            return False

        used_slots = count_used_slots(items, max_stack)
        # Якщо предмета ще немає і всі слоти зайняті — додати не можна
        if item_name not in items and used_slots >= max_slots:
            print(f"⚠️ Немає вільних слотів для '{item_name}'!")
            return False

        items[item_name] = items.get(item_name, 0) + count
        return True
    except Exception as e:
        print(f"[Помилка додавання в інвентар]: {e}")
        return False


def remove_from_inventory(items, item_name, count=1):
    """Видаляє вказану кількість предмета з інвентарю."""
    try:
        if item_name not in items or items[item_name] < count:
            return False

        items[item_name] -= count
        if items[item_name] <= 0:
            del items[item_name]
        return True
    except Exception as e:
        print(f"[Помилка видалення з інвентарю]: {e}")
        return False


def show_inventory(title, items, max_slots, max_stack):
    """Виводить вміст інвентарю в консоль."""
    try:
        used = count_used_slots(items, max_stack)
        print(f"\n--- {title} (Слоти: {used}/{max_slots}, стак: {max_stack}) ---")
        if not items:
            print("  (Порожньо)")
            return
        for name, qty in items.items():
            slots_for_item = math.ceil(qty / max_stack)
            print(f"  • {name}: {qty} шт. (слотів: {slots_for_item})")
    except Exception as e:
        print(f"[Помилка виводу інвентарю]: {e}")