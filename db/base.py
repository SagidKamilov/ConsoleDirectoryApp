from typing import Any
file_name = "g_d.txt"


class Base:
    def __init__(self):
        self.db = None
        self.file_name = file_name

    def connect_to_db(self, mode: str) -> Any:
        """
        Подключение к файловой базе данных, с переданным режимом

        :param mode: режим подключения к базе данных
        :return: None
        """
        try:
            self.db = open(file=file_name, mode=mode, encoding="UTF-8")
        except FileNotFoundError:
            print(f"Справочник с именем \"{file_name}\" не существует")

    def get_connection(self):
        """
        Передача ссылки на экземпляр открытого файла

        :return: Экземпляр отркытого файла
        """
        return self.db

    def close_db(self):
        """
        Закрытие подключения к файловой базе данных

        :return: None
        """
        self.db.close()
