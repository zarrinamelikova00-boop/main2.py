from storage import load_budget, save_budget


CATEGORIES = ["еда", "транспорт", "развлечения"]


def input_positive_number(prompt):
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            value = float(raw)
        except ValueError:
            print("Ошибка: введите число (например, 1500 или 250.5).")
            continue

        if value <= 0:
            print("Ошибка: сумма должна быть больше нуля.")
            continue

        return value


def choose_category():
    print("Выберите категорию:")
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"  {i}. {cat}")
    print(f"  {len(CATEGORIES) + 1}. другая категория")

    choice = input("Ваш выбор: ").strip()
    if choice.isdigit():
        idx = int(choice)
        if 1 <= idx <= len(CATEGORIES):
            return CATEGORIES[idx - 1]
        if idx == len(CATEGORIES) + 1:
            custom = input("Введите название категории: ").strip().lower()
            return custom if custom else "другое"

    return choice.lower() if choice else "другое"


def add_transaction(data):
    print("\n--- Добавление операции ---")
    while True:
        tx_type = input("Тип операции (доход / расход): ").strip().lower()
        if tx_type in ("доход", "расход"):
            break
        print("Введите 'доход' или 'расход'.")

    amount = input_positive_number("Введите сумму: ")
    category = choose_category()

    transaction = {
        "type": tx_type,
        "amount": amount,
        "category": category,
    }
    data["transactions"].append(transaction)
    save_budget(data)
    print("Операция успешно добавлена и сохранена.")

    if tx_type == "расход":
        check_limit_warning(data)


def calculate_balance(data):
    income = sum(t["amount"] for t in data["transactions"] if t["type"] == "доход")
    expense = sum(t["amount"] for t in data["transactions"] if t["type"] == "расход")
    return income - expense, income, expense


def show_balance(data):
    balance, income, expense = calculate_balance(data)
    print("\n--- Текущий баланс ---")
    print(f"Доходы:  {income:.2f}")
    print(f"Расходы: {expense:.2f}")
    print(f"Баланс:  {balance:.2f}")


def show_expenses_by_category(data):
    expenses = {}
    for t in data["transactions"]:
        if t["type"] == "расход":
            cat = t["category"]
            expenses[cat] = expenses.get(cat, 0.0) + t["amount"]

    print("\n--- Расходы по категориям ---")
    if not expenses:
        print("Расходов пока нет.")
        return

    for cat, total in expenses.items():
        print(f"  {cat}: {total:.2f}")

    top_category = max(expenses, key=expenses.get)
    top_amount = expenses[top_category]
    print(f"Самая затратная категория: {top_category} ({top_amount:.2f})")


def set_monthly_limit(data):
    print("\n--- Месячный лимит трат ---")
    current_limit = data.get("limit", 0)
    print(f"Текущий лимит: {current_limit:.2f}")
    new_limit = input_positive_number("Введите новый месячный лимит: ")
    data["limit"] = new_limit
    save_budget(data)
    print(f"Новый лимит установлен: {new_limit:.2f}")
    check_limit_warning(data)


def check_limit_warning(data):
    limit = data.get("limit", 0)
    if limit <= 0:
        return
    total_expense = sum(t["amount"] for t in data["transactions"] if t["type"] == "расход")
    if total_expense > limit:
        diff = total_expense - limit
        print(f"⚠️ ВНИМАНИЕ! Превышен месячный лимит на {diff:.2f} (расходы: {total_expense:.2f}, лимит: {limit:.2f}).")


def print_menu():
    print("\n=== ЛИЧНЫЙ БЮДЖЕТ ===")
    print("1. Добавить операцию")
    print("2. Показать текущий баланс")
    print("3. Расходы по категориям и самая затратная категория")
    print("4. Установить месячный лимит трат")
    print("5. Выход")


def main():
    data = load_budget()
    check_limit_warning(data)

    while True:
        print_menu()
        choice = input("Выберите пункт меню: ").strip()
        if choice == "1":
            add_transaction(data)
        elif choice == "2":
            show_balance(data)
        elif choice == "3":
            show_expenses_by_category(data)
        elif choice == "4":
            set_monthly_limit(data)
        elif choice == "5":
            save_budget(data)
            print("Данные сохранены. До встречи!")
            break
        else:
            print("Неверный пункт меню. Выберите число от 1 до 5.")

        if name == "main":
            main()