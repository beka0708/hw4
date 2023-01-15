class A:
    def __init__(self, name):
        self.name = name


class B:
    def __init__(self, age):
        self.age = age


class C:
    def user(self):
        return f'i am {self.name}'


class D:
    def ages(self):
        return f'i am {self.age}'


class F(D, C, B, A):
    def __init__(self, name, age):
        A.__init__(self, name)
        B.__init__(self, age)


users = F('Beka', 19)
print(users.user())
print(users.ages())