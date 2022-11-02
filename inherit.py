class Animal:
    def __init__(self,name):
        self.name = name

    def who(self):
        print(self.name)

    def dance(self):
        print(":)? Dance why the fk i need to dance")

class Dog(Animal):

    """
        def __init__(self,name):
            self.name = name
    """

    def __init__(self):
        super().__init__("Dog")
        self.haha  = True

    def set_name(self,name):
        self.name = name

    def laugh(self):
        print("haha" if self.haha else ":(")

    """
        def who(self):
            print(self.name)

        def dance(self):
            print(":)? Dance why the fk i need to dance")
    """
    
    def dance(self,happy_level):
        print("I love to dance happy dance")
        print(happy_level)


d = Dog()
d.dance(30)