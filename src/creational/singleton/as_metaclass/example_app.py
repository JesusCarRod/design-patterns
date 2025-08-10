from creational.singleton.as_metaclass.singleton import SingletonMeta


def main() -> None:
    print(":::::::::::::::::  Singleton Implementation Test  :::::::::::::::::")

    print("Case 1: Singleton class instances are initialized once")

    class Singleton(metaclass=SingletonMeta):
        pass

    s1 = Singleton()
    s2 = Singleton()

    print(s1 is s2)

    print(
        "Case 2: Singleton classes are initialized once and different class hierarchies are not mixed"
    )

    class A(metaclass=SingletonMeta):
        pass

    class B(A):
        pass

    class C(metaclass=SingletonMeta):
        pass

    a1 = A()
    a2 = A()
    b1 = B()
    b2 = B()
    c = C()

    print(a1 is a2)
    print(b1 is b2)
    print(a1 is not b1)
    print(a1 is not c)
    print(b1 is not c)

    print(
        "Case 3: Singleton classes can overwrite __new__ and __init__ without affection"
    )

    class CheatingSingleton(metaclass=SingletonMeta):
        def __new__(cls, *args, **kwargs):
            print("CheatingSingleton __new__ called!")
            if not hasattr(cls, "_instance"):
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self, name: str) -> None:
            print("CheatingSingleton __init__ called!")
            self.name = name

    cheating1 = CheatingSingleton("John")
    cheating2 = CheatingSingleton("Jane")

    print(cheating1.name == "John")
    print(cheating2.name == "John")
    print(cheating1 is cheating2)


if __name__ == "__main__":
    main()
