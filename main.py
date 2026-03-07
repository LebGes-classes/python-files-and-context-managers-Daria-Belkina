import os
from Parser import *
from Actions import Actions


class Menu:
    @staticmethod
    def print_menu():
        """Вывод пунктов главного пользовательского меню."""

        print('--------- МЕНЮ ---------\n',
              '0. ВЫЙТИ\n',
              '1. Работа с файлом data\n')

    def main_menu(self, choise: int) -> bool:
        """Главное пользовательское меню, которое обратабатывает выбор пользователя.

        Args:
            choise: Выбор пользователя.
        Returns:
            is_running: Продолжается ли работа программы.
        """

        is_running = True

        match choise:
            case 0:
                is_running = False
            case 1:
                json_parser = JSONParser('catalog_new')

                if os.path.exists('catalog_new.json'):
                    products = json_parser.deserialize_object()
                else:
                    txt_parser = TxtParser('data_1')
                    products = txt_parser.deserialize_object()
                    json_parser.serialize_list(products)

                element = Actions('catalog_new')
                print('Выберите пункт:\n',
                      '0. ВЫЙТИ\n',
                      '1. Изменить карточку товара\n',
                      '2. Добавить карточку товара\n',
                      '3. Удалить карточку товара\n')
                choise_number_1 = int(input('Введите пункт меню >>> '))
                match choise_number_1:
                    case 0:
                        is_running = False
                    case 1:
                        product_numb_id=input('Введите номер id карточки, которую хотите изменить: ')
                        key=input('Введите какой параметр хотите изменить: ')
                        new_value=input('Введите новое значение параметра: ')
                        element.changing_card(product_numb_id, key, new_value)
                    case 2:
                        new_added_product = {}

                        for i in range(9):
                            key = input("Введите новый параметр карточки: ")
                            value = input("Введите новое значение параметра: ")
                            new_added_product[key] = value
                            print(f'Параметр {key} с заначением {value} записан!')

                        element.add_card(new_added_product)
                    case 3:
                        product_numb_id=input('Введите номер карточки, которую хотите удалить: ')
                        element.delete_card(product_numb_id)
                    case _:
                        print("Неверный выбор. Такго пункта не существует. Попробуйте еще раз.")

            case _:
                print("Неверный выбор. Такго пункта не существует. Попробуйте еще раз.")

        return is_running


class Main:
    """Основной класс для запуска работы."""

    def run(self) -> None:
        """Метод запуска работы."""

        is_running = True

        menu = Menu()

        while is_running:
            menu.print_menu()

            choise = int(input('Введите пункт меню >>> '))

            is_running = menu.main_menu(choise)

if __name__ == "__main__":
    card = Main()
    card.run()
