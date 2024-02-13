import re
from typing import Dict, List

from db.directory_db import DirectoryDB
from db.formatter import FormatterData


class DirectoryService:
    def __init__(self):
        """
        Создаем экземпляр класса устройства усправления текстовой БД
        """
        self.db = DirectoryDB()

    def add_record(self, record_data: Dict[str, str]) -> int:
        """
        Форматирует данные из словаря в строку и добавляет в текстовую БД

        :param record_data: Данные о записи, собранные в словаре, в виде пар ключ-значение
        :return: Кол-во строк в БД
        """
        formatted_record: str = FormatterData.convert_to(data=record_data)
        response: int = self.db.insert(data=formatted_record)
        return response

    def get_record(self, record_id: str) -> Dict[str, str]:
        """
        Извлечение записи, по указанному id, и форматирует данные из строки в словарь

        :param record_id: ID записи для получения записи из текстовой БД
        :return: Словарь с данными пользователя
        """
        record: str = self.db.get(record_id=record_id)
        formatted_record: dict = FormatterData.convert_from(data=record)
        return formatted_record

    def get_records(self, cur: int, how_m: int) -> List[Dict[str, str]]:
        """
        Получение записей в определенном диапазоне

        :param cur: Номер записи, от которой надо вывести
        :param how_m: Номер записи, до которой надо вывести
        :return: Список с определнным срезом
        """
        records: list = self.db.get_all()
        formatted_records: list = [FormatterData.convert_from(data=record) for record in records]
        result = formatted_records[cur - 1:(how_m + cur) - 1]
        return result

    def find_record_with_param(self, name: str = "",
                               last_name: str = "",
                               surname: str = "",
                               org_name: str = "",
                               work_phone: str = "",
                               personal_phone: str = "") -> List[Dict[str, str]]:
        """
        Функция поиска с помощью регулярного выражения по одному или нескольким параметрам

        :return: Список результатов
        """

        records: list = self.db.get_all()
        separate_lines = [FormatterData.separate_line(line=record) for record in records]

        pattern = re.compile(rf'^.*\b{name}\b.*\b{last_name}\b.*\b{surname}\b.*\b{org_name}\b.*\b{work_phone}\b.*\b{personal_phone}\b.*$')

        search_list: list = []

        for sublist in separate_lines:
            if pattern.search(' '.join(sublist)):
                prepare_str: str = ",".join(sublist)
                formatted_data: dict = FormatterData.convert_from(prepare_str)
                search_list.append(formatted_data)

        return search_list

    def show_table_records(self, records: List[Dict[str, str]]):
        """
        Выводит в виде таблицы, переданные записи
        :param records: Список записей в виде словаря
        """
        for record in records:
            print("-" * 100)
            print(record.get("p_id"), record.get("first_name"), record.get("last_name"), record.get("surname"),
                  record.get("org_name"), record.get("work_phone"), record.get("personal_phone"),
                  sep="{:^10}".format("|"))

    def edit_record(self, record_id: str, record_data: dict) -> int:
        """
        Изменение одного или нескольких параметров записи, определенной по ID

        :param record_id: ID записи
        :param record_data: Данные для замены
        :return: Кол-во строк в БД
        """
        new_record: str = FormatterData.convert_to(data=record_data)
        response: int = self.db.update(record_id=record_id, data=new_record)
        return response

    def delete(self, record_id: str) -> int:
        """
        Удаление записи по ее ID

        :param record_id: ID записи
        :return: Кол-во строк в БД
        """
        response: int = self.db.delete(record_id=record_id)
        return response


# print(DirectoryService().add_record({"p_id": 65342, "first_name": "John", "last_name": "toh", "surname": "Malkovich", "org_name": "lol", "work_phone": "898459834", "personal_phone": "483975987"}))
# print(DirectoryService().get_record("903"))
# print(DirectoryService().get_records(2, 5,))
# print(DirectoryService().edit_reco    rd(record_id="90342", record_data={"p_id": "90342", "first_name": "Mi", "last_name": "LI", "surname": "Malkovich", "org_name": "lol", "work_phone": "898459834", "personal_phone": "483975987"}))
# print(DirectoryService().delete("43342"))
# print(DirectoryService().find_record_with_param(name="Li", last_name="LI"))