class KgToPounds:
    def __init__(self, kg):
        self._kg = kg  

    @property
    def kg(self):        
        return self._kg

    @kg.setter
    def kg(self, value):        
        if value < 0:
            raise ValueError("Количество килограммов не может быть отрицательным.")
        self._kg = value

    def to_pounds(self):       
        return self._kg * 2.20462  


kg_to_pounds = KgToPounds(2)
print(f"Килограммы: {kg_to_pounds.kg}")  
print(f"Фунты: {kg_to_pounds.to_pounds()}")  

kg_to_pounds.kg = 5  
print(f"Обновленные килограммы: {kg_to_pounds.kg}")  
print(f"Фунты: {kg_to_pounds.to_pounds()}")  