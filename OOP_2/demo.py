class A:
    def __init__(self):
        print("I`m in __A__INIT-method")
        self.value = 18

    def method(self):
        print("I`m in method!! __A__")
        self.value += 10


class B:
    def __init__(self):
        # A.__init__(self)
        super().__init__()
        print("I`m in __B__ init ")
        self.name = "Taras"

    def method(self):
        print("I`m in method!! __B__")


class C(B, A):
    def __init__(self):
        super().__init__()
        print("I`m in __C__ init ")
        self.color = "brown"

    # def method(self):
    #     print("I`m in method!! __C__")
    #     # super(B, self).method()
    #     A.method(self)


a = A()
print(a.value)
a.method()
print(a.value)

print("=" * 100)

# bb = B()
# print(bb.value)
# bb.method()
# print(bb.value)
#
# print("=" * 100)

cc = C()
print(cc.value)
cc.method()
print(cc.value)

# print(cc.name)
print(cc.color)
