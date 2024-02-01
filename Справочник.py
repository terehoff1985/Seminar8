import csv

def add_contact():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")

    contact = [surname, name, patronymic, phone_number]

    with open("contacts.txt", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(contact)

    print("Контакт успешно добавлен!")


def search_contacts():
    search_term = input("Введите характеристику для поиска: ")
    found_contacts = []

    with open("contacts.txt", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if any(search_term.lower() in field.lower() for field in row):
                found_contacts.append(row)

    if found_contacts:
        print("Найдены следующие контакты:")
        for contact in found_contacts:
            print(",".join(contact))
    else:
        print("Контакты не найдены.")


def copy_line(source_file, destination_file, line_number):
    with open(source_file, 'r') as source:
        lines = source.readlines()

        if line_number <= len(lines):
            line_to_copy = lines[line_number - 1]

            with open(destination_file, 'a') as destination:
                destination.write(line_to_copy)
                print(f"Строка {line_number} успешно скопирована из {source_file} в {destination_file}.")
        else:
            print(f"Ошибка: файл {source_file} содержит меньше строк, чем указано.")


def main():
    while True:
        print("Меню:")
        print("1. Добавить контакт")
        print("2. Поиск контактов")
        print("3. Копировать строку из одного файла в другой")
        print("4. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contacts()
        elif choice == "3":
            source_file = input("Введите имя исходного файла: ")
            destination_file = input("Введите имя файла назначения: ")
            line_number = int(input("Введите номер строки для копирования: "))
            copy_line(source_file, destination_file, line_number)
        elif choice == "4":
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()