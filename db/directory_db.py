from typing import List

from db.base import Base
from db.formatter import FormatterData


class DirectoryDB(Base):
    __insert_mode = 'a'
    __get_mode = 'r'
    __update_mode = 'w'

    def insert(self, data: str) -> int:
        """
        Функция устройства работы с БД для работы добавления записи в текстовуюю БД

        :param data: Данные, которые надо добавить в текстовую БД
        :return: Код ответа: 0 - все хорошо, 1 - ошибка
        """
        try:
            all_records = self.get_all()
            self.connect_to_db(mode=self.__insert_mode)

            cursor = self.get_connection()

            if data in all_records:
                return 1
            else:
                cursor.write(data)

            return 0
        except Exception as e:
            print("Ошибка при записи файла: ", e)
            return 1
        finally:
            self.close_db()

    def get(self, record_id: str) -> str:
        """
        Функция устройства работы с БД для получения данных из текстовой БД

        :param record_id: ID записи, которую надо получить из БД
        :return: Запись из БД в виде неформатированной строки
        """
        try:
            self.connect_to_db(mode=self.__get_mode)

            cursor = self.get_connection()
            result = cursor.readlines()
            found_record = ""

            for line in result:
                line_record_id = FormatterData.get_id_from_str(line)
                if record_id == line_record_id:
                    found_record = line
                    break

            return found_record
        except Exception as e:
            print("Ошибка при чтении файлов: ", e)
        finally:
            self.close_db()

    def get_all(self) -> List[str]:
        """
        Функция устройства работы с БД для получения всех записей из текстовой БД

        :return: Список неформатированных записей из БД
        """
        try:
            self.connect_to_db(mode=self.__get_mode)

            cursor = self.get_connection()
            result = cursor.readlines()

            return result
        except Exception as e:
            print("Ошибка при чтении файлов: ", e)
        finally:
            self.close_db()

    def update(self, record_id: str, data: str) -> int:
        """
        Функция устройства работы с БД для обновления записи в текстовой БД по ID и новым данным записи

        :param record_id: ID записи, которую надо обновить
        :param data: Данные, на которые надо заменить старые данные
        :return: Код ответа: 0 - все хорошо, 1 - ошибка
        """
        try:
            all_lines = self.get_all()

            self.connect_to_db(mode=self.__update_mode)
            file = self.get_connection()

            for line in all_lines:
                new_line = FormatterData.get_id_from_str(line)
                if record_id == new_line:
                    file.write(data)
                else:
                    file.write(line)

            return 0
        except Exception as e:
            print("Ошибка при обновлении файла: ", e)
            return 1
        finally:
            self.close_db()

    def delete(self, record_id: str) -> int:
        """
        Функция устройства работы с БД для удаления записи из текстовой БД

        :param record_id: ID записи, которую надо удалить из БД
        :return: Код ответа: 0 - все хорошо, 1 - ошибка
        """
        try:
            all_lines = self.get_all()

            self.connect_to_db(mode=self.__update_mode)
            file = self.get_connection()

            for line in all_lines:
                new_line = FormatterData.get_id_from_str(line)
                if record_id != new_line:
                    file.write(line)

            return 0
        except Exception as e:
            print("Ошибка при перезаписи файла: ", e)
            return 1
        finally:
            self.close_db()


# a = DirectoryDB()
# a.insert(data={"p_id": 53443, "name": "John", "last_name": "Smith", "surname": "Malkovich", "org_name": "lol", "work_phone": "898459834", "personal_phone": "483975987"})
# print(a.get("93443"))
# a.delete("93443")
# print(FormatterData.convert_from("*12323,None,Smith,Malkovich,lol,898459834,483975987#"))