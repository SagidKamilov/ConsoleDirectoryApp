import random

from service.directory import DirectoryService


class ConsoleApp:
    words = ["Имя", "Фамилия", "Отчество", "Наименование организации", "Домашний телефон", "Рабочий телефон"]

    def __init__(self):
        self.service = DirectoryService()

    def create_information_about_human(self):
        """
        Реализация создания пользователя по данным, введенными пользователем.
        Создается словарь и передается в функцию сервиса, которая возвращает целочисленный ответ 0 или 1.
        0 - все прошло успешно, 1 - возникли ошибки
        """
        print("\n{:#^50}".format(" Создание карты пользователя "))

        p_id = str(random.randint(1, 100000))
        name = input("Введите имя человека: ")
        last_name = input("Введите фамилию человека: ")
        surname = input("Введите отчество человека: ")
        org_name = input("Введите имя организации: ")
        work_phone = input("Введите рабочий номер телефона: ")
        personal_phone = input("Введите персональный номер телефона: ")

        new_human_card = {"p_id": p_id,
                         "first_name": name,
                         "last_name": last_name,
                         "surname": surname,
                         "org_name": org_name,
                         "work_phone": work_phone,
                         "personal_phone": personal_phone}

        response_code = self.service.add_record(record_data=new_human_card)
        if response_code == 0:
            print("\n{:#^30}".format("#"), "{:#^30}".format(" Запись создана! Возвращаю в главное меню. "), "{:#^30}".format("#"))
        else:
            print("\n{:#^30}".format("#"), "{:#^30}".format(" При создании записи произошла ошибка. Возвращаю в главное меню.  "), "{:#^30}".format("#"))
        self.run()

    def get_information_about_human(self, record_id: str, cur: int):
        """
        Получения информации о пользователе с возможностью перемещения назад в список.
        Данные получают по id записи из сервиса и выводятся в терминал.
        Пользователю предлагается выбор действий над записью.
        :param record_id: ID записи
        :param cur: Номер записи начала страницы, с которой был осуществлен переход
        """
        record: dict = self.service.get_record(record_id=str(record_id))

        if record == "":
            print("\n{:#^30}".format("#"), "{:#^30}".format(" Запись не найдена! "), "{:#^30}".format("#"))
        else:
            print("\n{:#^50}".format(" Информация о пользователе "), " ID: " + record.get("p_id"), "Имя: " + record.get("first_name"),
                  "Фамилия: " + record.get("last_name"), "Отчество: " + record.get("surname"), "Наименование организации: " + record.get("org_name"),
                  "Рабочий номер телефона: " + record.get("work_phone"), "Личный номер телефона: " + record.get("personal_phone"), "{:#^50}".format(""), sep="\n")

        print("\nВернуться назад - 1", "Обновить информацию о человеке - 2", "Удалить информацию о человеке - 3", sep="\n")

        answer = int(input("\nВведите цифру:"))
        if answer == 1:
            self.get_page_by_page(from_rec=cur)
        elif answer == 2:
            self.edit_information_about_human(record_id=record_id)
        elif answer == 3:
            self.delete_information_about_human(record_id=record_id)

    def edit_information_about_human(self, record_id: str):
        """
        Метод для редактирования записи пользователя.
        Запись достается из текстовой БД с помощью сервиса по ID и редактируется
        через цикл, изменяя пункты, где было указанно новое значение.
        :param record_id: ID записи
        """
        old_record = self.service.get_record(record_id=record_id)

        print("\n{:#^50}".format(" Редактирование карты пользователя "))
        for i in old_record.keys():
            print("Хотите изменить?\n", i, "=", old_record.get(i), "\nЕсли да, тогда введите новое значение, если нет, введите пустую строку...")
            new_val = input("\nВведите значение: ")
            if new_val == "":
                continue
            else:
                old_record[i] = new_val


        # answer = int(input("\nВведите цифру: "))
        # if answer == 1:
        #     name = input("Введите новое имя: ")
        #     if name == "":
        #         print("\nВы ввели пустую строку. Отмена изменений. ")
        #         self.get_page_by_page()
        #     else:
        #         old_record["first_name"] = name
        # elif answer == 2:
        #     last_name = input("Введите новую фамилию: ")
        #     if last_name == "":
        #         print("\nВы ввели пустую строку. Отмена изменений. ")
        #         self.get_page_by_page()
        #     else:
        #         old_record["last_name"] = last_name
        # elif answer == 3:
        #     surname = input("Введите новое отчество: ")
        #     if surname == "":
        #         print("\nВы ввели пустую строку. Отмена изменений. ")
        #         self.get_page_by_page()
        #     else:
        #         old_record["surname"] = surname
        # elif answer == 4:
        #     org_name = input("Введите новое наименование организации: ")
        #     if org_name == "":
        #         print("\nВы ввели пустую строку. Отмена изменений. ")
        #         self.get_page_by_page()
        #     else:
        #         old_record["org_name"] = org_name
        # elif answer == 5:
        #     work_phone = input("Введите новый рабочий телефон: ")
        #     if work_phone == "":
        #         print("\nВы ввели пустую строку. Отмена изменений. ")
        #         self.get_page_by_page()
        #     else:
        #         old_re cord["work_phone"] = work_phone
        # elif answer == 6:
        #     personal_phone = input("Введите новый домашний телефон: ")
        #     if personal_phone == "":
        #         print("\nВы ввели пустую строку. Отмена изменений. ")
        #         self.get_page_by_page()
        #     else:
        #         old_record["personal_phone"] = personal_phone

        response_code = self.service.edit_record(record_id=record_id, record_data=old_record)

        if response_code == 0:
            print("\n{:#^30}".format("#"), "{:#^30}".format(" Запись изменена! Возвращаю в главное меню. "),
                  "{:#^30}".format("#"))
        else:
            print("\n{:#^30}".format("#"),
                  "{:#^30}".format(" При изменении записи произошла ошибка. Возвращаю в главное меню.  "),
                  "{:#^30}".format("#"))
        self.run()

    def delete_information_about_human(self, record_id: str):
        """
        Метод для удаления записи по указанному ID
        :param record_id: ID записи
        """
        response_code: int = self.service.delete(record_id=record_id)
        if response_code == 0:
            print("\n{:#^30}".format("#"), "{:#^30}".format(" Запись удалена! Возвращаю на главное меню... "),
                  "{:#^30}".format("#"))
        else:
            print("\nПри удалении произошла ошибка. Возвращаю в главное меню.")
        self.run()

    def find_information(self):
        print("\n{:#^50}".format(" Поиск записи "))
        print("Введите значение, которое хотите заменить или нажмите Enter, чтобы пропустить.")

        answers = []

        for word in self.words:
            answer = input(f"Введите {word}: ")
            answers.append(answer)

        matches_found = self.service.find_record_with_param(*answers)
        self.service.show_table_records(records=matches_found)

        self.run()

    def get_page_by_page(self, from_rec=1, to_rec=5):
        """
        Постраницчное получение списка записей в диапазоне.
        Переход к другим страницам за счет рекурсивного вызова функции со стартовой записью
        через расстояние пагинатора.
        :param from_rec: Номер записи в начале страницы
        :param to_rec: Номер записи в конце страницы
        """
        cur = from_rec
        how_m = to_rec
        paginator_count = 5

        records = self.service.get_records(cur=cur, how_m=how_m)
        print("ID", "Имя", "Фамилия", "Отчество", "Наименование организации", "Рабочий телефон", "Домашний телефон",
              sep="{:^10}".format("|"))

        self.service.show_table_records(records=records)

        print("\nВернуться на главную - 1", "Следующая страница - 2", "Предыдущая страница - 3",
              "Перейти к записи - ID (номер записи)", sep="\n")

        answer = int(input("\nВведите цифру или ID: "))
        if answer == 1:
            self.run()
        elif answer == 2:
            cur += paginator_count
            self.get_page_by_page(from_rec=cur)
        elif answer == 3:
            cur -= paginator_count
            self.get_page_by_page(from_rec=cur)
        elif answer:
            record_id = str(answer)
            self.get_information_about_human(record_id=record_id, cur=cur)

    def run(self):
        """
        Запуск консольного приложения.
        """
        print("\nПосмотреть записи в справочнике - 1", "Поиск записи/записей в справочнике по ключу - 2",
              "Добавить запись в справочник - 3", sep='\n')

        answer = int(input("\nВведите цифру: "))
        if answer == 1:
            self.get_page_by_page()
        elif answer == 2:
            self.find_information()
        elif answer == 3:
            self.create_information_about_human()


if __name__ == "__main__":
    print("{:#^80}".format(""), "{:#^80}".format(" Добро пожаловать в справочник! ".upper()),
          "{:#^80}".format(""), sep='\n')
    app = ConsoleApp()
    app.run()

    # print(DirectoryService().add_record(
    #     {"p_id": 65542, "first_name": "John", "last_name": "toh", "surname": "Malkovich", "org_name": "lol",
    #      "work_phone": "898459834", "personal_phone": "483975987"}))


