from typing import Dict, List


class FormatterData:
    @staticmethod
    def convert_to(data: Dict[str, str]) -> str:

        personal_id = data.get("p_id")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        surname = data.get("surname")
        org_name = data.get("org_name")
        work_phone = data.get("work_phone")
        personal_phone = data.get("personal_phone")

        formatted_data = f"{personal_id},{first_name},{last_name},{surname},{org_name},{work_phone},{personal_phone}\n"

        return formatted_data

    @staticmethod
    def convert_from(data: str) -> Dict[str, str]:

        formatted_data = data.replace("\n", "").split(sep=",")

        un_formatted_data = {"p_id": formatted_data[0],
                            "first_name": formatted_data[1],
                            "last_name": formatted_data[2],
                            "surname": formatted_data[3],
                            "org_name": formatted_data[4],
                            "work_phone": formatted_data[5],
                            "personal_phone": formatted_data[6]}

        return un_formatted_data

    @staticmethod
    def get_id_from_str(line: str) -> int:
        """
        Трансформирует строку в список и получает из нее id записи
        :param line: Строка с разделителем
        :return: id записи
        """

        new_line: list = line.split(",")
        return new_line[0]

    @staticmethod
    def separate_line(line: str) -> List[str]:
        """
        Разделяет строку на компоненты и возвращает список компонентов
        :param line: Строка, которую надо разделить на компоненты
        :return: Список компонентов
        """

        new_line: list = line.replace("\n", "").split(",")
        return new_line
