from abc import ABC, abstractmethod
from Product import Product
import json


class BaseSerializer(ABC):
    """Базовый класс для сериализаторов."""

    @abstractmethod
    def serialize_object(self, obj):
        """Функция для сериализации объекта."""

        pass

    @abstractmethod
    def serialize_list(self, objs):
        """Функция для сериализации списка."""

        pass


class BaseDeserializer(ABC):
    """Базовый класс для десериализаторов."""

    @abstractmethod
    def deserialize_object(self):
        """Функция для десериализации объектов."""

        pass


class FileInfo:
    """Класс для хранения информации о файле."""

    def __init__(self, filename) -> None:
        """Инициализация файла.

        Args:
            filename: Имя файла.
        """

        self.filename = filename

    def set_filename(self, filename) -> None:
        """Сеттер для имени файла.

        Args:
            filename: Имя файла.
        """

        self.filename = filename

    def get_filename(self) -> str:
        """Геттер для имени файла.

        Returns:
            filename: Имя файла.
        """

        return self.filename
class TxtParser(FileInfo, BaseDeserializer):
    """Парсер для текстовых файлов."""

    def __init__(self, filename) -> None:
        """Инициализация парсера.

        Args:
            filename: Имя файла.
        """

        super().__init__(filename)

    def deserialize_object(self) -> list[Product]:
        """Функция для десериализации объектов из текстового файла.

        Returns:
            list[Product]: Список товаров.
        """

        products = []
        try:
            with open(f'{self.filename}.txt', 'r', encoding='utf-8') as txt_file:
                lines = txt_file.readlines()

                if lines:
                    headers = [h.strip() for h in lines[0].strip().split(';')]

                    for line_num, line in enumerate(lines[1:], 2):
                        values = line.strip().split(';')

                        if len(values) != len(headers):
                            print(f"Предупреждение: Строка {line_num-1} пропущена - несоответствие количества характеристик")
                            continue

                        product = Product()
                        product.set_from_str(line.strip())
                        products.append(product)

                    return products

                else:
                    raise EOFError('Ошибка, пустой файл!')

        except Exception as e:
            print(e)


class JSONParser(FileInfo,BaseSerializer ,BaseDeserializer):
    """Парсер для JSON файлов."""

    def __init__(self, filename) -> None:
        """Инициализация парсера.

        Args:
            filename: Имя файла.
        """

        super().__init__(filename)

    def serialize_list(self, products:list[Product]) -> None:
        """Функция для сериализации списка товаров в JSON файл.

        Args:
            products: Список товаров.
        """

        try:
            some_data = dict()

            for prod in products:
                some_data[prod.get_id()] = prod.to_dict()

            with open(f'{self.filename}.json', 'w', encoding='utf-8') as file:
                json.dump(some_data, file, ensure_ascii=False, indent=4)

        except Exception as e:
            print(e)

    def deserialize_object(self, ids:list[str]=None) -> list[Product]:
        """Функция для сериализации списка товаров в JSON файл.

        Args:
            ids: Список ID для загрузки конкретных товаров.
        Returns:
            products: Список товаров.
        """

        products = []
        try:
            with open(f'{self.filename}.json', 'r', encoding='utf-8') as file:
                data_dict=json.load(file)

            if ids:
                for current_id in ids:
                    product = Product()
                    product.set_from_dict(data_dict[current_id])
                    products.append(product)
            else:
                for data in data_dict.values():
                    product = Product()
                    product.set_from_dict(data)
                    products.append(product)

            print(f"Прочитано товаров из JSON: {len(products)}")

            return products

        except Exception as e:
            print(e)

    def serialize_object(self, product:Product) -> None:
        """Функция для сериализации объекта в JSON файл.

        Args:
            product: Товар для сериализации.
        """

        data_list=self.deserialize_object()
        new_data_list=list()

        if product not in data_list:
            data_list.append(product)
        else:
            for item in data_list:
                if item.get_id()==product.get_id():
                    new_data_list.append(product)
                else:
                    new_data_list.append(item)

        self.serialize_list(new_data_list)
