# Лямбда-функція для форматування ціни згідно з умовою
format_price = lambda price: f"{price:.2f}грн"


def show_menu():
    print("\n" + "=" * 35)
    print(" Міні-магазин компонентів")
    print("=" * 35)
    print("1. Переглянути каталог")
    print("2. Переглянути кошик")
    print("3. Додати товар в кошик")
    print("4. Видалити товар з кошика")
    print("5. Оформити замовлення (купити)")
    print("6. Увійти як адміністратор (залишки)")
    print("0. Вийти")
    print("=" * 35)


def show_catalog(catalog):
    print("\n--- Каталог товарів ---")
    for p_id, info in catalog.items():
        print(f"[{p_id}] {info['name']} — {format_price(info['price'])}")


def view_cart(cart, catalog):
    if not cart:
        print("\nВаш кошик порожній.")
        return False

    print("\n--- Ваш кошик ---")
    # Використання лямбда-функції для підрахунку загальної суми
    calc_total = lambda: sum(catalog[p_id]['price'] * qty for p_id, qty in cart.items())

    for p_id, qty in cart.items():
        name = catalog[p_id]['name']
        total_item_price = catalog[p_id]['price'] * qty
        print(f"[{p_id}] {name} (x{qty}) = {format_price(total_item_price)}")

    print(f"-" * 25)
    print(f"Загальна сума до оплати: {format_price(calc_total())}")
    return True


def add_to_cart(catalog, cart):
    show_catalog(catalog)
    try:
        p_id = int(input("\nВведіть ID товару для додавання: "))
        if p_id not in catalog:
            print("❌ Товар з таким ID не знайдено.")
            return

        qty = int(input("Введіть кількість: "))
        if qty <= 0:
            print("❌ Кількість має бути більшою за 0.")
            return

        available = catalog[p_id]['stock']
        current_in_cart = cart.get(p_id, 0)

        if current_in_cart + qty > available:
            print(f"❌ Недостатньо товару на складі. Максимально доступно: {available}")
        else:
            cart[p_id] = current_in_cart + qty
            print("✅ Товар успішно додано в кошик!")
    except ValueError:
        print("❌ Помилка вводу. Будь ласка, введіть число.")


def remove_from_cart(catalog, cart):
    if not view_cart(cart, catalog):
        return

    try:
        p_id = int(input("\nВведіть ID товару для видалення: "))
        if p_id not in cart:
            print("❌ Цього товару немає у вашому кошику.")
            return

        qty = int(input("Введіть кількість для видалення: "))
        if qty <= 0:
            print("❌ Кількість має бути більшою за 0.")
            return

        if qty >= cart[p_id]:
            del cart[p_id]
            print("✅ Товар повністю видалено з кошика.")
        else:
            cart[p_id] -= qty
            print("✅ Кількість товару в кошику зменшено.")
    except ValueError:
        print("❌ Помилка вводу. Будь ласка, введіть число.")


def checkout(catalog, cart):
    if not view_cart(cart, catalog):
        return

    confirm = input("\nПідтверджуєте покупку? (так/ні): ").strip().lower()
    if confirm in ['так', 'т', 'yes', 'y']:
        # Списання залишків зі складу після успішної покупки
        for p_id, qty in cart.items():
            catalog[p_id]['stock'] -= qty
        cart.clear()
        print("✅ Дякуємо за покупку! Замовлення успішно оформлено.")
    else:
        print("Оформлення скасовано.")


def admin_panel(catalog):
    password = input("\nВведіть пароль адміністратора: ")
    if password == "admin":  # Простий пароль для лаби
        print("\n--- Залишки на складі ---")
        for p_id, info in catalog.items():
            print(f"[{p_id}] {info['name']} — Залишок: {info['stock']} шт. (Ціна: {format_price(info['price'])})")
    else:
        print("❌ Невірний пароль!")


def main():
    # База товарів (id: деталі)
    catalog = {
        1: {"name": "Пластик PETG Bambu Lab", "price": 899.00, "stock": 15},
        2: {"name": "Акумулятор BAK 21700 5000mAh", "price": 145.50, "stock": 50},
        3: {"name": "Плата захисту BMS 5S 100A", "price": 350.00, "stock": 20},
        4: {"name": "Orange Pi 3B", "price": 2150.00, "stock": 5}
    }
    cart = {}  # Словник для кошика: {item_id: кількість}

    while True:
        show_menu()
        choice = input("Оберіть дію (0-6): ").strip()

        if choice == '1':
            show_catalog(catalog)
        elif choice == '2':
            view_cart(cart, catalog)
        elif choice == '3':
            add_to_cart(catalog, cart)
        elif choice == '4':
            remove_from_cart(catalog, cart)
        elif choice == '5':
            checkout(catalog, cart)
        elif choice == '6':
            admin_panel(catalog)
        elif choice == '0':
            print("До побачення!")
            break
        else:
            print("❌ Невідома команда. Спробуйте ще раз.")


if __name__ == "__main__":
    main()