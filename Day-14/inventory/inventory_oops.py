from abc import ABC, abstractmethod
import json
from datetime import datetime

def log_action(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("log.txt", "a") as f:
            f.write(f"{datetime.now()} - {func.__name__} executed\n")
        return result
    return wrapper


class Product(ABC):
    def __init__(self, category):
        self._category = category
        self.__products = {}
        self.load()

    def get_products(self):
        return self.__products

    def set_product(self, name, data):
        self.__products[name] = data

    def delete_product(self, name):
        self.__products.pop(name, None)

    def load(self):
        try:
            with open("inventory.json", "r") as f:
                data = json.load(f)
                self.__products = data.get(self._category, {})
        except FileNotFoundError:
            self.__products = {}

    def save(self):
        try:
            with open("inventory.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        data[self._category] = self.__products
        with open("inventory.json", "w") as f:
            json.dump(data, f, indent=4)

    @abstractmethod
    def add_product(self, name, price, stock):
        pass

    @abstractmethod
    def update_stock(self, name, stock):
        pass

    @abstractmethod
    def remove_product(self, name):
        pass


class Electronics(Product):
    def __init__(self):
        super().__init__("electronics")

    @log_action
    def add_product(self, name, price, stock):
        self.set_product(name, {"price": price, "stock": stock})
        self.save()

    @log_action
    def update_stock(self, name, stock):
        if name in self.get_products():
            self.get_products()[name]["stock"] = stock
            self.save()

    @log_action
    def remove_product(self, name):
        self.delete_product(name)
        self.save()


class Grocery(Product):
    def __init__(self):
        super().__init__("grocery")

    @log_action
    def add_product(self, name, price, stock):
        self.set_product(name, {"price": price, "stock": stock})
        self.save()

    @log_action
    def update_stock(self, name, stock):
        if name in self.get_products():
            self.get_products()[name]["stock"] = stock
            self.save()

    @log_action
    def remove_product(self, name):
        self.delete_product(name)
        self.save()
