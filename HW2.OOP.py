# 1. Create a class hierarchy of animals with at least 5 animals that have additional methods each, 
# create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class
# 
# class Animals:
#     """
#     Parent class, should have eat, sleep
#     """
# 
# class Animal1(Animal):
#     """
#     Some of the animal with 1-2 extra methods related to this animal
#     """
#     
#  ...
class Animals:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} like eating tasty food')

    def sleep(self):
        print(f'{self.name} like sleeping')


class Dog(Animals):
    def dog_skill(self):
        print(f'{self.name} can bark')


class Cat(Animals):
    def cat_skill(self):
        print(f'{self.name} can purr')


class Frog(Animals):
    def frog_skill(self):
        print(f'{self.name} can jump')


class Bird(Animals):
    def bird_skill(self):
        print(f'{self.name} can fly')


class Cheetah(Animals):
    def cheetah_skill(self):
        print(f'{self.name} can run')


dog = Dog('Rex')
cat = Cat('Tom')
frog = Frog('Pix')
bird = Bird('Maya')
cheetah = Cheetah('Faster')

for pet in (dog, cat, frog, bird, cheetah):
    print(f'{pet.name} is one of the Animals : issistance (pet, Animals)')


# 1.a. Create a new class Human and use multiple inheritance to create Centaur class,
#  create an instance of Centaur class and call the common method of these classes and unique.
#  
#  class Human:
#     """
#     Human class, should have eat, sleep, study, work
#     """
#  
#  class Centaur(.. , ..):
#     """
#     Centaur class should be inherited from Human and Animal and has unique method related to it.
#     """


class Human:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'The {self.name} eat tasty food.')

    def sleep(self):
        print(f'The {self.name} sleep a little.')

    def study(self):
        print(f'The {self.name} study a lot.')

    def work(self):
        print(f'The {self.name} work a lot.')


class Centaur(Human, Animals):
    def gallop(self):
        print(f'The {self.name} can gallop.')


centaur = Centaur('Centaur')
print()
centaur.sleep()
centaur.work()
centaur.gallop()


# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
# a.

class Person:
    def __init__(self, name):
        self.name = name
        left = Arm('Left')
        right = Arm('Right')
        self.arms = [left, right]


class Arm:
    def __init__(self, arm):
        self.arm = arm


person1 = Person('Helen')

for ar in person1.arms:
    print(person1.name + ' ' + "has" ' ' + ar.arm + ' ' + "hand!")


# aggregation
class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self, screen_size):
        self.screen_size = screen_size


our_screen = Screen('5.5"')
our_phone = CellPhone(our_screen)
#print(our_screen.screen_size)
print(our_phone.screen.screen_size)

# 3.
# class Profile:
#    """
#      Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
#       Override a printable string representation of Profile class and return: list of the params mentioned above
#        """
class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.params = [name, last_name, phone_number, address, email, birthday, age, sex]

    def __str__(self):
        return str(self.params)


profile = Profile('John', 'Bing', '+12345678', 'LA', 'jb@com', '2000', '21', 'male')
print(profile)

# 4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
#     and create an HPLaptop class by using your interface.
from abc import abstractmethod, ABC


class Laptop(ABC):
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class Apple(Laptop):
    def __init__(self, model, screen, keyboard, touchpad, webcam, ports, dynamics):
        self.model = model
        self.screen = screen
        self.keyboard = keyboard
        self.touchpad = touchpad
        self.webcam = webcam
        self.ports = ports
        self.dynamics = dynamics

        def screen(self):
            print(f'The screen of {self.model} laptop is {self.screen}')

        def keyboard(self):
            print(f'The keyboard of {self.model} laptop is {self.keyboard}')

        def touchpad(self):
            print(f'The touchpad of {self.model} laptop is {self.touchpad}')

        def webcam(self):
            print(f'The webcam of {self.model} laptop is {self.webcam}')

        def ports(self):
            print(f'The ports of {self.model} laptop is {self.ports}')

        def dynamics(self):
            print(f'The dynamics of {self.model} laptop is {self.dynamics}')


laptop = Apple('Apple MacBook Air M1 2020', 'Retina 13.3', 'Magic keyboard', 'Track Force Touch','HD-camera Face Time 720p', 'USB Type-C 3.1', 'SRS Premium Sound')
laptop.screen()
laptop.keyboard()
laptop.touchpad()
laptop.webcam()
laptop.ports()
laptop.dynamics()
print(laptop)
