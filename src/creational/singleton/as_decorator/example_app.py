from creational.singleton.as_decorator.singleton import singleton


def main() -> None:
    print(":::::::::::::::::  Singleton Implementation Test  :::::::::::::::::")

    print("Case 1: Singleton classes are initialized once and different class hierarchies are not mixed")

    @singleton
    class A:
        pass

    @singleton
    class B:
        pass

    a1 = A()
    a2 = A()
    b = B()

    print(a1 is a2)
    print(a1 is not b)

    print("Case 2: Singleton decorator allow to pass arguments to the class constructor")

    @singleton
    class SingletonClass:
        def __init__(self, value: str = "default"):
            self.value = value

    instance1 = SingletonClass("test")
    instance2 = SingletonClass("different")

    print(f"{instance1.value=}")
    print(f"{instance2.value=}")
    print(instance1 is instance2)

    print("Case 3: Singleton-decorated classes preserve their original metadata thanks to wraps")

    print(SingletonClass.__name__)
    print(SingletonClass.__qualname__)


# Example usage
if __name__ == "__main__":
    main()
