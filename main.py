from hw5.Animal import Animal
from hw5.AnimalFactory import AnimalFactory
from hw5.Bird import Bird
from hw5.Cat import Cat
from hw5.Dog import Dog
from hw5.Mammal import Mammal
from hw5.Parrot import Parrot
from hw5.Reptiles import Reptiles
from hw5.Shop import Shop
from hw5.Snake import Snake
from hw5.Turtle import Turtle

snake1 = AnimalFactory.create('Snake','snake1',10,1)
dog1 = AnimalFactory.create('Dog','dog1',5,10)
cat1 = AnimalFactory.create('Cat','cat1',5,10)
# parrot1 = AnimalFactory.create('Parrot','parrot1',30,10)
# turtle1 = AnimalFactory.create('Turtle','turtle1',30,10)
my_shop = Shop('myshop',40)
print(my_shop.get__animals())
list_of_animals = [snake1,dog1,cat1]
my_shop + list_of_animals
print(my_shop.get__animals())
# num = my_shop + snake1
# print('\n')
# print(num)
# print(my_shop.get__animals())
# print('turtle1 power = ' + str(turtle1._get__power()))
# print('snake1 power = ' + str(snake1._get__power()))
# print(my_shop.play('snake1','turtle1'))
# print('turtle1 power = ' + str(turtle1._get__power()))
# print('snake1 power = ' + str(snake1._get__power()))