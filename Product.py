class Product:
    """"Класс карточки товара."""

    def __init__(
            self,
            id:str='None',
            name:str='None',
            count:int=0,
            state:str='None',
            distributor:str='None',
            manufacturer:str='None',
            price: float=0.0,
            location:str='None',
            city:str='None'
    ) -> None:
        """Инициализация карточки.

        Args:
            id: ID карточки.
            name: Наименование карточки.
            count: Количество карточки.
            state: Состояние карточки.
            distributor: Поставщик карточки.
            manufacturer: Производитель карточки.
            price: Стоимость карточки.
            location: Местоположение карточки.
            city: Город карточки.
        """

        self.__id = id
        self.__name = name
        self.__count = count
        self.__state = state
        self.__distributor = distributor
        self.__manufacturer = manufacturer
        self.__price = price
        self.__location = location
        self.__city = city

    def set_id(self, id:str) -> None:
        """Сеттер для ID карточки.

        Args:
            id: ID карточки.
        """

        self.__id = id

    def set_name(self, name:str) -> None:
        """Сеттер для наименования карточки.

        Args:
            name: Наименование карточки.
        """

        self.__name = name

    def set_count(self, count:int) -> None:
        """Сеттер для количества карточки.

        Args:
            count: Количество карточки.
        """

        if isinstance(count, int):
            if count > 0:
                self.__count = count
            else:
                raise ValueError
        else:
            raise TypeError

    def set_state(self, state:str) -> None:
        """Сеттер для состояния карточки.

        Args:
            state: Состояние карточки.
        """

        self.__state = state

    def set_distributor(self, distributor:str) -> None:
        """Сеттер для поставщика карточки.

        Args:
            distributor: Поставщик карточки.
        """

        self.__distributor = distributor

    def set_manufacturer(self, manufacturer:str) -> None:
        """Сеттер для производителя карточки.

        Args:
            manufacturer: Производитель карточки.
        """

        self.__manufacturer = manufacturer

    def set_price(self, price:float) -> None:
        """Сеттер для стоимости карточки.

        Args:
            price: Стоимость карточки.
        """

        if type(price) is float:
            if price >= 0:
                self.__price = price
            else:
                raise ValueError
        else:
            raise TypeError

    def set_location(self, location:str) -> None:
        """Сеттер для местоположения карточки.

        Args:
            location: Местоположение карточки.
        """

        self.__location = location

    def set_city(self, city:str) -> None:
        """Сеттер для города карточки.

        Args:
            city: Город карточки.
        """

        self.__city = city

    def get_id(self) -> str:
        """Геттер для ID карточки.

        Returns:
            id: ID карточки.
        """

        return self.__id

    def get_name(self) -> str:
        """Геттер для наименования карточки.

        Returns:
            name: Наименование карточки.
        """

        return self.__name

    def get_count(self) -> int:
        """Геттер для количества карточки.

        Returns:
            count: Количество карточки.
        """

        return self.__count

    def get_state(self) -> str:
        """Геттер для состояния карточки.

        Returns:
            state: Состояние карточки.
        """

        return self.__state

    def get_distributor(self) -> str:
        """Геттер для поставщика карточки.

        Returns:
            distributor: Поставщик карточки.
        """

        return self.__distributor

    def get_manufacturer(self) -> str:
        """Геттер для производителя карточки.

        Returns:
            manufacturer: Производитель карточки.
        """

        return self.__manufacturer

    def get_price(self) -> float:
        """Геттер для стоимости карточки.

        Returns:
            price: Стоимость карточки.
        """

        return self.__price

    def get_location(self) -> str:
        """Геттер для местоположения карточки.

        Returns:
            location: Местоположение карточки.
        """

        return self.__location

    def get_city(self) -> str:
        """Геттер для города карточки.

        Returns:
            city: Город карточки.
        """

        return self.__city

    def set_from_str(self, line:str) -> None:
        """Функция для получения и установки полей класса из строки.

        Args:
            line: Строка с данными товара.
        """

        elements = line.split(';')

        self.set_id(elements[1])
        self.set_name(elements[2])
        self.set_count(int(elements[3]))
        self.set_state(elements[4])
        self.set_distributor(elements[5])
        self.set_manufacturer(elements[6])
        self.set_price(float(elements[7].split(' ')[0]))
        self.set_location(elements[8])
        self.set_city(elements[9])

    def set_from_dict(self, data:dict) -> None:
        """Функция для получения и установки полей класса из словаря.

        Args:
            data: Словарь с данными товара.
        """

        self.set_id(data['id'])
        self.set_name(data['name'])
        self.set_count(int(data['count']))
        self.set_state(data['state'])
        self.set_distributor(data['distributor'])
        self.set_manufacturer(data['manufacturer'])
        self.set_price(float(data['price']))
        self.set_location(data['location'])
        self.set_city(data['city'])

    def to_dict(self) -> dict:
        """Функция для преобразования товара в словарь.

        Returns:
            dict: Словарь с данными товара.
        """

        return {
            'id': self.get_id(),
            'name': self.get_name(),
            'count': self.get_count(),
            'state': self.get_state(),
            'distributor': self.get_distributor(),
            'manufacturer': self.get_manufacturer(),
            'price': float(self.get_price()),
            'location': self.get_location(),
            'city': self.get_city(),
        }