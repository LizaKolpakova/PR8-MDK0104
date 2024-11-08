class Nikola:
    def __init__(self, name, age):
        if name.lower() == "николай":
            self.name = name
        else:
            self.name = "Я не {}, а Николай".format(name)
        self.age = age

    
    def __setattr__(self, key, value):
        raise AttributeError("Нельзя добавлять новые атрибуты к экземпляру класса Nikola.")

    
    def __init__(self, name, age):
        super().__setattr__('age', age)
        if name.lower() == "николай":
            super().__setattr__('name', name)
        else:
            super().__setattr__('name', f"Я не {name}, а Николай")


try:
    person1 = Nikola("Вова", 25)
    print(person1.name)  
    print(person1.age)   

    person2 = Nikola("Николай", 30)
    print(person2.name)  
    print(person2.age)   

    person1.patronymic = "Иванович"  
except AttributeError as e:
    print(e)

