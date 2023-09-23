class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def test2(self, age=None):
        if age is not None:
            self.age = age

        if self.age is not None:
            print(f"Привет, мне {self.age} лет.")
        else:
            print("Привет.")

# Создаем экземпляр класса Person
person = Person()

# Вызываем метод test2 на экземпляре класса
person.test2(35)  # Вызываем метод test2 с новым возрастом
