import unittest

from hw5.AnimalFactory import AnimalFactory
from hw5.Shop import Shop


class Test(unittest.TestCase):

    def test_1(self):
        """
        Check init method of shop
        """
        shop = Shop("My shop", 10000)
        self.assertEqual(shop.get_name(), "My shop",
                         msg="The name is not the same")
        self.assertEqual(shop.balance, 10000,
                         msg="The balance is not the same")
        self.assertEqual(shop.get__animals(), {},
                         msg="The dict is not the same")

    def test_2(self):
        """
        Check if one animal add to shop
        """
        dog_1 = AnimalFactory.create("Dog", "dog_1", 10, 60)
        shop = Shop("My shop", 10000)
        shop.__add__(dog_1)
        dict_compare = {dog_1.nick_name: dog_1}
        self.assertEqual([i for i in dict_compare if i not in shop.get__animals()], [],
                         msg="The animal was not added to the shop")

    def test_3(self):
        """
        Check if list animals add to shop
        """
        cat_1 = AnimalFactory.create("Cat", "cat_1", 10, 10)
        cat_2 = AnimalFactory.create("Cat", "cat_2", 5, 20)
        cat_3 = AnimalFactory.create("Cat", "cat_3", 15, 30)
        shop = Shop("My shop", 10000)
        list_animals = [cat_1, cat_2, cat_3]
        shop.__add__(list_animals)
        dict_compare = {x.nick_name: x for x in list_animals}
        self.assertEqual([i for i in dict_compare if i not in shop.get__animals()], [],
                         msg="The animals was not added to the shop")

    def test_4(self):
        """
        Check the count of animal in shop
        """
        shop = Shop("My shop", 100)
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 10)
        shop.__add__(parrot_1)
        self.assertEqual(shop.num_of_animals(), 1)

        parrot_2 = AnimalFactory.create("Parrot", "parrot_2", 10, 10)
        snake_1 = AnimalFactory.create("Snake", "snake_1", 10, 10)
        list_add = [snake_1, parrot_2]
        shop.__add__(list_add)
        self.assertEqual(shop.num_of_animals(), 3)

    def test_5(self):
        """
        Check remove animal from shop
        """
        shop = Shop("My shop", 100)
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 10)
        shop.__add__(parrot_1)
        self.assertEqual(shop.sell("parrot_1"), parrot_1)

    def test_6(self):
        """
        Check play method
        """
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 9)
        snake_1 = AnimalFactory.create("Snake", "snake_1", 20, 25)
        list_add = [parrot_1, snake_1]
        shop = Shop("My shop", 10000)
        shop.__add__(list_add)
        self.assertEqual(shop.play("parrot_1", "snake_1"), "snake_1 winner\nparrot_1 loser")

    def test_7(self):
        """
        Too bad there's no documentation in the code.
        Now you're going to have to read it to understand what the test does.
        """
        cat_1 = AnimalFactory.create("Cat", "cat_1", 8, 9)
        self.assertEqual(cat_1.speak(), "cat_1 says meow")

    def test_8(self):
        """
        Dog speak
        """
        dog_1 = AnimalFactory.create("Dog", "dog_1", 8, 9)
        self.assertEqual(dog_1.speak(), "dog_1 says woof woof")

    def test_9(self):
        """
        Dog wins
        """
        dog_1 = AnimalFactory.create("Dog", "dog_1", 8, 9)
        self.assertEqual(dog_1.win(), "dog_1 says woof woof dog_1 winner")

    def test_10(self):
        """
        Turtle move
        """
        turtle_1 = AnimalFactory.create("Turtle", "turtle_1", 8, 91)
        turtle_2 = AnimalFactory.create("Turtle", "turtle_1", 8, 45.5)
        turtle_1.move()
        self.assertEqual(turtle_1, turtle_2)

    def test_11(self):
        """
        Snake moves
        """
        Snake_1 = AnimalFactory.create("Snake", "Snake_1", 8, 9)
        Snake_1.move()
        self.assertEqual(Snake_1, Snake_1)

    def test_12(self):
        """
        ge Reptiles
        """
        Snake_1 = AnimalFactory.create("Snake", "Snake_1", 8, 10)
        turtle_2 = AnimalFactory.create("Turtle", "turtle_1", 8, 50)
        a = Snake_1 >= turtle_2
        self.assertEqual(a, True)

    def test_13(self):
        """
        Turtle lose
        """
        Turtle_1 = AnimalFactory.create("Turtle", "Turtle_1", 18, 9)
        self.assertEqual(Turtle_1.loss(), "Turtle_1 loser I always lose")

    def test_14(self):
        """
        GE bird
        """
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 9)
        parrot_2 = AnimalFactory.create("Parrot", "parrot_2", 10, 10)
        parrot_1.fly = "False"
        self.assertEqual(parrot_1 >= parrot_2, False)

    def test_15(self):
        """
        GE bird
        """
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 11)
        Parrot_2 = AnimalFactory.create("Parrot", "Parrot_2", 10, 13)
        self.assertEqual(parrot_1 >= Parrot_2, False)

    def test_16(self):
        """
        get type
        """
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 11)
        self.assertEqual(parrot_1.get_type(), "Parrot")

    def test_17(self):
        """
        get power
        """
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 11)
        self.assertEqual(parrot_1._get__power(), 11.0)

    def test_18(self):
        """
        set power
        """
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 11)
        parrot_1._set__power(3)
        self.assertEqual(parrot_1._get__power(), 3.0)

    def test_19(self):
        """
        animal win
        """
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 8, 9)
        self.assertEqual(parrot_1.win(), "parrot_1 winner")

    def test_20(self):
        """
        animal loss
        """
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 8, 9)
        self.assertEqual(parrot_1.loss(), "parrot_1 loser")

    def test_21(self):
        """
        Turtle loss
        """
        Turtle_1 = AnimalFactory.create("Turtle", "Turtle_1", 8, 9)
        self.assertEqual(Turtle_1.loss(), "Turtle_1 loser I always lose")

    def test_22(self):
        """
        Snake loss
        """
        Snake_1 = AnimalFactory.create("Snake", "Snake_1", 8, 9)
        self.assertEqual(Snake_1.loss(), "Snake_1 loser")

    def test_23(self):
        """
        Check repr
        """
        Snake_1 = AnimalFactory.create("Snake", "Snake_1", 18, 29)
        self.assertEqual(Snake_1.__repr__(), "Name: Snake_1, Price: 18.0 NIS, Power: 29.0")

    def test_24(self):
        """
        Check eq
        """
        Snake_1 = AnimalFactory.create("Snake", "Snake_1", 1, 100)
        self.assertEqual(Snake_1 == 3, False)

    def test_25(self):
        """
        Check play method
        """
        parrot_1 = AnimalFactory.create("Parrot", "Parrot_1", 10, 9)
        Parrot_2 = AnimalFactory.create("Parrot", "Parrot_2", 20, 25)
        Parrot_2.fly = False
        list_add = [parrot_1, Parrot_2]
        shop = Shop("My shop", 10000)
        shop.__add__(list_add)
        self.assertEqual(shop.play("Parrot_1", "Parrot_2"), "Parrot_1 winner\nParrot_2 loser")

    def test_26(self):
        """
        Check play method
        """
        Turtle_1 = AnimalFactory.create("Turtle", "Turtle_1", 10, 9)
        Parrot_2 = AnimalFactory.create("Parrot", "Parrot_2", 20, 25)
        Parrot_2.fly = False
        list_add = [Turtle_1, Parrot_2]
        shop = Shop("My shop", 10000)
        shop.__add__(list_add)
        self.assertEqual(shop.play("Turtle_1", "Parrot_2"), "Parrot_2 winner\nTurtle_1 loser I always lose")


if __name__ == "__main__":
    unittest.main()
