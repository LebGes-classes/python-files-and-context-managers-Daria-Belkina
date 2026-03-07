from Parser import *
from Product import Product


class Actions:
    """Класс для выполнения действий с товарами."""

    def __init__(self, file):
        """Инициализация файла.

        Args:
            file: Имя файла.
        """

        self.file = file

    def changing_card(self, product_numb_id, key, new_value):
        """Функция для изменение карточки товара.

        Args:
            product_numb_id: Номер id товара.
            key: Ключ-параметр для изменения.
            new_value: Новое значение.
        """

        example = JSONParser(self.file)
        products = example.deserialize_object()

        try:
            for i, product in enumerate(products):
                if str(product.get_id()) == str(product_numb_id):
                    product_dict = product.to_dict()

                    if key == 'count':
                        new_value = int(new_value)
                    elif key == 'price':
                        new_value = float(new_value)

                    product_dict[key] = new_value

                    updated_product = Product()
                    updated_product.set_from_dict(product_dict)

                    products[i] = updated_product

                    example.serialize_list(products)
                    print('Изменения сохранены в файл!')

        except Exception as e:
            print(e)

    def delete_card(self, product_numb_id):
        """Функция для удаление карточки товара.

        Args:
            product_numb_id: Номер id товара для удаления.
        """

        example_2 = JSONParser(self.file)
        products = example_2.deserialize_object()

        try:
            for product in products:
                if str(product.get_id()) == str(product_numb_id):
                    products.remove(product)
                    example_2.serialize_list(products)
                    print('Изменения сохранены в файл!')

        except Exception as e:
            print(e)

    def add_card(self, new_added_product:dict):
        """Добавление новой карточки товара.

        Args:
            new_added_product: Данные нового товара.
        """

        example_3 = JSONParser(self.file)
        products = example_3.deserialize_object()

        new_product = Product()
        new_product.set_from_dict(new_added_product)

        products.append(new_product)
        example_3.serialize_list(products)

        print('Изменения сохранены в файл!')
