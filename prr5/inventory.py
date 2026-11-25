class Inventory:
    def __init__(self, max_slots, max_stack):
        self.max_slots = max_slots
        self.max_stack = max_stack
        # Структура: {"Назва": кількість}
        self.items = {}

    def add_item(self, item_name, count=1):
        """Додає предмет у відповідності до правил стакування та слотів."""
        try:
            if count <= 0:
                raise ValueError("Кількість для додавання має бути більше 0.")

            remaining = count

            # Якщо предмет вже є в інвентарі, доповнюємо існуючі слоти
            if item_name in self.items:
                current_count = self.items[item_name]
                space_in_current_stack = self.max_stack - (current_count % self.max_stack)
                if space_in_current_stack < self.max_stack:
                    to_add = min(remaining, space_in_current_stack)
                    self.items[item_name] += to_add
                    remaining -= to_add

            # Обчислюємо скільки нових слотів потрібно для залишку
            while remaining > 0:
                used_slots = self.get_used_slots()
                if used_slots >= self.max_slots:
                    print(f"⚠️  Інвентар заповнений! Не вдалося додати {remaining}x '{item_name}'.")
                    return False

                to_add = min(remaining, self.max_stack)
                self.items[item_name] = self.items.get(item_name, 0) + to_add
                remaining -= to_add

            return True
        except Exception as e:
            print(f"[Помилка додавання в інвентар]: {e}")
            return False

    def remove_item(self, item_name, count=1):
        """Видаляє предмет з інвентарю."""
        try:
            if item_name not in self.items or self.items[item_name] < count:
                raise ValueError(f"Недостатньо '{item_name}' в інвентарі.")

            self.items[item_name] -= count
            if self.items[item_name] <= 0:
                del self.items[item_name]
            return True
        except Exception as e:
            print(f"❌ {e}")
            return False

    def get_used_slots(self):
        """Обчислює кількість зайнятих слотів."""
        try:
            import math
            slots = 0
            for count in self.items.values():
                slots += math.ceil(count / self.max_stack)
            return slots
        except Exception as e:
            print(f"[Помилка підрахунку слотів]: {e}")
            return 0

    def display(self, title):
        """Відображає вміст інвентарю."""
        try:
            print(f"\n--- {title} (Слоти: {self.get_used_slots()}/{self.max_slots}) ---")
            if not self.items:
                print(" (Порожньо)")
            else:
                for item, count in self.items.items():
                    print(f" • {item}: {count} шт.")
        except Exception as e:
            print(f"[Помилка відображення інвентарю]: {e}")
            