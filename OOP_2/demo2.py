class Hello:
    x = 2
    y = 3

    def one(self):
        print("Ordinary method!!!")
        print(self.y)
        print(self.x)

    @classmethod
    def two(cls):
        print("Class method")
        print(cls.y)
        print(cls.x)

    @staticmethod
    def three():
        print("Static method")
        # print(self.x)
        # print(self.y)

    def __call__(self):
        print("I`m  in call")
        print(f"Values : x= {self.x}, y = {self.y} ")


example = Hello()
example.one()

example.two()
Hello.two()

Hello.three()

example()
print(example)
