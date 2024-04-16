def add_contact():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    with open("phonebook.txt", "a") as file:
        file.write(f"{surname} {name} {patronymic}: {phone_number}\n")
    print("Контакт успешно добавлен.")

def display_contacts():
    with open("phonebook.txt", "r") as file:
        for line in file:
            print(line.strip())

def search_contact():
    search_term = input("Введите имя или фамилию для поиска: ")
    found = False
    with open("phonebook.txt", "r") as file:
        for line in file:
            if search_term.lower() in line.lower():
                print(line.strip())
                found = True
    if not found:
        print("Контакт не найден.")

def export_contacts():
    with open("phonebook.txt", "r") as file:
        data = file.read()
    with open("exported_phonebook.txt", "w") as file:
        file.write(data)
    print("Контакты успешно экспортированы в файл exported_phonebook.txt")

def copy_line():
    try:
        line_number = int(input("Введите номер строки для копирования: "))
        with open("phonebook.txt", "r") as file:
            lines = file.readlines()
            try:
                copied_line = lines[line_number - 1]
                with open("copied_line.txt", "a") as new_file:
                    new_file.write(copied_line)
                print("Строка успешно скопирована.")
            except IndexError:
                print("Неверный номер строки.")
    except ValueError:
        print("Введите число.")
        
def main():
    while True:
        print("\nМеню:")
        print("1. Добавить контакт")
        print("2. Показать все контакты")
        print("3. Поиск контакта")
        print("4. Экспорт контактов")
        print("5. Скопировать строку в другой файл")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            display_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            export_contacts()
        elif choice == "5":
            copy_line()
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
