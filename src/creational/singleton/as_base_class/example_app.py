from creational.singleton.as_base_class.singleton import Singleton


def main() -> None:
    print(":::::::::::::::::  Singleton Implementation Test  :::::::::::::::::")

    print("Case 1: Simple singleton instances are initialized once")

    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)

    print(
        "Case 2: Singleton classes are initialized once and different class hierarchies are not mixed"
    )

    class A(Singleton):
        pass

    class B(A):
        pass

    class C(Singleton):
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

    print("Case 3: _setup method allows initializing custom class attributes")

    class DatabaseConnection(Singleton):
        def _setup(self, connection_string: str) -> None:
            self.connection_string = connection_string

    class Logger(Singleton):
        def _setup(self, log_level: str) -> None:
            self.log_level = log_level

    db = DatabaseConnection(connection_string="postgresql://")
    logger = Logger(log_level="INFO")

    print(db.connection_string)
    print(logger.log_level)

    print("Case 4: override of __init__ in subclasses not allowed, use _setup")

    try:

        class CheatingClass(Singleton):
            def __init__(self) -> None:
                print("__init__ ovtherwritten")

    except TypeError:
        print("Expected exception when defining the class raised")


if __name__ == "__main__":
    main()
