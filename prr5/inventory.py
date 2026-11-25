import math


class Inventory:
    def __init__(self, max_slots, max_stack):
        self.max_slots = max_slots
        self.max_stack = max_stack
        self.items = {}  # {"Назва": кількість}

    def get_used_slots(self):
        """Рахує, скільки слотів зайнято."""
        try:
            slots = 0
            for count in self.items.values():
                slots += math.ceil(count / self.max_stack)
            return slots
        except Exception as e:
            print(f"[Помилка підрахунку слотів]: {e}")
            return 0

    def add_item(self, item_name, count=1):
        """Додає предмет в інвентар з урахуванням слотів."""
        try:
            current_slots = self.get_used_slots()
            # Якщо предмета немає і всі слоти зайняті — додати не можна
            if item_name not in self.items and current_slots >= self.max_slots:
                print(f"⚠️ Немає вільних слотів для '{item_name}'!")
                return False

            self.items[item_name] = self.items.get(item_name, 0) + count
            return True
        except Exception as e:
            print(f"[Помилка додавання предмета]: {e}")
            return False

    def remove_item(self, item_name, count=1):
        """Видаляє предмет з інвентарю."""
        try:
            if item_name not in self.items or self.items[item_name] < count:
                return False

            self.items[item_name] -= count
            if self.items[item_name] <= 0:
                del self.items[item_name]
            return True
        except Exception as e:
            print(f"[Помилка видалення предмета]: {e}")
            return False

    def display(self, title):
        """Виводить вміст інвентарю."""
        try:
            print(f"\n--- {title} (Слоти: {self.get_used_slots()}/{self.max_slots}) ---")
            if not self.items:
                print("  (Порожньо)")
            for item, count in self.items.items():
                print(f"  • {item}: {count} шт.")
        except Exception as e:
            print(f"[Помилка виводу інвентарю]: {e}")