class Soda:
    def __init__(self, add_on=None):
        self.add_on = add_on

    def show_my_drink(self):
        if self.add_on:
            print(f"Газировка и {self.add_on}")
        else:
            print("Обычная газировка")

drink1 = Soda()
drink1.show_my_drink() 

drink2 = Soda("None")
drink2.show_my_drink()  

drink3 = Soda("мята")
drink3.show_my_drink()  
