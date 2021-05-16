# There is a Person whose characteristics are:
# 1. Name
# 2. Age
# 3. Availability of money
# 4. Having your own home
#
# Human can:
# 1. Provide information about yourself
# 2. Make money
# 3. Buy a house
#
# There is also a House, the properties of which include:
# 1. Area
# 2. Cost
#
# For Home you can:
# 1. Apply a purchase discount
#
# e.g.: There is also a Small Typical House with a required area of 40m2.
#
# *Realtor:
# 1. Name
# 2. Houses
# 3. Discount that he/she can give you.
#
# *There is only one realtor who handles small houses you wanna buy. (Singleton)
# Realtor is only one in your city and can:
# 1. Provide information about all the Houses
# 2. Give a discount
# 3. Steal your money with 10% chance


from abc import ABC, abstractmethod
import random


class Human(ABC):
    @abstractmethod
    def provide_info_person(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self, house):
        raise NotImplementedError


class Person(Human):
    def __init__(self, name, age, availability_of_money, salary, having_your_own_home: list):
        self.name = name
        self.age = age
        self.availability_of_money = availability_of_money
        self.salary = salary
        self.having_your_own_home = having_your_own_home

    def provide_info_person(self):
        print(f' I am {self.name} and I am {self.age} years old'
              f'I have {self.availability_of_money}'
              f'My salary is {self.salary}')

    def make_money(self):
        print(f'Current sum of money is {self.availability_of_money}')
        self.availability_of_money += self.salary
        print(f'After receiving a salary current sum of money is {self.availability_of_money}')

    def buy_house(self, house):
        if self.availability_of_money < house.cost:
            print("You don't have enough money to buy this house.")
        else:
            self.availability_of_money -= house.cost
            self.having_your_own_home.append(house)
            print("You have bought a house.")


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost


class SmallTypicalHouse(House):
    def __init__(self, cost, area=40):
        super().__init__(area, cost)


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class OurRealtor(metaclass=RealtorMeta):
    def __init__(self, name, age, houses: list):
        self.name = name
        self.age = age
        self.houses = houses

    def provide_info(self):
        print(f'I am {self.name}. I am your realtor.'
              f'You can buy such houses for now as:')
        for home in self.houses:
            print(f'The area of house is {home.area}, it costs {home.cost}')

    def give_discount(self, house):
        print('The realtor would like to propose you a discount')
        if house in self.houses:
            house.cost -= house.cost / 100 * random.randint(1, 50)
        print(f'Now the price of this house is {house.cost}')

    @staticmethod
    def steal(person):
        probability = random.randint(1, 10)
        if probability == 1:
            person.availability_of_money = max(person.availability_of_money - random.randint(100, 10000), 0)
        print(
            f"Be careful next time. The realtor steals your money! Now your balance is {person.availability_of_money}")

if __name__ == "__main__":
    house1 = House(45, 54000)
    house2 = House(83, 88000)
    house3 = House(58, 63000)

    person1 = Person('Liudmula', 35, 40000, 20000, [])
    person1.provide_info_person()
    person1.make_money()

    realtor1 = OurRealtor('Olga', 45, [house1, house2, house3])
    realtor1.provide_info()
    realtor1.give_discount(house3)
    person1.buy_house(house3)
    realtor1.steal(person1)