from builder import ConcreteBuilder1, ConcreteBuilder2
from director import Director

def main():
    builder1 = ConcreteBuilder1()
    director = Director(builder1)
    director.construct()
    product1 = builder1.get_result()
    product1.show()

    builder2 = ConcreteBuilder2()
    director = Director(builder2)
    director.construct()
    product2 = builder2.get_result()
    product2.show()


if __name__ == "__main__":
    main()
