from models import Animal, Dog, Cat


def main():
    dog = Dog("Rex", 5, 20, "Labrador")
    cat = Cat("Milo", 3, 5, "Black")
    animal = Animal("Generic Animal", 2, 10)
    animals = [dog, cat, animal]
    for a in animals:
        print(a)
        print(a.make_sound())
        print(a.eat())
        print()

if __name__ == "__main__":
    main()